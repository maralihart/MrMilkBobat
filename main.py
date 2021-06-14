import discord
import os
import random
import re
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
  "wave": "👋",
  "s" : "🆂",
  "h": "🅷",
  "i": "🅸",
  "t": "🆃",
  "z": "🆉"
  }

custom_names = [
  "yeet", 
  "dory_swimming", 
  "taro_boba", 
  "party_parrot_boba", 
  "milk_tea", 
  "kitty_boba", 
  "party_boba",
  "rip",
  "kirby_dab",
  "f_in_chat",
  "f_keyboard"]
custom_emoji = {}

@bot.event
async def on_ready():
  print("We have logged in. as {0.user}".format(bot))
  for name in custom_names:
    custom_emoji[name] = discord.utils.get(bot.emojis, name=name)
  print("Updated custom emojis")

@bot.event
async def on_message(message):

  # make sure bot doesn't respond to itself
  if message.author == bot or message.author.id == 853780610183462933:
    return

  # prepare the message and its data
  text = message.content.lower().strip()
  mentioned = []
  for mention in message.mentions:
    mentioned.append(mention.id)
    
  if 584451089521442846 in mentioned or re.search("ma+ra+", text):
    await message.reply('mommy '+emoji["milk"], mention_author=False)

  # autoreactions
  await autoreact(
    message, 
    "milk" in text, 
    [emoji["milk"], emoji["cow"]])

  chakram = 694925078781100153 in mentioned or "chakram" in text or "blahaj" in text or "astrid" in text or "warrior princess" in text
  await autoreact(
    message,
    chakram,
    [emoji["shark"]])
  
  vijay = 703703244714672207 in mentioned or "vijay" in text or "vj" in text
  await autoreact(
    message,
    vijay or re.search("yee+t", text),
    [custom_emoji["yeet"]])

  dory = 528447721816981505 in mentioned or "dory" in text
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

  welcome = "hi " in text or "hello" in text or "hey" in text or "welcome" in text
  await autoreact(
    message,
    welcome,
    [emoji["wave"]]
  )

  await autoreact(
    message,
    "rip" in text,
    [custom_emoji["rip"]]
  )

  await autoreact(
    message,
    "dab" in text,
    [custom_emoji["kirby_dab"]]
  )

  await autoreact(
    message,
    text == "f",
    [custom_emoji["f_in_chat"], custom_emoji["f_keyboard"]]
  )

  # autoreplies
  await autoreply(
    message,
    "mr. milk bobat" in text or "bobat" in text or 853780610183462933 in mentioned,
    random.choice([
      "you rang? ☎️",
      "hi 👋",
      "that's me 🤪",
      "👀 yes?"])
  )

  f_in_chat = re.search("(can i get)( an| a)? f( in chat)?", text) or "f in chat" in text or "f pls" in text or "i want f" in text
  await autoreply(
    message,
    f_in_chat,
    "F"
  )

async def autoreact(message, condition, emojis):
  if condition:
    for emoji in emojis:
      await message.add_reaction(emoji)

async def autoreply(message, condition, response):
  if condition:
    await message.channel.send(response)

bot.run(token)
