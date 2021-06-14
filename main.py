import discord
import os
from stay_awake import stay_awake

stay_awake()

token = os.environ['TOKEN']
bot = discord.Client()

emoji = {
  "milk": "🥛",
  "cow": "🐄",
  "shark": "🦈",
  "basketball": "🏀",
  "boba": "🧋",
  "wave": "👋"
  }

custom_names = [
  "yeet", 
  "dory_swimming", 
  "taro_boba", 
  "party_parrot_boba", 
  "milk_tea", 
  "kitty_boba", 
  "party_boba"]
custom_emoji = {}

@bot.event
async def on_ready():
  print("We have logged in. as {0.user}".format(bot))
  for name in custom_names:
    custom_emoji[name] = discord.utils.get(bot.emojis, name=name)
  print("Updated custom emojis")

@bot.event
async def on_message(message):
  if message.author == bot:
    return

  text = message.content.lower().strip()

  await autoreact(
    message, 
    "milk" in text, 
    [emoji["milk"], emoji["cow"]])

  chakram = message.author.id == "694925078781100153" or "chakram" in text or "blahaj" in text
  await autoreact(
    message,
    chakram,
    [emoji["shark"]])
  
  vijay = message.author.id == "703703244714672207" or "vijay" in text or "vj" in text or "yeet" in text
  await autoreact(
    message,
    vijay,
    [emoji["basketball"], custom_emoji["yeet"]])

  dory = message.author.id == "528447721816981505" or "dory" in text
  await autoreact(
    message, 
    dory,
    [custom_emoji["dory_swimming"]])

  boba_emoji = [
    emoji["boba"], 
    custom_emoji["party_parrot_boba"], 
    custom_emoji["kitty_boba"]]
  boba = "boba" in text or "bubble tea" in text or "milk tea" in text
  await autoreact(
    message,
    boba,
    boba_emoji
  )

  welcome = "hi" in text or "hello" in text or "hey" in text or "welcome" in text
  await autoreact(
    message,
    welcome,
    emoji["wave"]
  )

async def autoreact(message, condition, emojis):
  if condition:
    for emoji in emojis:
      await message.add_reaction(emoji)

bot.run(token)
