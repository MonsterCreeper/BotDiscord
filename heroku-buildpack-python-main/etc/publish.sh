#!/bin/bash

set -e

BP_NAME=${1:-"heroku/python"}

curVersion=$(heroku buildpacks:versions "$BP_NAME" | awk 'FNR == 3 { print $1 }')
newVersion="v$((curVersion + 1))"

read -p "Deploy as version: $newVersion [y/n]? " choice
case "$choice" in
  y|Y ) echo "";;
  n|N ) exit 0;;
  * ) exit 1;;
esac

originMain=$(git rev-parse origin/main)
echo "Tagging commit $originMain with $newVersion... "
git tag "$newVersion" "${originMain:?}"
git push origin refs/tags/$newVersion

heroku buildpacks:publish "$BP_NAME" "$newVersion"

if [ $(git tag | grep -q previous-version) ]; then
    echo "Updating previous-version tag"
    git tag -d previous-version
    git push origin :previous-version
    git tag previous-version latest-version
fi
if [ $(git tag | grep -q latest-version) ]; then
    echo "Updating latest-version tag"
    git tag -d latest-version
    git push origin :latest-version
    git tag latest-version "${originMain:?}"
    git push --tags
fi

echo "Done."
