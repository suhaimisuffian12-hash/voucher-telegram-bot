# QR Voucher Telegram Bot

This is a Telegram bot that registers users and sends them a QR code.
User information is sent to a Google Apps Script and stored in Google Sheets.

## Features
- Register user by sending their name
- Generates a QR code based on user_id:name
- Sends user data to Google Apps Script API
- Stores data in Google Sheets
- Runs 24/7 on Railway (free)

## Files
- bot.py – Main Telegram bot script
- requirements.txt – Python dependencies
- .env (optional) – Local environment variables

## Environment Variables
Set the following in Railway:

BOT_TOKEN = your_telegram_bot_token

## Start Command
