import telebot
from telebot import types

TOKEN = '8923441790:AAEzo7OxwVF4oUxMEwzHJG0e6_XdaXQ3xsc'
bot = telebot.TeleBot(TOKEN)

user_states = {}
user_data = {}

# --- 1. إعدادات مواد الطور المتوسط ---
MIDDLE_SUBJECTS_CONFIG = {
    "med_1_2": [
        {"key": "arabic", "name": "اللغة العربية", "coeff": 5},
        {"key": "math", "name": "الرياضيات", "coeff": 4},
        {"key": "french", "name": "اللغة الفرنسية", "coeff": 3},
        {"key": "history", "name": "التاريخ والجغرافيا", "coeff": 2},
        {"key": "science", "name": "علوم طبيعية", "coeff": 2},
        {"key": "islamic", "name": "تربية إسلامية", "coeff": 2},
        {"key": "english", "name": "لغة إنجليزية", "coeff": 2},
        {"key": "civic", "name": "تربية مدنية", "coeff": 1},
        {"key": "art", "name": "تربية تشكيلية", "coeff": 1},
        {"key": "music", "name": "تربية موسيقية", "coeff": 1},
        {"key": "sport", "name": "تربية بدنية", "coeff": 1}
    ],
    "med_3": [
        {"key": "arabic", "name": "اللغة العربية", "coeff": 5},
        {"key": "math", "name": "الرياضيات", "coeff": 4},
        {"key": "french", "name": "اللغة الفرنسية", "coeff": 3},
        {"key": "history", "name": "التاريخ والجغرافيا", "coeff": 3},
        {"key": "science", "name": "علوم طبيعية", "coeff": 2},
        {"key": "physics", "name": "علوم فيزيائية", "coeff": 2},
        {"key": "islamic", "name": "تربية إسلامية", "coeff": 2},
        {"key": "english", "name": "لغة إنجليزية", "coeff": 2},
        {"key": "civic", "name": "تربية مدنية", "coeff": 1},
        {"key": "art", "name": "تربية تشكيلية", "coeff": 1},
        {"key": "music", "name": "تربية موسيقية", "coeff": 1},
        {"key": "sport", "name": "تربية بدنية", "coeff": 1}
    ],
    "med_4": [
        {"key": "arabic", "name": "اللغة العربية", "coeff": 5},
        {"key": "math", "name": "الرياضيات", "coeff": 4},
        {"key": "french", "name": "اللغة الفرنسية", "coeff": 3},
        {"key": "history", "name": "التاريخ والجغرافيا", "coeff": 3},
        {"key": "science", "name": "علوم طبيعية", "coeff": 2},
        {"key": "physics", "name": "علوم فيزيائية", "coeff": 2},
        {"key": "islamic", "name": "تربية إسلامية", "coeff": 2},
        {"key": "english", "name": "لغة إنجليزية", "coeff": 2},
        {"key": "civic", "name": "تربية مدنية", "coeff": 1},
        {"key": "art", "name": "تربية تشكيلية", "coeff": 1},
        {"key": "music", "name": "تربية موسيقية", "coeff": 1},
        {"key": "sport", "name": "تربية بدنية", "coeff": 1}
    ]
}

# --- 2. إعدادات مواد الطور الثانوي الرسمية ودقيقة جداً ---
SECONDARY_SUBJECTS_CONFIG = {
    # السنة أولى ثانوي - جذع مشترك علوم وتكنولوجيا (ST)
    "sec_1_st": [
        {"key": "math", "name": "الرياضيات", "coeff": 5},
        {"key": "physics", "name": "العلوم الفيزيائية", "coeff": 4},
        {"key": "science", "name": "علوم الطبيعة والحياة", "coeff": 3},
        {"key": "arabic", "name": "اللغة العربية وآدابها", "coeff": 3},
        {"key": "french", "name": "اللغة الفرنسية", "coeff": 2},
        {"key": "english", "name": "اللغة الإنجليزية", "coeff": 2},
        {"key": "history", "name": "التاريخ والجغرافيا", "coeff": 2},
        {"key": "islamic", "name": "العلوم الإسلامية", "coeff": 2},
        {"key": "civic", "name": "التربية المدنية", "coeff": 1},
        {"key": "tech", "name": "التكنولوجيا (إعلام ألي / هندسة)", "coeff": 2},
        {"key": "sport", "name": "التربية البدنية", "coeff": 1}
    ],
    # السنة أولى ثانوي - جذع مشترك آداب وفلسفة (LPH)
    "sec_1_lph": [
        {"key": "arabic", "name": "اللغة العربية وآدابها", "coeff": 5},
        {"key": "history", "name": "التاريخ والجغرافيا", "coeff": 3},
        {"key": "french", "name": "اللغة الفرنسية", "coeff": 3},
        {"key": "english", "name": "اللغة الإنجليزية", "coeff": 3},
        {"key": "math", "name": "الرياضيات", "coeff": 3},
        {"key": "islamic", "name": "العلوم الإسلامية", "coeff": 2},
        {"key": "philosophy", "name": "الفلسفة", "coeff": 2},
        {"key": "science", "name": "العلوم الطبيعية", "coeff": 1},
        {"key": "physics", "name": "العلوم الفيزيائية", "coeff": 1},
        {"key": "civic", "name": "التربية المدنية", "coeff": 1},
        {"key": "sport", "name": "التربية البدنية", "coeff": 1}
    ],
    # شعبة علوم تجريبية (2 و 3 ثانوي)
    "sec_sc": [
        {"key": "science", "name": "علوم الطبيعة والحياة", "coeff": 5},
        {"key": "math", "name": "الرياضيات", "coeff": 5},
        {"key": "physics", "name": "العلوم الفيزيائية", "coeff": 5},
        {"key": "arabic", "name": "اللغة العربية وآدابها", "coeff": 3},
        {"key": "french", "name": "اللغة الفرنسية", "coeff": 2},
        {"key": "english", "name": "اللغة الإنجليزية", "coeff": 2},
        {"key": "history", "name": "التاريخ والجغرافيا", "coeff": 2},
        {"key": "philosophy", "name": "الفلسفة", "coeff": 2},
        {"key": "islamic", "name": "العلوم الإسلامية", "coeff": 2},
        {"key": "sport", "name": "التربية البدنية", "coeff": 1}
    ],
    # شعبة رياضيات (2 و 3 ثانوي)
    "sec_math": [
        {"key": "math", "name": "الرياضيات", "coeff": 7},
        {"key": "physics", "name": "العلوم الفيزيائية", "coeff": 6},
        {"key": "science", "name": "علوم الطبيعة والحياة", "coeff": 2},
        {"key": "arabic", "name": "اللغة العربية وآدابها", "coeff": 3},
        {"key": "french", "name": "اللغة الفرنسية", "coeff": 2},
        {"key": "english", "name": "اللغة الإنجليزية", "coeff": 2},
        {"key": "history", "name": "التاريخ والجغرافيا", "coeff": 2},
        {"key": "philosophy", "name": "الفلسفة", "coeff": 2},
        {"key": "islamic", "name": "العلوم الإسلامية", "coeff": 2},
        {"key": "sport", "name": "التربية البدنية", "coeff": 1}
    ],
    # شعبة تقني رياضي (2 و 3 ثانوي)
    "sec_tm": [
        {"key": "tech_spec", "name": "المادة التكنولوجية الأساسية (هندسة)", "coeff": 6},
        {"key": "math", "name": "الرياضيات", "coeff": 6},
        {"key": "physics", "name": "العلوم الفيزيائية", "coeff": 5},
        {"key": "arabic", "name": "اللغة العربية وآدابها", "coeff": 3},
        {"key": "french", "name": "اللغة الفرنسية", "coeff": 2},
        {"key": "english", "name": "اللغة الإنجليزية", "coeff": 2},
        {"key": "history", "name": "التاريخ والجغرافيا", "coeff": 2},
        {"key": "philosophy", "name": "الفلسفة", "coeff": 2},
        {"key": "islamic", "name": "العلوم الإسلامية", "coeff": 2},
        {"key": "sport", "name": "التربية البدنية", "coeff": 1}
    ],
    # شعبة تسيير واقتصاد (2 و 3 ثانوي)
    "sec_ge": [
        {"key": "accounting", "name": "التسيير المالي والمحاسبي", "coeff": 5},
        {"key": "economy", "name": "الاقتصاد والمناجمنت", "coeff": 5},
        {"key": "math", "name": "الرياضيات", "coeff": 3},
        {"key": "arabic", "name": "اللغة العربية وآدابها", "coeff": 3},
        {"key": "law", "name": "القانون", "coeff": 2},
        {"key": "history", "name": "التاريخ والجغرافيا", "coeff": 3},
        {"key": "french", "name": "اللغة الفرنسية", "coeff": 2},
        {"key": "english", "name": "اللغة الإنجليزية", "coeff": 2},
        {"key": "philosophy", "name": "الفلسفة", "coeff": 2},
        {"key": "islamic", "name": "العلوم الإسلامية", "coeff": 2},
        {"key": "sport", "name": "التربية البدنية", "coeff": 1}
    ],
    # شعبة آداب وفلسفة (2 و 3 ثانوي)
    "sec_lph": [
        {"key": "philosophy", "name": "الفلسفة", "coeff": 6},
        {"key": "arabic", "name": "اللغة العربية وآدابها", "coeff": 6},
        {"key": "history", "name": "التاريخ والجغرافيا", "coeff": 4},
        {"key": "french", "name": "اللغة الفرنسية", "coeff": 3},
        {"key": "english", "name": "اللغة الإنجليزية", "coeff": 3},
        {"key": "math", "name": "الرياضيات", "coeff": 2},
        {"key": "islamic", "name": "العلوم الإسلامية", "coeff": 2},
        {"key": "sport", "name": "التربية البدنية", "coeff": 1}
    ],
    # شعبة لغات أجنبية (2 و 3 ثانوي)
    "sec_le": [
        {"key": "lang_3", "name": "لغة أجنبية ثالثة (إسبانية/ألمانية/إيطالية)", "coeff": 5},
        {"key": "english", "name": "اللغة الإنجليزية (أو الفرنسية الأولى)", "coeff": 5},
        {"key": "french", "name": "اللغة الفرنسية (أو الإنجليزية الأولى)", "coeff": 5},
        {"key": "arabic", "name": "اللغة العربية وآدابها", "coeff": 4},
        {"key": "history", "name": "التاريخ والجغرافيا", "coeff": 3},
        {"key": "math", "name": "الرياضيات", "coeff": 2},
        {"key": "philosophy", "name": "الفلسفة", "coeff": 2},
        {"key": "islamic", "name": "العلوم الإسلامية", "coeff": 2},
        {"key": "sport", "name": "التربية البدنية", "coeff": 1}
    ]
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_states[message.chat.id] = None
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn_prim = types.KeyboardButton("🏫 الطور الابتدائي")
    btn_med = types.KeyboardButton("📘 الطور المتوسط")
    btn_sec = types.KeyboardButton("🎓 الطور الثانوي")
    markup.add(btn_prim, btn_med, btn_sec)
    
    bot.reply_to(message, "مرحباً بك في بوت حاسبة المعدلات للأطوار الثلاثة في الجزائر 🇩🇿.\nاختر الطور الدراسي للبدء:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "🔙 القائمة الرئيسية")
def back_home(message):
    send_welcome(message)

# --- قسم الطور الابتدائي ---
@bot.message_handler(func=lambda message: message.text == "🏫 الطور الابتدائي")
def primary_menu(message):
    user_states[message.chat.id] = None
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("⭐ السنة 1 و 2 ابتدائي")
    btn2 = types.KeyboardButton("⭐ السنة 3، 4 و 5 ابتدائي")
    btn_back = types.KeyboardButton("🔙 القائمة الرئيسية")
    markup.add(btn1, btn2, btn_back)
    bot.send_message(message.chat.id, "🏫 **الطور الابتدائي**\nاختر المستوى الدراسي:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "⭐ السنة 3، 4 و 5 ابتدائي")
def prim_345_start(message):
    user_states[message.chat.id] = "p_arabic"
    user_data[message.chat.id] = {}
    bot.send_message(message.chat.id, "📖 **حساب معدل السنة (3، 4، 5 ابتدائي)**\n\nأرسل نقطة مادة **اللغة العربية** (من 10، معامل 5):")

@bot.message_handler(func=lambda message: isinstance(user_states.get(message.chat.id), str) and user_states.get(message.chat.id, "").startswith("p_"))
def handle_primary_grades(message):
    try:
        val = float(message.text)
        if not (0 <= val <= 10):
            bot.send_message(message.chat.id, "الخطأ: النقطة يجب أن تكون بين 0 و 10:")
            return
        
        chat_id = message.chat.id
        state = user_states[chat_id]
        
        if state == "p_arabic":
            user_data[chat_id]['arabic'] = val
            user_states[chat_id] = "p_math"
            bot.send_message(chat_id, "أرسل نقطة مادة **الرياضيات** (من 10، معامل 4):")
        elif state == "p_math":
            user_data[chat_id]['math'] = val
            user_states[chat_id] = "p_french"
            bot.send_message(chat_id, "أرسل نقطة مادة **اللغة الفرنسية** (من 10، معامل 2):")
        elif state == "p_french":
            user_data[chat_id]['french'] = val
            user_states[chat_id] = "p_english"
            bot.send_message(chat_id, "أرسل نقطة مادة **اللغة الإنجليزية** (من 10، معامل 1):")
        elif state == "p_english":
            user_data[chat_id]['english'] = val
            user_states[chat_id] = "p_islamic"
            bot.send_message(chat_id, "أرسل نقطة مادة **التربية الإسلامية** (من 10، معامل 2):")
        elif state == "p_islamic":
            user_data[chat_id]['islamic'] = val
            user_states[chat_id] = "p_history"
            bot.send_message(chat_id, "أرسل نقطة مادة **التاريخ والجغرافيا** (من 10، معامل 1):")
        elif state == "p_history":
            user_data[chat_id]['history'] = val
            user_states[chat_id] = "p_civic"
            bot.send_message(chat_id, "أرسل نقطة مادة **التربية المدنية** (من 10، معامل 1):")
        elif state == "p_civic":
            user_data[chat_id]['civic'] = val
            user_states[chat_id] = "p_science"
            bot.send_message(chat_id, "أرسل نقطة مادة **العلوم والتكنولوجيا** (من 10، معامل 1):")
        elif state == "p_science":
            user_data[chat_id]['science'] = val
            user_states[chat_id] = "p_art"
            bot.send_message(chat_id, "أرسل نقطة مادة **التربية التشكيلية/الفنية** (من 10، معامل 1):")
        elif state == "p_art":
            user_data[chat_id]['art'] = val
            
            d = user_data[chat_id]
            total = (
                (d.get('arabic', 0) * 5) + (d.get('math', 0) * 4) +
                (d.get('french', 0) * 2) + (d.get('english', 0) * 1) +
                (d.get('islamic', 0) * 2) + (d.get('history', 0) * 1) +
                (d.get('civic', 0) * 1) + (d.get('science', 0) * 1) +
                (d.get('art', 0) * 1)
            )
            moyen = total / 18
            
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            markup.add(types.KeyboardButton("🏫 الطور الابتدائي"), types.KeyboardButton("📘 الطور المتوسط"), types.KeyboardButton("🎓 الطور الثانوي"))

            bot.send_message(chat_id, f"🎉 **نتيجة معدل السنة (3، 4، 5 ابتدائي) من 10:**\nالمعدل النهائي هو: **{moyen:.2f}** / 10", reply_markup=markup)
            user_states[chat_id] = None

    except ValueError:
        bot.send_message(message.chat.id, "الرجاء إدخال أرقام صحيحة فقط:")


# --- قسم الطور المتوسط ---
@bot.message_handler(func=lambda message: message.text == "📘 الطور المتوسط")
def متوسط_menu(message):
    user_states[message.chat.id] = None
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(
        types.KeyboardButton("📘 السنة الأولى متوسط"),
        types.KeyboardButton("📘 السنة الثانية متوسط"),
        types.KeyboardButton("📘 السنة الثالثة متوسط"),
        types.KeyboardButton("📘 السنة الرابعة متوسط"),
        types.KeyboardButton("🔙 القائمة الرئيسية")
    )
    bot.send_message(message.chat.id, "📘 **الطور المتوسط**\nاختر السنة الدراسية:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ["📘 السنة الأولى متوسط", "📘 السنة الثانية متوسط"])
def middle_y1_2(message):
    start_middle_process(message, "med_1_2", "السنة الأولى/الثانية متوسط")

@bot.message_handler(func=lambda message: message.text == "📘 السنة الثالثة متوسط")
def middle_y3(message):
    start_middle_process(message, "med_3", "السنة الثالثة متوسط")

@bot.message_handler(func=lambda message: message.text == "📘 السنة الرابعة متوسط")
def middle_y4(message):
    start_middle_process(message, "med_4", "السنة الرابعة متوسط")

def start_middle_process(message, config_key, title):
    chat_id = message.chat.id
    user_states[chat_id] = {"stage": "middle", "config_key": config_key, "index": 0, "sub_step": "fardh"}
    user_data[chat_id] = {"grades": [], "config_key": config_key}
    
    subjects = MIDDLE_SUBJECTS_CONFIG[config_key]
    sub = subjects[0]
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add(types.KeyboardButton("🔙 القائمة الرئيسية"))
    
    bot.send_message(chat_id, f"📘 **حساب معدل {title}**\n\nمادة: **{sub['name']}** (معامل {sub['coeff']})\nأرسل نقطة **الفرض** (من 20):", reply_markup=markup)

@bot.message_handler(func=lambda message: isinstance(user_states.get(message.chat.id), dict) and user_states.get(message.chat.id, {}).get("stage") == "middle")
def handle_middle_process(message):
    chat_id = message.chat.id
    state_info = user_states[chat_id]
    config_key = state_info["config_key"]
    subjects = MIDDLE_SUBJECTS_CONFIG[config_key]
    
    idx = state_info["index"]
    sub_step = state_info["sub_step"]
    sub = subjects[idx]
    
    try:
        val = float(message.text)
        if not (0 <= val <= 20):
            bot.send_message(chat_id, "الرجاء إدخال نقطة صحيحة بين 0 و 20:")
            return
        
        markup_back = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        markup_back.add(types.KeyboardButton("🔙 القائمة الرئيسية"))

        if sub_step == "fardh":
            user_data[chat_id]["temp_fardh"] = val
            state_info["sub_step"] = "taqwim"
            bot.send_message(chat_id, f"مادة **{sub['name']}**\nأرسل نقطة **التقويم المستمر** (من 20):", reply_markup=markup_back)
            
        elif sub_step == "taqwim":
            user_data[chat_id]["temp_taqwim"] = val
            state_info["sub_step"] = "ikhtibar"
            bot.send_message(chat_id, f"مادة **{sub['name']}**\nأرسل نقطة **الاختبار** (من 20):", reply_markup=markup_back)
            
        elif sub_step == "ikhtibar":
            ikhtibar = val
            fardh = user_data[chat_id]["temp_fardh"]
            taqwim = user_data[chat_id]["temp_taqwim"]
            
            moyen_madda = (((fardh + taqwim) / 2) + (ikhtibar * 2)) / 3
            
            user_data[chat_id]["grades"].append({
                "name": sub["name"],
                "moyen": moyen_madda,
                "coeff": sub["coeff"]
            })
            
            idx += 1
            state_info["index"] = idx
            
            if idx < len(subjects):
                state_info["sub_step"] = "fardh"
                next_sub = subjects[idx]
                bot.send_message(chat_id, f"✅ معدل **{sub['name']}** هو: {moyen_madda:.2f}\n\n------------------\nمادة: **{next_sub['name']}** (معامل {next_sub['coeff']})\nأرسل نقطة **الفرض** (من 20):", reply_markup=markup_back)
            else:
                total_sum = 0
                total_coeff = 0
                report = "📊 **كشف النقاط والمعدل الفصلي (متوسط):**\n\n"
                
                for item in user_data[chat_id]["grades"]:
                    report += f"- {item['name']}: معدلها **{item['moyen']:.2f}** (المعامل {item['coeff']})\n"
                    total_sum += item['moyen'] * item['coeff']
                    total_coeff += item['coeff']
                
                final_moyen = total_sum / total_coeff
                report += f"\n🎉 **المعدل النهائي للفصل:** **{final_moyen:.2f}** / 20"
                
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                markup.add(types.KeyboardButton("🏫 الطور الابتدائي"), types.KeyboardButton("📘 الطور المتوسط"), types.KeyboardButton("🎓 الطور الثانوي"))
                
                bot.send_message(chat_id, report, reply_markup=markup)
                user_states[chat_id] = None

    except ValueError:
        bot.send_message(chat_id, "الرجاء إدخال أرقام صحيحة فقط:")


# --- قسم الطور الثانوي ---
@bot.message_handler(func=lambda message: message.text == "🎓 الطور الثانوي")
def ثانوي_menu(message):
    user_states[message.chat.id] = None
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(
        types.KeyboardButton("🎓 1 ثانوي - علوم وتكنولوجيا"),
        types.KeyboardButton("🎓 1 ثانوي - آداب وفلسفة"),
        types.KeyboardButton("🎓 شعبة علوم تجريبية"),
        types.KeyboardButton("🎓 شعبة رياضيات"),
        types.KeyboardButton("🎓 شعبة تقني رياضي"),
        types.KeyboardButton("🎓 شعبة تسيير واقتصاد"),
        types.KeyboardButton("🎓 شعبة آداب وفلسفة"),
        types.KeyboardButton("🎓 شعبة لغات أجنبية"),
        types.KeyboardButton("🔙 القائمة الرئيسية")
    )
    bot.send_message(message.chat.id, "🎓 **الطور الثانوي**\nاختر السنة أو الشعبة الدراسية:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in [
    "🎓 1 ثانوي - علوم وتكنولوجيا", "🎓 1 ثانوي - آداب وفلسفة",
    "🎓 شعبة علوم تجريبية", "🎓 شعبة رياضيات", "🎓 شعبة تقني رياضي",
    "🎓 شعبة تسيير واقتصاد", "🎓 شعبة آداب وفلسفة", "🎓 شعبة لغات أجنبية"
])
def route_secondary_branch(message):
    mapping = {
        "🎓 1 ثانوي - علوم وتكنولوجيا": ("sec_1_st", "السنة الأولى ثانوي (علوم وتكنولوجيا)"),
        "🎓 1 ثانوي - آداب وفلسفة": ("sec_1_lph", "السنة الأولى ثانوي (آداب وفلسفة)"),
        "🎓 شعبة علوم تجريبية": ("sec_sc", "شعبة علوم تجريبية"),
        "🎓 شعبة رياضيات": ("sec_math", "شعبة رياضيات"),
        "🎓 شعبة تقني رياضي": ("sec_tm", "شعبة تقني رياضي"),
        "🎓 شعبة تسيير واقتصاد": ("sec_ge", "شعبة تسيير واقتصاد"),
        "🎓 شعبة آداب وفلسفة": ("sec_lph", "شعبة آداب وفلسفة"),
        "🎓 شعبة لغات أجنبية": ("sec_le", "شعبة لغات أجنبية")
    }
    key, title = mapping[message.text]
    start_secondary_process(message, key, title)

def start_secondary_process(message, config_key, title):
    chat_id = message.chat.id
    user_states[chat_id] = {"stage": "secondary", "config_key": config_key, "index": 0, "sub_step": "fardh"}
    user_data[chat_id] = {"grades": [], "config_key": config_key}
    
    subjects = SECONDARY_SUBJECTS_CONFIG[config_key]
    sub = subjects[0]
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add(types.KeyboardButton("🔙 القائمة الرئيسية"))
    
    bot.send_message(chat_id, f"🎓 **حساب معدل {title}**\n\nمادة: **{sub['name']}** (معامل {sub['coeff']})\nأرسل نقطة **الفرض (أو التقويم المستمر)** (من 20):", reply_markup=markup)

@bot.message_handler(func=lambda message: isinstance(user_states.get(message.chat.id), dict) and user_states.get(message.chat.id, {}).get("stage") == "secondary")
def handle_secondary_process(message):
    chat_id = message.chat.id
    state_info = user_states[chat_id]
    config_key = state_info["config_key"]
    subjects = SECONDARY_SUBJECTS_CONFIG[config_key]
    
    idx = state_info["index"]
    sub_step = state_info["sub_step"]
    sub = subjects[idx]
    
    try:
        val = float(message.text)
        if not (0 <= val <= 20):
            bot.send_message(chat_id, "الرجاء إدخال نقطة صحيحة بين 0 و 20:")
            return
        
        markup_back = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        markup_back.add(types.KeyboardButton("🔙 القائمة الرئيسية"))

        if sub_step == "fardh":
            user_data[chat_id]["temp_fardh"] = val
            state_info["sub_step"] = "ikhtibar"
            bot.send_message(chat_id, f"مادة **{sub['name']}**\nأرسل نقطة **الاختبار** (من 20):", reply_markup=markup_back)
            
        elif sub_step == "ikhtibar":
            ikhtibar = val
            fardh = user_data[chat_id]["temp_fardh"]
            
            # قانون حساب معدل المادة في الثانوي: (الفرض + الاختبار * 2) / 3
            moyen_madda = (fardh + (ikhtibar * 2)) / 3
            
            user_data[chat_id]["grades"].append({
                "name": sub["name"],
                "moyen": moyen_madda,
                "coeff": sub["coeff"]
            })
            
            idx += 1
            state_info["index"] = idx
            
            if idx < len(subjects):
                state_info["sub_step"] = "fardh"
                next_sub = subjects[idx]
                bot.send_message(chat_id, f"✅ معدل **{sub['name']}** هو: {moyen_madda:.2f}\n\n------------------\nمادة: **{next_sub['name']}** (معامل {next_sub['coeff']})\nأرسل نقطة **الفرض (أو التقويم)** (من 20):", reply_markup=markup_back)
            else:
                total_sum = 0
                total_coeff = 0
                report = "📊 **كشف النقاط والمعدل الفصلي (ثانوي):**\n\n"
                
                for item in user_data[chat_id]["grades"]:
                    report += f"- {item['name']}: معدلها **{item['moyen']:.2f}** (المعامل {item['coeff']})\n"
                    total_sum += item['moyen'] * item['coeff']
                    total_coeff += item['coeff']
                
                final_moyen = total_sum / total_coeff
                report += f"\n🎉 **المعدل النهائي للفصل:** **{final_moyen:.2f}** / 20"
                
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                markup.add(types.KeyboardButton("🏫 الطور الابتدائي"), types.KeyboardButton("📘 الطور المتوسط"), types.KeyboardButton("🎓 الطور الثانوي"))
                
                bot.send_message(chat_id, report, reply_markup=markup)
                user_states[chat_id] = None

    except ValueError:
        bot.send_message(chat_id, "الرجاء إدخال أرقام صحيحة فقط:")


if __name__ == '__main__':
    print("Bot is running...")
    bot.infinity_polling()
