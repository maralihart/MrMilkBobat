from flask import Flask
from threading import Thread
# code from FreeCodeCamp
app = Flask("")

@app.route('/')
def home():
  return "Hey, I'm awake!"

def run():
  app.run(host='0.0.0.0', port=8080)

def stay_awake():
  t = Thread(target=run)
  t.start()
