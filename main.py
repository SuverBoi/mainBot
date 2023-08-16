# -*- coding: UTF-8 -*-

import telebot
from telebot import types

bot = telebot.TeleBot("6507382240:AAFclDSWTCfqekzR_aTt8RGtMmyuiOzUpOM")


def main_reply_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # itembtn1 = types.KeyboardButton('a')
    # itembtn2 = types.KeyboardButton('v')
    # itembtn3 = types.KeyboardButton('d')
    # markup.add(itembtn1, itembtn2, itembtn3)
    markup.row(types.KeyboardButton("test_start"), types.KeyboardButton("BTN - 2"),
               types.KeyboardButton("BTN - 3"))
    markup.row(types.KeyboardButton("BTN - 4"), types.KeyboardButton("BTN - 5"))
    return markup


def story_choose_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_one = types.KeyboardButton("🔮Таємничий артефакт🔍")
    btn_two = types.KeyboardButton("Story-2")
    btn_three = types.KeyboardButton("Story-3")
    btn_four = types.KeyboardButton("Story-4")
    btn_five = types.KeyboardButton("Story-5")
    btn_six = types.KeyboardButton("Story-6")
    btn_seven = types.KeyboardButton("Story-7")
    btn_eight = types.KeyboardButton("Story-8")
    btn_nine = types.KeyboardButton("Story-9")
    btn_ten = types.KeyboardButton("👈Назад👈")

    markup.row(btn_one, btn_two, btn_three)
    markup.row(btn_four, btn_five, btn_six)
    markup.row(btn_seven, btn_eight, btn_nine)
    markup.row(btn_ten)
    return markup

def arc_story():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_one = types.KeyboardButton("Продовжити🚀")
    btn_two = types.KeyboardButton("👈Назад👈")
    markup.row(btn_one)
    markup.row(btn_two)
    return markup


def arc_story_end():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_one = types.KeyboardButton("Заново🔍")
    btn_two = types.KeyboardButton("👈Назад👈")
    markup.row(btn_one)
    markup.row(btn_two)
    return markup


def arc_story_var1():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_one = types.KeyboardButton("🌳 Пройти через глибокий ліс.")
    btn_two = types.KeyboardButton("🪨 Піднятися на гору для кращого огляду.")
    markup.row(btn_one)
    markup.row(btn_two)
    return markup


def arc_story_var2():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_one = types.KeyboardButton("👣 Досліджувати руїни.")
    btn_two = types.KeyboardButton("🚀 Вирушити назад до табору.")
    markup.row(btn_one)
    markup.row(btn_two)
    return markup


def arc_story_var3():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_one = types.KeyboardButton("👁️ Досліджувати символ на скелі.")
    btn_two = types.KeyboardButton("🚀 Вирушити назад до табору.")
    markup.row(btn_one)
    markup.row(btn_two)
    return markup


def arc_story_var4():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_one = types.KeyboardButton("🗡️ Вступити в бій зі сторожами.")
    btn_two = types.KeyboardButton("🏃‍♀️ Постаратися уникнути сторожів.")
    markup.row(btn_one)
    markup.row(btn_two)
    return markup


def arc_story_var5():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_one = types.KeyboardButton("👁️ Досліджувати артефакт детальніше.")
    btn_two = types.KeyboardButton("🏃‍♂️ Піти з підземелля.")
    markup.row(btn_one)
    markup.row(btn_two)
    return markup


def arc_story_var6():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_one = types.KeyboardButton("🏃‍♂️ Постаратися врятувати артефакт та втекти.")
    btn_two = types.KeyboardButton("🛡️ Залишити артефакт і вибратися з руїн.")
    markup.row(btn_one)
    markup.row(btn_two)
    return markup


def arc_story_var7():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_one = types.KeyboardButton("👁️ Досліджувати артефакт.")
    btn_two = types.KeyboardButton("🏃‍♂️ Швидко відійти від артефакта.")
    markup.row(btn_one)
    markup.row(btn_two)
    return markup


def arc_story_var8():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_one = types.KeyboardButton("🛡️ Вивчити голограму та обрати вказаний напрямок.")
    btn_two = types.KeyboardButton("🏃‍♂️ Постаратися вийти з підземелля.")
    markup.row(btn_one)
    markup.row(btn_two)
    return markup


def arc_story_var9():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_one = types.KeyboardButton("🚀 Вирушити назад до табору.")
    markup.row(btn_one)
    return markup


def arc_story_var_number():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_one = types.KeyboardButton("🚀493")
    btn_two = types.KeyboardButton("💔000")
    markup.row(btn_one, btn_two)
    return markup
@bot.message_handler(commands=['start', 'help'])
def send_welcome(msg):
    cid = msg.chat.id
    bot.send_message(cid, '''Привіт! Я 🌆AdventureStoryBot🌇, твій провідник у світі захоплюючих пригод і незабутніх історій. Тут ти зможеш впливати на хід подій, приймаючи важливі рішення разом з головними героями🗝️.

🛤️ Вирушай у захоплюючі подорожі, де кожне рішення може вплинути на весь хід історії🗺️. Ти обираєш свій шлях, стаючи частиною непередбачуваних пригод і захоплюючих випробувань.

Нехай твій вибір веде до великих перемог🏆, та незабутніх моментів🌠. Почни свою історію прямо зараз і давай подорожувати разом у цьому унікальному світі!🚀

Для початку, скажи "test_start", і ми відразу ж потрапимо у захоплюючу історію. Рушаймо в пригоду разом🌍!

''', reply_markup=main_reply_menu())


@bot.message_handler(func=lambda message: True)
def echo_all(msg):
    cid = msg.chat.id
    if msg.text.lower() == "test_start":
        bot.send_message(cid, "📚 Вибери історію в меню: 📑", reply_markup=story_choose_menu())
    elif msg.text == "👈Назад👈":
        bot.send_message(cid, "🤔 Зробіть вибір:🤷‍♂️", reply_markup=main_reply_menu())
    elif msg.text == "🔮Таємничий артефакт🔍":
        bot.send_message(cid, '''🔮Ви — археолог, який знаходить таємничий артефакт у віддаленому лісі.🔍

Назва історії: "Таємниця Загубленого Міста"

Герой: Джеймс Вільямсон, відомий археолог з досвідом у вивченні загадкових артефактів.

Вступ: Джеймс Вільямсон завжди мріяв дізнатися більше про загублене місто, яке легендарно вважалося скарбницею древніх знань. Він досліджував довгий час і врешті-решт виявив сліди, що вказували на те, що місто може бути реальним. Джеймс вирішив покинути усе і вирушити у відправлення на пошуки Загубленого Міста разом зі своєю командою.''',
                         reply_markup=arc_story())
    elif msg.text == "Продовжити🚀":
        bot.send_message(cid, '''Частина 1: Вибір шляху 

Джеймс та його команда опиняються перед розгалуженням у лісі. Є два шляхи, які вони можуть обрати: через глибокий ліс або піднятися на гору для кращого огляду.''',
                         reply_markup=arc_story_var1())

    elif msg.text == "🌳 Пройти через глибокий ліс.":
        bot.send_message(cid, '''Варіант 1: Глибокий ліс

Джеймс та його команда вирішують пройти через глибокий ліс. Вони потрапляють у гущавину, де їх оточують високі дерева. Ліс виявляється заплутаним, і вони заблукають. Подальший пошук артефакту ускладнюється через збірність місцевості.''',
                         reply_markup=arc_story_var2())
    elif msg.text == "🪨 Піднятися на гору для кращого огляду.":
        bot.send_message(cid, '''Варіант 2: Гора
W   
Джеймс та його команда вирішують піднятися на гору для кращого огляду. Зверху вони бачать прекрасний краєвид, але ніякого міста. Але їх увагу привертає загадковий символ на скелі. Це може бути ключем до того, де знаходиться місто.''',
                         reply_markup=arc_story_var3())
    elif msg.text == "👣 Досліджувати руїни.":
        bot.send_message(cid,
                         '''Вони розбивають табір і намагаються розібратися, як пройти крізь ліс. Нарешті, після декількох днів блукання, вони знаходять виходи з лісу. Вони потрапляють на відкрите поле, де бачать давні руїни.''',
                         reply_markup=arc_story_var4())
    elif msg.text == "👁️ Досліджувати символ на скелі.":
        bot.send_message(cid,
                         '''Вони досліджують символ на скелі і розуміють, що він вказує на підземний вхід. Вони спускаються вниз і опиняються в загадковому підземеллі. Вони виявляють артефакт, який виділяється загадковим сяйвом.''',
                         reply_markup=arc_story_var5())
    elif msg.text == "🚀 Вирушити назад до табору.":
        bot.send_message(cid,
                         '''Вони розбивають табір і повертаються до свого табору, де вирішують переглянути свої збірки та зробити нові плани. Зробіть за них вибір: ''',
                         reply_markup=arc_story_var1())
    elif msg.text == "🗡️ Вступити в бій зі сторожами.":
        bot.send_message(cid, '''Вступити в бій зі сторожами

Джеймс та його команда вирішують вступити в бій зі сторожами руїн. Бій стає жорстоким, але вони зумівають перемогти сторожів. Після бою, вони знаходять артефакт, який лежить на підігрітій плиті. Здавалося б, вони здобули перемогу, але раптово починається землетрус, і вони повинні швидко вирватися з руїн, тримаючи артефакт.''',
                         reply_markup=arc_story_var6())
    elif msg.text == "🏃‍♀️ Постаратися уникнути сторожів.":
        bot.send_message(cid,
                         '''Джеймс та його команда намагаються уникнути зіткнення зі сторожами руїн. Вони обходять сторожів і вирішують обійти руїни. Проте вони помічають загадковий артефакт на підігрітій плиті.''',
                         reply_markup=arc_story_var7())

    elif msg.text == "👁️ Досліджувати артефакт детальніше.":
        bot.send_message(cid, ''' Досліджувати артефакт детальніше

Джеймс та його команда вирішують дослідити артефакт детальніше. Вони наближаються до артефакта, і відразу відчувають загадкову енергію, яка випромінює з нього. Раптово артефакт активізується, і перед ними з'являється голограма, яка вказує на напрямок подальшого дослідження.''',
                         reply_markup=arc_story_var8())
    elif msg.text == "🏃‍♂️ Піти з підземелля.":
        bot.send_message(cid, ''' Піти з підземелля

Відчуваючи незвичну енергію артефакта, Джеймс та його команда вирішують залишити підземелля. Вони роблять кроки назад, коли раптово починається обвал, і вони швидко повертаються до виходу.''',
                         reply_markup=arc_story_var9())

    elif msg.text == "🏃‍♂️ Постаратися врятувати артефакт та втекти.":
        bot.send_message(cid, '''⚖️ Вибери 493 чи 000: ⚖️

🔄 Від цього вибору залежить життя Джеймса. 🔄''', reply_markup=arc_story_var_number())

    elif msg.text == "🚀493":
        bot.send_message(cid, '''💔 Нажаль, Джеймсу та його команді не вдалося втекти від руйнівного землетрусу. Вони робили все можливе, але сила природи була надто потужною. Артефакт залишився під завалами разом з їхнім мрійним здобутком.

Джеймс і його товариші відчувають глибоку розчарованість і сум у серцях. Вони віддавали все, щоб врятувати артефакт, але ситуація виявилася надто складною. Їхні зусилля не даремно, адже ця пригода залишить незабутній слід у їхніх серцях і стане важливим досвідом для майбутніх викликів.

🌄 Джеймс і його команда продовжують свої дослідження, відправляючись в нові подорожі та пригоди. Їхній рішучий дух не згасає, і вони готові долати будь-які труднощі, щоб розкрити таємниці минулого і внести свій внесок у скарбницю людського знання.''', reply_markup=arc_story_end())

    elif msg.text == "💔000":
        bot.send_message(cid, '''🏃‍♂️ Джеймс та його команда роблять все можливе, щоб врятувати артефакт від руїн та землетрусу. Вони вдаються до виходу, майже втративши артефакт, але вони виходять з цінним здобичем. Життя Джеймса на волоску, і від цього вирішального вибору залежить, чи вдасться їм врятувати артефакт і втекти від небезпеки.

😅 Джеймс і його команда, позбавлені подиху, здолали останні метри до виходу. Вони виходять на поверхню, відчуваючи суміш полегшення та напруженості. Вони врятували артефакт, і тепер від цього вирішального рішення залежить, чи зможуть вони повернутися до безпеки.

Роздуми та Майбутнє

🤔 Повертаючись до свого табору, Джеймс та його команда обговорюють події, які сталися. Вони розуміють, що цей артефакт може бути ключем до розкриття багатьох таємниць, і вони планують ретельніше вивчити його властивості. Від цього вибору також''', reply_markup=arc_story_end())


    elif msg.text == "Заново🔍":

        bot.send_message(cid, '''🔮Ви — археолог, який знаходить таємничий артефакт у віддаленому лісі.🔍

    
Назва історії: "Таємниця Загубленого Міста"

    
Герой: Джеймс Вільямсон, відомий археолог з досвідом у вивченні загадкових артефактів.

    
Вступ: Джеймс Вільямсон завжди мріяв дізнатися більше про загублене місто, яке легендарно вважалося скарбницею древніх знань. Він досліджував довгий час і врешті-решт виявив сліди, що вказували на те, що місто може бути реальним. Джеймс вирішив покинути усе і вирушити у відправлення на пошуки Загубленого Міста разом зі своєю командою.''',

                         reply_markup=arc_story())
bot.infinity_polling()