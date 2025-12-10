import telebot
import requests
import qrcode
import io
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_URL = "https://script.google.com/macros/s/AKfycby_DkJrtXgR0cRUti9RXWz0LMeuVHMfxH8Iz8ZDNq8afhaxRzVp3FkUBSZT2wE8k4br/exec"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(msg):
    bot.reply_to(msg, "Send your name to register and get your QR code.")

@bot.message_handler(func=lambda m: True)
def register(msg):
    user_id = msg.from_user.id
    name = msg.text.strip()

    payload = {
        "user_id": user_id,
        "name": name
    }

    try:
        requests.post(API_URL, json=payload)
    except:
        bot.reply_to(msg, "❌ Failed to send data to Google Apps Script.")
        return

    # Generate QR
    qr = qrcode.make(f"{user_id}:{name}")
    buf = io.BytesIO()
    qr.save(buf, format="PNG")
    buf.seek(0)

    bot.send_photo(
        msg.chat.id,
        buf,
        caption="Here is your QR code."
    )

bot.polling(none_stop=True)
