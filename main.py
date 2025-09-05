from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher, executor, types
from groq import Groq

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

client = Groq(api_key=GROQ_API_KEY)

class Reference:
    def __init__(self) -> None:
        self.response = ""

reference = Reference()

model_name = "llama-3.1-8b-instant"

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dispatcher = Dispatcher(bot)

def clear_past():
    reference.response = ""

@dispatcher.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.reply("Hi...\nI am Mehu! Created by Mehedi Hassan.\nHow can I assist you?")

@dispatcher.message_handler(commands=['help'])
async def helper(message: types.Message):
    help_command = (
        "Hi there, I'm Mehu - created by Mehedi Hassan.\n"
        "Please follow these commands:\n"
        "/start - to start the conversation.\n"
        "/clear - to clear the past conversation and context.\n"
        "/help - to get this help menu."
    )
    await message.reply(help_command)

@dispatcher.message_handler(commands=['clear'])
async def clear(message: types.Message):
    clear_past()
    await message.reply("I have cleared the previous conversation and context.")

@dispatcher.message_handler()
async def chatgpt(message: types.Message):
    user_input = message.text.lower().strip()
    print(f">>> USER:\n\t{user_input}")

    # --- Greeting detection ---
    greetings = ["assalamu alaikum", "assalamualaikum"]
    if any(greet in user_input for greet in greetings):
        reply_text = (
            "Wa Alaikum Salam! 🌸\n"
            "I am Mehu! Created by Mehedi Hassan.\n"
            "How can I assist you now?"
        )
        await bot.send_message(chat_id=message.chat.id, text=reply_text)
        return

    # --- Otherwise, forward to Groq ---
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "assistant", "content": reference.response},
            {"role": "user", "content": message.text},
        ],
    )

    reply_text = response.choices[0].message.content
    reference.response = reply_text

    print(f">>> Mehu:\n\t{reply_text}")
    await bot.send_message(chat_id=message.chat.id, text=reply_text)

if __name__ == "__main__":
    executor.start_polling(dispatcher, skip_updates=False)