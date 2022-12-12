from flask import Flask
from aiogram import Bot, Dispatcher, executor, types
from multiprocessing import Process


app = Flask(import_name=__name__)

bot = Bot(token="5787914744:AAGEMphfea_vetIz7EPe1RnKJaLOT0w3QwQ")
dispatcher = Dispatcher(bot=bot)


def bot_start_polling():
    executor.start_polling(dispatcher=dispatcher, skip_updates=True)


@dispatcher.message_handler(commands=['start'])
async def bot_handler_start(message: types.Message):
    await message.reply('Foo')


@app.get(rule='/bot')
def start_bot():
    bot_process = Process(target=bot_start_polling)
    bot_process.start()

    return str(bot_process.pid)


if __name__ == '__main__':
    app.run()
