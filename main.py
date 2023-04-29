from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ChatActions
import random
from nerogpt_backend import *

banlist = [] # Enter User ID for Banlist
openai_api = "" # Enter your OpenAI API
telegram_api = "" # Enter your Telegram API
bot = Bot(token=telegram_api)
dp = Dispatcher(bot)
@dp.message_handler()
async def handle_message(message: types.Message):
    if message.chat.type == 'private':
        await message.answer('Hello. 👋\nThis is Open-Source NeroGPT, created by AriGPT (ArmaniOS Foundation)\nBot is not for using in PM, use in in chats, groups, etc. 😊\nBot commands:\n - /nerogpt prompt - get answer from your prompt \n- /wipedialog - wiping your dialog\n\nProject link: https://github.com/csoftware-arigpt/Open-NeroGPT')
    elif message.chat.type != 'private':
        if "/nerogpt" in message.text:
           try:
                if message.from_user.id not in banlist:
                    text = message.text
                    text = text.replace("/nerogpt ", "")
                    await bot.send_chat_action(message.chat.id, action=ChatActions.TYPING)
                    e = await question_answer(text, message.from_user.id, openai_api)
                    await message.answer(e, reply=True)
                else:
                    await message.answer("Banned", reply=True)
           except:
               await message.answer("Error while generating  🚫", reply=True)
        elif "/wipedialog" in message.text and message.from_user.id not in banlist:
                try:
                    await wipedialog(message.from_user.id)
                    await message.answer("History is wiped", reply=True)
                except:
                    await message.answer("Error while wiping 🚫", reply=True)
if __name__ == '__main__':
    executor.start_polling(dp)
