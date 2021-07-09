import telebot
import smtplib
from telebot import types
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os, os.path
email_list = ['gmail','yahoo','yandex']
name1 = ''
surname1 = ''
email1 = ''
age1 = 0
name=''
surname=''
age=0
email = ""
subject_list = ["Русский язык","Белорусский язык"]
class_list = [[9],[9]]
num = 0
subject=""
task_num = 0
string = ''
user_id = 0
ban_id=0
user_id_blacklist = []#blacklist#/ban to ban someone
user_id_list = [1277476860,1083300266]
user_id_information_list = [["fedarau@gmail.com",'Mom','Mom','40'],["fedarau@gmail.com",'the Creator','Fedarau','13']]
bot = telebot.TeleBot("TOKEN",parse_mode = "HTML")
@bot.message_handler(commands=['start'])
def send_welcome(message):
    global user_id
    user_id = message.from_user.id
    if user_id not in user_id_blacklist:
        sti = open("hi_totoro_sticker.png", 'rb')
        bot.send_sticker(message.chat.id,sti)
        bot.send_message(message.chat.id,"Greetings from me and Totoro! 😝")
        bot.send_message(message.chat.id,"Use /help to get the list of commands.")
    else:
        bot.send_message(message.chat.id, "You have been banned")
@bot.message_handler(commands=['help'])
def send_welcome(message):
    global user_id
    user_id = message.from_user.id
    if user_id not in user_id_blacklist:
        bot.send_message(message.chat.id,"Take the list of commands: \n/hi; -- command to check your registration \n/reg;  -- command to registrate \n/start; -- command to start bot \n/help; -- command to get the list of commands \n/gdz. -- command to get completed homework")
    else:
        bot.send_message(message.chat.id, "You have been banned")
@bot.message_handler(commands=['gdz'])
def gdz_send(message):
    global user_id
    user_id = message.from_user.id
    if user_id in user_id_blacklist:
        bot.send_message(message.chat.id, "You have been banned")
    elif user_id in user_id_list:
        bot.send_message(message.from_user.id,"Choose subject and class")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
        item1 = types.KeyboardButton("Русский язык 9")
        item2 = types.KeyboardButton("Белорусский язык 9")
        markup.add(item1,item2)
        bot.send_message(message.chat.id,"We have: \nРусский язык -- 9 (1-10); \nБелорусский язык -- 9 (1-5). ",parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(message,choose_subject)
    else:
        bot.send_message(message.from_user.id, "First /reg (registration)!")
def choose_subject(message):
    global subject,num,string
    string = str(message.text)
    string_1 = string.split()
    if len(string_1)==2:
        subject = string_1[0]
        num = (string_1[1])
        if subject in subject_list and num.isdigit() and int(num) in class_list[subject_list.index(subject)]:
            bot.send_message(message.from_user.id, "Ok.")
            bot.send_message(message.from_user.id, "Choose number of exercise.")
            bot.register_next_step_handler(message, choose_task)
        else:
            bot.send_message(message.from_user.id, "Your input is incorrect or we don't have this infromation. Try one more time!")
            continue_keyboard_1 = types.InlineKeyboardMarkup()
            continue_key_yes_1 = types.InlineKeyboardButton(text="Yes", callback_data='yes_continue_1')
            continue_key_no_1 = types.InlineKeyboardButton(text="No", callback_data='no_continue_1')
            continue_keyboard_1.add(continue_key_yes_1, continue_key_no_1)
            bot.send_message(message.chat.id, "Do you want to continue?", reply_markup=continue_keyboard_1)
            @bot.callback_query_handler(func = lambda call_3: call_3.data in ["yes_continue_1","no_continue_1"])
            def continue_1_callback_worker(call_3):
                if call_3.data == "yes_continue_1":
                    bot.send_message(call_3.from_user.id, "Choose subject and class")
                    bot.send_message(call_3.from_user.id,
                                     "We have: \nРусский язык -- 9 (1-10); \nБелорусский язык -- 9 (1-5). ")
                    bot.register_next_step_handler(call_3.message, choose_subject)
                if call_3.data == "no_continue_1":
                    empty_valuable = 0
                bot.edit_message_text(chat_id=call_3.message.chat.id, message_id=call_3.message.message_id, text="Ok.",
                                      reply_markup=None)
    elif len(string_1)==3:
        num = (string_1[2])
        subject = string_1[0]+" "+string_1[1]
        if subject in subject_list and num.isdigit() and int(num) in class_list[subject_list.index(subject)]:
            num = int(num)
            bot.send_message(message.from_user.id, "Ok")
            bot.send_message(message.from_user.id, "Choose number of exercise.")
            bot.register_next_step_handler(message, choose_task)
        else:
            bot.send_message(message.from_user.id,
                             "Your input is incorrect or we don't have this information. Try one more time!")
            continue_keyboard_2 = types.InlineKeyboardMarkup()
            continue_key_yes_2 = types.InlineKeyboardButton(text="Yes", callback_data='yes_continue_2')
            continue_key_no_2 = types.InlineKeyboardButton(text="No", callback_data='no_continue_2')
            continue_keyboard_2.add(continue_key_yes_2, continue_key_no_2)
            bot.send_message(message.chat.id, "Do you want to continue?", reply_markup=continue_keyboard_2)
            @bot.callback_query_handler(func=lambda call_4: call_4.data in ["yes_continue_2", "no_continue_2"])
            def continue_1_callback_worker(call_4):
                if call_4.data == "yes_continue_2":
                    bot.send_message(call_4.from_user.id, "Choose subject and class")
                    bot.send_message(call_4.from_user.id,
                                     "We have: \nРусский язык -- 9 (1-10); \nБелорусский язык -- 9 (1-5). ")
                    bot.register_next_step_handler(call_4.message, choose_subject)
                if call_4.data == "no_continue_2":
                    empty_valuable = 0
                bot.edit_message_text(chat_id=call_4.message.chat.id, message_id=call_4.message.message_id, text="Ok.",
                                      reply_markup=None)
    else:
        bot.send_message(message.from_user.id,
                         "Your input is incorrect or we don't have this information. Try one more time!")
        continue_keyboard_3 = types.InlineKeyboardMarkup()
        continue_key_yes_3 = types.InlineKeyboardButton(text="Yes", callback_data='yes_continue_3')
        continue_key_no_3 = types.InlineKeyboardButton(text="No", callback_data='no_continue_3')
        continue_keyboard_3.add(continue_key_yes_3, continue_key_no_3)
        bot.send_message(message.chat.id, "Do you want to continue?", reply_markup=continue_keyboard_3)
        @bot.callback_query_handler(func=lambda call_5: call_5.data in ["yes_continue_3", "no_continue_3"])
        def continue_1_callback_worker(call_5):
            if call_5.data == "yes_continue_3":
                bot.send_message(call_5.from_user.id, "Choose subject and class")
                bot.send_message(call_5.from_user.id,
                                 "We have: \nРусский язык -- 9 (1-10); \nБелорусский язык -- 9 (1-5). ")
                bot.register_next_step_handler(call_5.message, choose_subject)
            if call_5.data == "no_continue_3":
                empty_valuable = 0
            bot.edit_message_text(chat_id=call_5.message.chat.id, message_id=call_5.message.message_id, text="Ok.",
                                  reply_markup=None)
def choose_task(message):
    global task_num,string
    task_num = message.text
    length_of_folder = (len([name for name in os.listdir(string) if os.path.isfile(os.path.join(string, name))]))
    if not task_num.isdigit() or int(task_num)>length_of_folder:
        bot.send_message(message.from_user.id, "Your input is incorrect or we don't have this information. Try one more time!")
    else:
        task_num = "0" * (3 - len(task_num)) + task_num
        name_file = string + "/" + str(task_num) + ".png"
        task = open(name_file, 'rb')
        bot.send_photo(message.from_user.id, task)
    continue_keyboard = types.InlineKeyboardMarkup()
    continue_key_yes = types.InlineKeyboardButton(text="Yes",callback_data='yes_continue')
    continue_key_no = types.InlineKeyboardButton(text="No",callback_data='no_continue')
    continue_keyboard.add(continue_key_yes,continue_key_no)
    bot.send_message(message.chat.id,"Do you want to continue?",reply_markup=continue_keyboard)
@bot.callback_query_handler(func = lambda call_2: call_2.data in ["yes_continue","no_continue"])
def continue_callback_worker(call_2):
    if call_2.data=="yes_continue":
        bot.send_message(call_2.from_user.id, "Choose subject and class")
        bot.send_message(call_2.from_user.id,
                         "We have: \nРусский язык -- 9 (1-10); \nБелорусский язык -- 9 (1-5). ")
        bot.register_next_step_handler(call_2.message, choose_subject)
    if call_2.data=="no_continue":
        empty_valuable = 0
    bot.edit_message_text(chat_id=call_2.message.chat.id, message_id=call_2.message.message_id, text="Ok.",
                          reply_markup=None)
@bot.message_handler(func=lambda m: True)
def base(message):
    global user_id
    user_id = message.from_user.id
    if (message.text=="/hi"):
        if user_id in user_id_blacklist:
            bot.send_message(message.chat.id, "You have been banned")
        elif user_id not in user_id_list:
            bot.reply_to(message,"Hello. I don't know your name. /reg to make us friends! 😃")
        else:
            bot.reply_to(message,"Hello, "+user_id_information_list[user_id_list.index(user_id)][1]+"!")
    elif message.text=='/reg':
        if user_id in user_id_blacklist:
            bot.send_message(message.chat.id, "You have been banned")
        elif user_id not in user_id_list:
            bot.send_message(message.chat.id,"Hi! What is your email? I need this information to tell you about techichal works, when bot may not work!😜")
            bot.register_next_step_handler(message,reg_email)
        else:
            bot.reply_to(message,'You have already registered!')
    elif user_id==1083300266 and message.text=="/ban":
        bot.send_message(message.chat.id,"Write an id of person, which is need to be banned.")
        bot.register_next_step_handler(message, acception_of_ban)
    else:
        bot.reply_to(message, "I don't know what should I answer 😢.")
def acception_of_ban(message):
    global ban_id
    ban_id = int(message.text)
    if ban_id==1083300266:
        bot.send_message(message.chat.id,"You can't ban yourself!")
    else:
        ban_keyboard = types.InlineKeyboardMarkup()
        ban_key_yes = types.InlineKeyboardButton(text="Yes", callback_data="yes")
        ban_keyboard.add(ban_key_yes)
        ban_key_no = types.InlineKeyboardButton(text="No", callback_data="no")
        ban_keyboard.add(ban_key_no)
        bot.send_message(message.chat.id, text="Are you sure?", reply_markup=ban_keyboard)
@bot.callback_query_handler(func = lambda call_1: call_1.data in ["yes","no"])
def ban_callback_worker(call_1):
    if call_1.data=="yes":
        if ban_id not in user_id_blacklist:
            print(ban_id,"<== banned person")
            user_id_blacklist.append(ban_id)
            bot.answer_callback_query(callback_query_id=call_1.id, show_alert=False, text="This person is banned.")
        else:
            bot.answer_callback_query(callback_query_id=call_1.id, show_alert=False, text="This person is already banned.")
    if call_1.data=="no":
        bot.answer_callback_query(callback_query_id=call_1.id, show_alert=False, text="This person is not banned.")
    bot.edit_message_text(chat_id=call_1.message.chat.id, message_id=call_1.message.message_id, text="Ok.",
                          reply_markup=None)
def reg_email(message):
    global email,email1
    email1 = message.text
    if email1.find("@")==-1 or email1.find(".com")==-1:
        bot.reply_to(message, "Registration is failed. 😡 Example of email: user@example.com")
        bot.send_message(message.chat.id, "Hi! What is your email?")
        bot.register_next_step_handler(message, reg_email)
    else:
        if (email1[email1.find("@")+1:email1.find(".com")]) not in email_list:
            bot.reply_to(message, "Registration is failed. 😡 Example of email: user@example(gmail,yahoo,yandex).com")
            bot.send_message(message.chat.id, "Hi! What is your email?")
            bot.register_next_step_handler(message, reg_email)
        else:
            bot.send_message(message.chat.id,
                             "Thank you for adding your email! I need this to send you messages about technical works!")
            bot.send_message(message.chat.id, "What is your name?")
            bot.register_next_step_handler(message, reg_name)
def reg_name(message):
    global name1
    name1 = message.text
    name1 = name1.capitalize().strip()
    if not name1.isalpha():
        bot.reply_to(message, "Registration is failed. Use letters! 😡")
        bot.send_message(message.chat.id, "Hi! What is your email?")
        bot.register_next_step_handler(message, reg_email)
    else:
        bot.send_message(message.chat.id, 'Nice to meet you '+name1+"!"+' What is your surname?')
        bot.register_next_step_handler(message, reg_surname)
def reg_surname(message):
    global surname,surname1
    surname1 = message.text
    surname1 = surname1.capitalize().strip()
    if not surname1.isalpha():
        bot.reply_to(message, "Registration is failed. Use letters! 😡")
        bot.send_message(message.chat.id, "Hi! What is your email?")
        bot.register_next_step_handler(message, reg_email)
    else:
        bot.send_message(message.chat.id,"Cool! Ok,"+surname1+" "+name1+". How old are you?")
        bot.send_message(message.chat.id,"Use only numbers or you will do all of this again 😉")
        bot.register_next_step_handler(message, reg_age)
def reg_age(message):
    global age,age1
    age1 = str(message.text)
    if not age1.isdigit():
        bot.reply_to(message,"Registration is failed. Use digits! 😡")
        bot.send_message(message.chat.id, "Hi! What is your email?")
        bot.register_next_step_handler(message, reg_email)
    else:
        question = "Is your information correct?"
        bot.send_message(message.chat.id,"Email == "+email1)
        bot.send_message(message.chat.id, "Name == "+name1)
        bot.send_message(message.chat.id, "Surname == " + surname1)
        bot.send_message(message.chat.id, "Age == " + str(age1))
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text="Yes",callback_data="Yes")
        keyboard.add(key_yes)
        key_no = types.InlineKeyboardButton(text="No", callback_data="No")
        keyboard.add(key_no)
        bot.send_message(message.chat.id, text = question,reply_markup = keyboard)
@bot.callback_query_handler(func = lambda call: call.data in ["Yes","No"])
def callback_worker(call):
    if call.data=="Yes":
        global email,age,surname,name,user_id
        email = email1
        name = name1
        surname = surname1
        age = age1
        user_id_list.append(user_id)
        user_id_information_list.append(['0','0','0','0'])
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ok.",
                              reply_markup=None)
        user_id_information_list[len(user_id_information_list)-1][0]=email
        user_id_information_list[len(user_id_information_list) - 1][1] = name
        user_id_information_list[len(user_id_information_list) - 1][2] = surname
        user_id_information_list[len(user_id_information_list) - 1][3] = str(age)
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Registration is successful")
        msg = MIMEMultipart()
        to_email = 'fe........my gmail'
        message = email+" "+name+" "+surname+" "+str(age)+" "+str(user_id)
        msg.attach(MIMEText(message, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()
        server.login("ne.......my gmail", "So......pasword for my_gmail")
        server.sendmail("ne....my gmail", to_email, msg.as_string())
        server.quit()
    if call.data=="No":
        bot.send_message(call.from_user.id,"Let's try again 🧐")
        bot.send_message(call.from_user.id, "Hi! What is your email?")
        bot.register_next_step_handler(call.message, reg_email)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ok.",reply_markup=None)
bot.infinity_polling(True)
