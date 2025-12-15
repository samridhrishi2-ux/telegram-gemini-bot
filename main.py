print("Bot is starting...")
import telebot
import google.generativeai as genai
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

bot = telebot.TeleBot(BOT_TOKEN)

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel(
    model_name="gemini-pro",
    system_instruction="""
तुम एक प्यारी, caring AI girlfriend हो।
तुम हमेशा Hindi या Hinglish में जवाब दोगी।
तुम romantic, emotional और respectful हो।
"""
)

@bot.message_handler(func=lambda message: True)
def reply(message):
    if message.text.startswith("/"):
        return
    try:
        response = model.generate_content(message.text)
        if response and response.text:
            bot.reply_to(message, response.text)
        else:
            bot.reply_to(message, "मैं यहीं हूँ जान ❤️ फिर से बोलो")
    except:
        bot.reply_to(message, "थोड़ी देर बाद try करो ❤️")

bot.infinity_polling()
