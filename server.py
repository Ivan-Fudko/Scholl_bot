from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import CommandStart, CommandHelp, Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from data import db_session
from data.name_answers import Answers
from keyboards.inline.choice_but_start_test import towers

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

db_session.global_init("bot_DB.db")
db_sess = db_session.create_session()


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if not (db_sess.query(Answers).filter(Answers.user_id == message.from_user.id).first()):
        user = Answers()
        user.user_id = message.from_user.id
        db_sess.add(user)
        db_sess.commit()
    await message.answer(f"Здравствуйте, {message.from_user.full_name}!\nНапишите комманду"
                         f" \help чтобы получить подробную информацию о возможнастях бота")


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/help - Получить справку",
            "/choose_color - Выбрать цвет для цветного дня. Итоги голосования подводяться в среду.",)

    await message.answer("\n".join(text))


@dp.message_handler(commands=['all_delete'])
async def delete(message: types.Message):
    id = message.from_user.id
    if id == 888211046:
        list_button_name = []
        with open('listfile.txt', 'r') as filehandle:
            for line in filehandle:
                currentPlace = line[:-1]
                list_button_name.append(currentPlace)
        users = db_sess.query(Answers).all()
        first = db_sess.query(Answers).filter(Answers.answer == list_button_name[0]).count()
        second = db_sess.query(Answers).filter(Answers.answer == list_button_name[1]).count()
        third = db_sess.query(Answers).filter(Answers.answer == list_button_name[2]).count()
        answers_count = [first, second, third]
        color = list_button_name[answers_count.index(max(answers_count))]
        for user in users:
            user.answer = '0'
            db_sess.add(user)
            db_sess.commit()
            a = user.user_id
            await bot.send_message(user.user_id, f"На голосование участники выбрали {color} цвет.")
        MyList = towers()
        MyFile = open('listfile.txt', 'w')
        for element in MyList:
            MyFile.write(element)
            MyFile.write('\n')
        MyFile.close()


@dp.message_handler(commands=['choose_color'])
async def on_start_test(message: types.Message):
    if db_sess.query(Answers.answer).filter(Answers.user_id == message.from_user.id).first()._data[0] == '0':
        list_button_name = []
        with open('listfile.txt', 'r') as filehandle:
            for line in filehandle:
                currentPlace = line[:-1]
                list_button_name.append(currentPlace)
        buttons_list = []
        for item in list_button_name:
            l = []
            l.append(InlineKeyboardButton(text=item, callback_data=item))
            buttons_list.append(l)
        await message.answer(text="Выберите цвет из предложенных",
                             reply_markup=InlineKeyboardMarkup(inline_keyboard=buttons_list))
    else:
        await message.answer(f'Вы уже голосовали!')


@dp.callback_query_handler()
async def choose_callback(callback: types.CallbackQuery):
    if db_sess.query(Answers.answer).filter(Answers.user_id == callback.from_user.id).first()._data[0] == '0':
        user = db_sess.query(Answers).filter(Answers.user_id == callback.from_user.id).first()
        user.answer = callback.data
        db_sess.add(user)
        db_sess.commit()
        await callback.answer('Ваш голос принят.\nСпасибо за участие.')
    else:
        await callback.answer('Вы уже голосовали!')

if __name__ == '__main__':
    executor.start_polling(dp)
