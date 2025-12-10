import os
import telebot
import requests
import qrcode
import io
from flask import Flask, request

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_URL = "https://script.google.com/macros/s/AKfycby_DkJrtXgR0cRUti9RXWz0LMeuVHMfxH8Iz8ZDNq8afhaxRzVp3FkUBSZT2wE8k4br/exec"

bot = telebot.TeleBot(BOT_TOKEN, threaded=False)
server = Flask(__name__)

# ================================
# Telegram Bot Handlers
# ================================
@bot.message_handler(commands=['start'])
def start(msg):
    bot.reply_to(msg, "Send your name to register and get your QR code.")

@bot.message_handler(func=lambda m: True)
def register(msg):
    user_id = msg.from_user.id
    name = msg.text

    # Send to Google Apps Script
    requests.post(API_URL, json={"user_id": user_id, "name": name})

    # Generate QR code
    qr = qrcode.make(f"{user_id}:{name}")
    buf = io.BytesIO()
    qr.save(buf, format="PNG")
    buf.seek(0)

    bot.send_photo(msg.chat.id, buf, caption="Here is your QR code.")

# ================================
# Flask Webhook Endpoint
# ================================
@server.route("/" + BOT_TOKEN, methods=["POST"])
def webhook():
    json_str = request.stream.read().decode("utf-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "OK"
