from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
  return "Your bot is alive And Ready To Raid!! For More Awesome Shit Join Our Discord Server!: https://discord.gg/ZQdwGKMSDv"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()
