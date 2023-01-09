from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random



def towers():
    list_button_name = []
    colors = ['Крассный', 'Зелёный', 'Синий', 'Белый', 'Чёрный', 'Фиолетовый', 'Оранжевый', 'Жёлтый', 'Розовый']
    i = 1
    while i:
        random_color = colors[random.randint(0, len(colors) - 1)]
        if len(list_button_name) < 3:
            if random_color not in list_button_name:
                list_button_name.append(random_color)
        else:
            i = 0
    buttons_list = []
    for item in list_button_name:
        l = []
        l.append(InlineKeyboardButton(text=item, callback_data=item))
        buttons_list.append(l)

    return list_button_name
