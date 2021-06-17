import discord
import os
import random
import re
from stay_awake import stay_awake
import paralleldots

stay_awake()

token = os.environ['TOKEN']
bot = discord.Client()

API_KEY="N5U7mnmq9gGLwxVjhPjOncSEJScUSG2eIh6l63XCRWc"
paralleldots.set_api_key(API_KEY)


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
  "f_keyboard",
  "party_blahaj",
  "party_blob",
  "cat_heartbongo",
  "drinking_milk"
  ]


custom_emoji = {}


# Any of these emojis will be randomly selected to add_reaction for positive sentiments
positive={
  "a":"🥲",
  "b":"☺️",
  "c":"🅿"
  # Add more emojis
  }

# Any of these emojis will be randomly selected to add_reaction for neutral sentiments
neutral={
  "a":"🙃",
  "b":"👤"
  # Add more emojis
  }


# Getting sentiments
def get_sentiment(message):
  sentiments=paralleldots.sentiment(message.content).get('sentiment')
  Max_Probability=max(sentiments, key= sentiments.get)
  return [Max_Probability,sentiments[Max_Probability]]
  

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
  
  # React with relevant emoji or send "F" in message by sentiment analysis
  sentiment=get_sentiment(message)
  print(sentiment)
  if sentiment[1]>0.50 and message.author != bot.user:
    my_emoji=neutral if sentiment[0]=="neutral" or sentiment[0]== "negative" else positive
    await autoreact(message,sentiment[0]=="neutral" or sentiment[0]=="positive",random.choice(list(my_emoji.values())))
    await automessage(message, sentiment[0]=="negative", "F")
    
  # prepare the message and its data
  text = message.content.lower().strip()
  mentioned = []
  for mention in message.mentions:
    mentioned.append(mention.id)

  # autoreactions
  chakram = 694925078781100153 in mentioned or "chakram" in text or "blahaj" in text or "astrid" in text or "warrior princess" in text
  vijay = 703703244714672207 in mentioned or "vijay" in text or "vj" in text
  dory = 528447721816981505 in mentioned or "dory" in text
  zoheb = 716186953510551572 in mentioned or "zoheb" in text
  boba_emoji = [emoji["boba"], custom_emoji["party_parrot_boba"], custom_emoji["kitty_boba"]]
  boba = "boba" in text or "bubble tea" in text or "milk tea" in text
  def hello(i): return i == 'hi' or i == 'hey' or i == 'hello' or i == 'welcome'

  split = text.split()
  autoreactions = [
    ["milk" in text, [emoji["milk"], emoji["cow"]]],
    [chakram, [custom_emoji["party_blahaj"]]],
    [vijay or re.search("yee+t", text), [custom_emoji["yeet"]]],
    [dory, [custom_emoji["dory_swimming"]]],
    [zoheb, [custom_emoji["drinking_milk"]]],
    [boba, boba_emoji],
    ["rip" in text, [custom_emoji["rip"]]],
    ["dab" in text, [custom_emoji["kirby_dab"]]],
    [text == "f", [custom_emoji["f_in_chat"], custom_emoji["f_keyboard"]]],
    ["love" in text or "heart" in text, [custom_emoji["cat_heartbongo"]]],
    ["🥳" in text or "party" in text or "woo" in text, [custom_emoji["party_blob"]]],
    [True in [hello(i) for i in split], [emoji["wave"]]]
  ]

  for autoreaction in autoreactions:
    await autoreact(message, autoreaction[0], autoreaction[1])

  # autoreplies
  random_bot_reply = random.choice(["you rang? ☎️", "hi 👋", "that's me 🤪", "👀 yes?"])
  f_in_chat = re.search("(can i get)( an| a)? f( in chat)?", text) or "f in chat" in text or "f pls" in text or "i want f" in text
  autoreplies = [
    ["mr. milk bobat" in text or "bobat" in text or 853780610183462933 in mentioned, random_bot_reply],
    [f_in_chat, "F"]
  ]

  for autoreply in autoreplies:
    await automessage(message, autoreply[0], autoreply[1])

async def autoreact(message, condition, emojis):
  if condition:
    for emoji in emojis:
      await message.add_reaction(emoji)

async def automessage(message, condition, response):
  if condition:
    await message.channel.send(response)

bot.run(token)
