#Config__________________________________________________________________

rolels = ["Inconnu", "FortniteNews","SauverLeMondeNews","R6News","MinecraftNews"]
canalls = [669579220212776991,742054123414749184,742054123414749184,742054123414749184,742054123414749184]
messagels = [0,742057446490636349,742057446490636349,742057446490636349,742057446490636349]

a = len(rolels)

#________________________________________________________________________
# on importe le module discord.py
import discord

from discord.utils import get
# ajouter un composant de discord.py
from discord.ext import commands


# créer le bot
bot = commands.Bot(command_prefix='!')
warnings = {}

# détecter quand le bot est allumé
@bot.event
async def on_ready():
    print("Bot prêt")
    await bot.change_presence(activity=discord.Game("attribuer les rôle !"))


# détecter quand quelqu'un ajoute un emoji sur un message

@bot.event
async def on_raw_reaction_add(payload):

    global role, canalbon , emojibon


    emoji = payload.emoji.name  # recupere l'emoji
    canal = payload.channel_id  # recupere le numero du canal
    message = payload.message_id  # recupere le numero du message
    membre = bot.get_guild(payload.guild_id).get_member(payload.user_id) # recupere celui qui a mit l'emoji



    role = get(bot.get_guild(payload.guild_id).roles, name=rolels[0])
    canalbon = canalls[0]
    emojibon = rolels[0]

    if canal == canalbon and emoji == emojibon:  # c'est pour accepter les règles
        await membre.add_roles(role)

    for n in range (a):  # c'est une boucle

      canalbon = canalls[n]
      messagebon = messagels[n]
      emojibon = rolels[n]
      role = get(bot.get_guild(payload.guild_id).roles, name=rolels[n])

      if  canal == canalbon and message == messagebon and emoji == emojibon: # on vérifie
        await membre.add_roles(role) # on lui donne le grade

@bot.event
async def on_raw_reaction_remove(payload):

    global role, canalbon, emojibon

    emoji = payload.emoji.name  # recupere l'emoji
    canal = payload.channel_id  # recupere le numero du canal
    message = payload.message_id  # recupere le numero du message
    membre = bot.get_guild(payload.guild_id).get_member(payload.user_id)

    role = get(bot.get_guild(payload.guild_id).roles, name=rolels[0])

    canalbon = canalls[0]
    emojibon = rolels[0]

    if canal == canalbon and emoji == emojibon:  # c'est pour ne plus accepter les règles
        await membre.remove_roles(role)

    for n in range(a):  # c'est une boucle

      canalbon = canalls[n]
      messagebon = messagels[n]
      emojibon = rolels[n]
      role = get(bot.get_guild(payload.guild_id).roles, name=rolels[n])

      if  canal == canalbon and message == messagebon and emoji == emojibon:  # on vérifie
        await membre.remove_roles(role)

# phrase
print("Lancement du bot...")

# connecter au serveur
bot.run(jeton)


