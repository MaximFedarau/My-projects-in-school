import telebot #main library to create telebot
import smtplib #library to send mails
import sqlite3 #data base library
from telebot import types #main library to work with buttons
from email.mime.text import MIMEText#library to work with smtplib
from email.mime.multipart import MIMEMultipart#library to work with smtplib
import os, os.path #library to work with folders
import time#library to get the time of running program
import cowsay #cool terminal pictures library
from random import randint #library of random
#sudoku solver for user's map
def sudoku_solver(sudoku):
    zero_counter = 0
    for row in sudoku:
        zero_counter += row.count(0)
    list_of_intervals = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    while zero_counter > 0:
        for x in range(9):
            for y in range(9):
                if sudoku[x][y] == 0:
                    lst_1 = []
                    for element in sudoku[x]:
                        if element != 0 and element not in lst_1:
                            lst_1.append(element)
                    for row in sudoku:
                        element = row[y]
                        if element != 0 and element not in lst_1:
                            lst_1.append(element)
                    ind_x = -1
                    ind_y = -1
                    for i in list_of_intervals:
                        if x in i:
                            ind_x = list_of_intervals.index(i)
                        if y in i:
                            ind_y = list_of_intervals.index(i)
                    if ind_x >= 0 and ind_y >= 0:
                        for i in list_of_intervals[ind_x]:
                            for j in list_of_intervals[ind_y]:
                                if sudoku[i][j] != 0 and sudoku[i][j] not in lst_1:
                                    lst_1.append(sudoku[i][j])
                        if len(lst_1) == 8:
                            sudoku[x][y] = 45 - sum(lst_1)
                            zero_counter -= 1
                    else:
                        continue
    return sudoku
#variables
sudoku_map_num = 0
start_bot_map_time = 0
unban_id = 0
email_list = ['gmail','yahoo','yandex']
russian_email_list = ['yandex',"mail"]
name1 = ''
surname1 = ''
email1 = ''
age1 = 0
name=''
surname=''
age=0
email = ""
subject_list = ["Русский язык","Белорусский язык","Английский язык"]
class_list = [[9],[9],[9]]
num = 0
subject=""
task_num = 0
string = ''
user_id = 0
ban_id=0
#bot itself
bot = telebot.TeleBot("TOKEN",parse_mode = "HTML")
#command to start bot
@bot.message_handler(commands=['start'])
def send_welcome(message):
    global user_id
    user_id = message.from_user.id
    connect1 = sqlite3.connect("ban_user.db")
    cursor1 = connect1.cursor()
    connect1.commit()
    cursor1.execute(f'SELECT * FROM ban_id_db WHERE id = {user_id}')
    data1 = cursor1.fetchall()
    if data1==[]:
        sti = open("hi_totoro_sticker.png", 'rb')
        bot.send_sticker(message.chat.id,sti)
        bot.send_message(message.chat.id,"Greetings from me and Totoro! 😝")
        bot.send_message(message.chat.id,"Use /help to get the list of commands.")
    else:
        bot.send_message(message.chat.id, "You have been banned. Use /contacts to contact with me.")
#command to get the list of commands
@bot.message_handler(commands=['help'])
def send_welcome(message):
    global user_id
    user_id = message.from_user.id
    connect1 = sqlite3.connect("ban_user.db")
    cursor1 = connect1.cursor()
    connect1.commit()
    cursor1.execute(f'SELECT * FROM ban_id_db WHERE id = {user_id}')
    data1 = cursor1.fetchall()
    if data1==[]:
        bot.send_message(message.chat.id,"Take the list of commands: \n/hi; -- command to check your registration \n/reg;  -- command to registrate \n/start; -- command to start bot \n/help; -- command to get the list of commands \n/gdz; -- command to get completed homework \n/contacts; -- my contacts \n/sudoku; -- play different sudoku maps \n/games; -- help to activate telegram games \n/memes. -- send you some cool memes")
    else:
        bot.send_message(message.chat.id, "You have been banned. Use /contacts to contact with me.")
#first step to get answers
@bot.message_handler(commands=['gdz'])
def gdz_send(message):
    global user_id
    user_id = message.from_user.id
    connect = sqlite3.connect("users_2.db")
    cursor = connect.cursor()
    cursor.execute(f'SELECT * FROM login_id WHERE id = {user_id}')
    data = cursor.fetchall()
    connect1 = sqlite3.connect("ban_user.db")
    cursor1 = connect1.cursor()
    connect1.commit()
    cursor1.execute(f'SELECT * FROM ban_id_db WHERE id = {user_id}')
    data1 = cursor1.fetchall()
    if data1!=[]:
        bot.send_message(message.chat.id, "You have been banned. Use /contacts to contact with me.")
    elif not data==[]:
        bot.send_message(message.from_user.id,"Choose subject and class")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Русский язык 9")
        item2 = types.KeyboardButton("Белорусский язык 9")
        item3 = types.KeyboardButton("Английский язык 9")
        markup.add(item1,item2,item3)
        bot.send_message(message.chat.id,"We have: \nРусский язык -- 9 (1-28); \nБелорусский язык -- 9 (1-5); \nАнглийский язык -- 9 (1-28(+3)) 13(+3) page doesn't work. ",parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(message,choose_subject)
    else:
        bot.send_message(message.from_user.id, "First /reg (registration)!")
#second step to get answers -- choosing subject and grade
def choose_subject(message):
    global subject,num,string
    string = str(message.text)
    string_1 = string.split()
    if len(string_1)==2:
        subject = string_1[0]
        num = (string_1[1])
        if subject in subject_list and num.isdigit() and int(num) in class_list[subject_list.index(subject)]:
            bot.send_message(message.from_user.id, "Ok.")
            bot.send_message(message.from_user.id, "Choose number of exercise or page.")
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
                                     "We have: \nРусский язык -- 9 (1-28); \nБелорусский язык -- 9 (1-5); \nАнглийский язык -- 9 (1-28(+3)) 13(+3) page doesn't work. ")
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
            bot.send_message(message.from_user.id, "Choose number of exercise or page.")
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
                                     "We have: \nРусский язык -- 9 (1-28); \nБелорусский язык -- 9 (1-5); \nАнглийский язык -- 9 (1-28(+3)) 13(+3) page doesn't work.  ")
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
                                 "We have: \nРусский язык -- 9 (1-28); \nБелорусский язык -- 9 (1-5); \nАнглийский язык -- 9 (1-28(+3)) 13(+3) page doesn't work. ")
                bot.register_next_step_handler(call_5.message, choose_subject)
            if call_5.data == "no_continue_3":
                empty_valuable = 0
            bot.edit_message_text(chat_id=call_5.message.chat.id, message_id=call_5.message.message_id, text="Ok.",
                                  reply_markup=None)
#third step to get answers -- choosing the number of task
def choose_task(message):
    global task_num,string
    task_num = message.text
    length_of_folder = (len([name for name in os.listdir(string) if os.path.isfile(os.path.join(string, name))]))
    if not task_num.isdigit() or int(task_num)>length_of_folder:
        bot.send_message(message.from_user.id, "Your input is incorrect or we don't have this information. Try one more time!")
    else:
        task_num = str(int(task_num))
        task_num = "0" * (3 - len(task_num)) + task_num
        name_file = string + "/" + str(task_num) + ".png"
        task = open(name_file, 'rb')
        bot.send_photo(message.from_user.id, task)
    continue_keyboard = types.InlineKeyboardMarkup()
    continue_key_yes = types.InlineKeyboardButton(text="Yes",callback_data='yes_continue')
    continue_key_no = types.InlineKeyboardButton(text="No",callback_data='no_continue')
    continue_keyboard.add(continue_key_yes,continue_key_no)
    bot.send_message(message.chat.id,"Do you want to continue?",reply_markup=continue_keyboard)
#infinity loop of getting answers
@bot.callback_query_handler(func = lambda call_2: call_2.data in ["yes_continue","no_continue"])
def continue_callback_worker(call_2):
    if call_2.data=="yes_continue":
        bot.send_message(call_2.from_user.id, "Choose subject and class")
        bot.send_message(call_2.from_user.id,
                         "We have: \nРусский язык -- 9 (1-28); \nБелорусский язык -- 9 (1-5); \nАнглийский язык -- 9 (1-28(+3)) 13(+3) page doesn't work.  ")
        bot.register_next_step_handler(call_2.message, choose_subject)
    if call_2.data=="no_continue":
        empty_valuable = 0
    bot.edit_message_text(chat_id=call_2.message.chat.id, message_id=call_2.message.message_id, text="Ok.",
                          reply_markup=None)
#base functions
@bot.message_handler(func=lambda m: True)
def base(message):
    global user_id
    user_id = message.from_user.id
    connect = sqlite3.connect("users_2.db")
    cursor = connect.cursor()
    cursor.execute(f'SELECT * FROM login_id WHERE id = {user_id}')
    data = cursor.fetchall()
    connect1 = sqlite3.connect("ban_user.db")
    cursor1 = connect1.cursor()
    connect1.commit()
    cursor1.execute(f'SELECT * FROM ban_id_db WHERE id = {user_id}')
    data1 = cursor1.fetchall()
    if (message.text=="/hi"):#commnad to check your registration
        if data1!=[]:
            bot.send_message(message.chat.id, "You have been banned. Use /contacts to contact with me.")
        elif data==[]:
            bot.reply_to(message,"Hello. I don't know your name. /reg to make us friends! 😃")
        else:
            private_information_list = list(data[0])
            bot.reply_to(message,"Hello, "+private_information_list[2]+"!")
    elif message.text=='/reg':#registration command
        if data1!=[]:
            bot.send_message(message.chat.id, "You have been banned. Use /contacts to contact with me.")
        elif data == []:
            bot.send_message(message.chat.id,"Hi! What is your email? I need this information to tell you about techichal works, when bot may not work!😜")
            bot.register_next_step_handler(message,reg_email)
        else:
            bot.reply_to(message,'You have already registered!')
    elif user_id==1083300266 and message.text=="/ban":#ban command -- only for me and my moderators
        bot.send_message(message.chat.id,"Write an id of person, which is need to  be banned.")
        bot.register_next_step_handler(message, acception_of_ban)
    elif user_id == 1083300266 and message.text=="/unban":#unban command -- only for me and my moderators
        bot.send_message(message.chat.id,"Write an id of person, which is need to be UNbanned. ")
        bot.register_next_step_handler(message,acception_of_unban)
    elif message.text=="/contacts":#command to get my contacts
        bot.send_message(message.chat.id,"If you wanna know the reason of your ban, have some offers or you have any questions,then write on this email: fedarau@gmail.com")
    elif message.text=="/sudoku":
        if data1!=[]:
            bot.send_message(message.chat.id, "You have been banned. Use /contacts to contact with me.")
        elif data==[]:
            bot.send_message(message.chat.id,"First /reg to play sudoku.")
        else:
            bot.send_message(message.chat.id,"Let's play sudoku")
            choose_mode_sudoku_keyboard = types.InlineKeyboardMarkup()
            bot_maps_sudoku_button = types.InlineKeyboardButton(text="My map's.", callback_data="bot_maps")
            user_maps_sudoku_button = types.InlineKeyboardButton(text="Daily contest.", callback_data="user_maps")
            choose_mode_sudoku_keyboard.add(bot_maps_sudoku_button, user_maps_sudoku_button)
            bot.send_message(message.chat.id, text="Ok. Choose game mode.", reply_markup=choose_mode_sudoku_keyboard)
    elif message.text=="/games":
        if data1!=[]:
            bot.send_message(message.chat.id,"You have been banned. Use /contacts to contact with me.")
        elif data==[]:
            bot.send_message(message.chat.id,"First /reg to have the opportunity to play games.")
        else:
            bot.send_message(message.chat.id,"Start typing message @gamebot or @gamee and you will see a few games. Choose one of 'em and play.")
    elif message.text=="/memes":
        if data1 != []:
            bot.send_message(message.chat.id, "You have been banned. Use /contacts to contact with me.")
        elif data == []:
            bot.send_message(message.chat.id, "First /reg to have memes.")
        else:
            length_of_folder_1 = (len([i for i in os.listdir("memes") if os.path.isfile(os.path.join("memes", i))]))
            bot.send_message(message.chat.id, f"Ok. Send a number of meme (1-{length_of_folder_1}). or /quit if you want to exit this command.")
            bot.register_next_step_handler(message,choose_number_of_meme)
    else:#other cases
        characters = ['daemon', 'milk', 'cheese',"cow",'stimpy',"tux"]
        figure_name = (list(characters)[randint(0,len(characters)-1)])
        text_moo = cowsay.get_output_string(str(figure_name),"Your input is wrong!").split(":")[0].strip().replace("'", "").replace(",", "").replace("[",
                                                                                                                   "").replace(
        "]", "")
        bot.reply_to(message,text_moo)
def choose_number_of_meme(message):
    length_of_folder_1 = (len([i for i in os.listdir("memes") if os.path.isfile(os.path.join("memes", i))]))
    meme_number = message.text
    if meme_number == "/quit":
        bot.send_message(message.chat.id,"You exit this mode.")
    elif not meme_number.isdigit() or int(meme_number)>length_of_folder_1:
        bot.send_message(message.chat.id,"Your input is incorrect. Try one more time")
        bot.register_next_step_handler(message,choose_number_of_meme)
    else:
        meme_number=str(int(meme_number))
        meme_number = "0" * (3 - len(meme_number)) + meme_number
        meme_location = "memes/"+str(meme_number)+".mp4"
        bot.send_video(message.chat.id,open(meme_location,"rb"))
        bot.send_message(message.chat.id,f"Ok. Send a number of meme (1-{length_of_folder_1}). or /quit if you want to exit this command.")
        bot.register_next_step_handler(message, choose_number_of_meme)
#choose sudoku mode
@bot.callback_query_handler(func = lambda call_choose_mode_sudoku: call_choose_mode_sudoku.data in ["bot_maps","user_maps"])
def callback_worker_for_choose_sudoku_mode(call_choose_mode_sudoku):
    global sudoku_map_num
    if call_choose_mode_sudoku.data=="bot_maps":
        length_of_folder_1 = (len([i for i in os.listdir("Sudoku") if os.path.isfile(os.path.join("Sudoku", i))]))-1
        bot.send_message(call_choose_mode_sudoku.message.chat.id,f"Ok. Choose the map. Insert the number of map (1 - {length_of_folder_1}) or send command /back to return to the list of modes. If you want to exit the game send command /quit.")
        bot.register_next_step_handler(call_choose_mode_sudoku.message,choose_number_of_map)
    if call_choose_mode_sudoku.data=="user_maps":
        bot.send_message(call_choose_mode_sudoku.message.chat.id, "If a lot of people write on my email (/contacts) and ask me about this mode, so I'll do it with liderboard and new daily challenges!")
        bot.send_message(call_choose_mode_sudoku.message.chat.id, "Use /sudoku to play sudoku more!")
    bot.edit_message_text(chat_id=call_choose_mode_sudoku.message.chat.id, message_id=call_choose_mode_sudoku.message.message_id, text="Ok.",
                          reply_markup=None)
def choose_number_of_map(message):#choose number of my map
    global sudoku_map_num,start_bot_map_time
    sudoku_map_num = message.text
    length_of_folder = (len([i for i in os.listdir("Sudoku") if os.path.isfile(os.path.join("Sudoku", i))]))
    if sudoku_map_num=="/quit":
        bot.send_message(message.chat.id,"You exit the game.")
    elif sudoku_map_num=="/back":
        bot.send_message(message.chat.id, "Let's play sudoku")
        choose_mode_sudoku_keyboard = types.InlineKeyboardMarkup()
        bot_maps_sudoku_button = types.InlineKeyboardButton(text="My map's.", callback_data="bot_maps")
        user_maps_sudoku_button = types.InlineKeyboardButton(text="Daily contest.", callback_data="user_maps")
        choose_mode_sudoku_keyboard.add(bot_maps_sudoku_button, user_maps_sudoku_button)
        bot.send_message(message.chat.id, text="Ok. Choose game mode.", reply_markup=choose_mode_sudoku_keyboard)

        @bot.callback_query_handler(
            func=lambda call_choose_mode_sudoku: call_choose_mode_sudoku.data in ["bot_maps", "user_maps"])
        def callback_worker_for_choose_sudoku_mode(call_choose_mode_sudoku):
            global sudoku_map_num
            if call_choose_mode_sudoku.data == "bot_maps":
                length_of_folder_1 = (len([i for i in os.listdir("Sudoku") if os.path.isfile(os.path.join("Sudoku", i))]))-1
                bot.send_message(call_choose_mode_sudoku.message.chat.id,
                                 f"Ok. Choose the map. Insert the number of map (1 - {length_of_folder_1}) or send command /back to return to the list of modes. If you want to exit the game send command /quit.")
                bot.register_next_step_handler(call_choose_mode_sudoku.message, choose_number_of_map)
            if call_choose_mode_sudoku.data == "user_maps":
                bot.send_message(call_choose_mode_sudoku.message.chat.id,
                                 "If a lot of people write on my email (/contacts) and ask me about this mode, so I'll do it with leaderboard and new daily challenges! Use /sudoku to return to the game.")
                bot.send_message(call_choose_mode_sudoku.message.chat.id,"Use /sudoku to play sudoku more!")
            bot.edit_message_text(chat_id=call_choose_mode_sudoku.message.chat.id,
                                  message_id=call_choose_mode_sudoku.message.message_id, text="Ok.",
                                  reply_markup=None)
    elif not sudoku_map_num.isdigit() or int(sudoku_map_num)>length_of_folder-1:
        bot.send_message(message.from_user.id,"Your input is incorrect! Try one more time!")
        bot.register_next_step_handler(message,choose_number_of_map)
    else:
        sudoku_map_num = str(int(sudoku_map_num))
        sudoku_map_num = "0" * (3 - len(sudoku_map_num)) + sudoku_map_num
        map = open("Sudoku/" + str(sudoku_map_num) + ".png", 'rb')
        bot.send_photo(message.chat.id,map)
        bot.send_message(message.chat.id,"Timer is going. Answer write like a string (from left to right), for example: 123456789... or /quit if you want to exit he game. If you want to go back and choose the number of map send command /back")
        start_bot_map_time = time.time()
        bot.register_next_step_handler(message,input_map_answer)
def input_map_answer(message):#get answer in maps
    answer_map = message.text
    answer_matrix = []
    length_of_folder = (len([i for i in os.listdir("Sudoku") if os.path.isfile(os.path.join("Sudoku", i))]))-1
    for i in range(9):
        answer_matrix.append([0,0,0,0,0,0,0,0,0])
    if answer_map=="/quit":
        bot.send_message(message.chat.id,"You exit the game.")
    elif answer_map=="/back":
        bot.send_message(message.chat.id,f"Ok. Choose the map. Insert the number of map (1 - {length_of_folder}) or send command /back to return to the list of modes. If you want to exit the game send command /quit.")
        bot.register_next_step_handler(message,choose_number_of_map)
    elif not answer_map.isdigit() or len(answer_map)!=81:
        bot.send_message(message.chat.id,"Try one more time. Input your answer.")
        bot.register_next_step_handler(message,input_map_answer)
    else:
        index_new_list_answer_matrix = -1
        element_index_answer_matrix= 0
        for i in range(81):
            if i%9==0:
                index_new_list_answer_matrix+=1
                element_index_answer_matrix=0
            answer_matrix[index_new_list_answer_matrix][element_index_answer_matrix]=int(answer_map[i])
            element_index_answer_matrix+=1
        real_answer_sudoku_list = [ [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        if str(sudoku_map_num) == "001":
            real_answer_sudoku_list = [[5,3,0,0,7,0,0,0,0],
                                       [6,0,0,1,9,5,0,0,0],
                                       [0,9,8,0,0,0,0,6,0],
                                       [8,0,0,0,6,0,0,0,3],
                                       [4,0,0,8,0,3,0,0,1],
                                       [7,0,0,0,2,0,0,0,6],
                                       [0,6,0,0,0,0,2,8,0],
                                       [0,0,0,4,1,9,0,0,5],
                                       [0,0,0,0,8,0,0,7,9]]
        if str(sudoku_map_num) =="002":
            real_answer_sudoku_list=[ [1, 0, 0, 4, 8, 9, 0, 0, 6],
                                    [7, 3, 0, 0, 0, 0, 0, 4, 0],
                                    [0, 0, 0, 0, 0, 1, 2, 9, 5],
                                    [0, 0, 7, 1, 2, 0, 6, 0, 0],
                                    [5, 0, 0, 7, 0, 3, 0, 0, 8],
                                    [0, 0, 6, 0, 9, 5, 7, 0, 0],
                                    [9, 1, 4, 6, 0, 0, 0, 0, 0],
                                    [0, 2, 0, 0, 0, 0, 0, 3, 7],
                                    [8, 0, 0, 5, 1, 2, 0, 0, 4]]
        real_answer_sudoku_list = sudoku_solver(real_answer_sudoku_list)
        if real_answer_sudoku_list==answer_matrix:
            user_time = round(time.time() - start_bot_map_time)
            minutes_user_time = user_time//60
            seconds_user_time = user_time%60
            bot.send_message(message.chat.id,f"Congratulations! You solved this puzzle! Your time {minutes_user_time} min {seconds_user_time} sec!")
            bot.send_message(message.chat.id,"Send /sudoku if you want to play sudoku more!")
        else:
            bot.send_message(message.chat.id,"Your answer is wrong. Try one more time")
            bot.register_next_step_handler(message,input_map_answer)
#first step to ban some person
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
#second step to ban some person
@bot.callback_query_handler(func = lambda call_1: call_1.data in ["yes","no"])
def ban_callback_worker(call_1):
    connect1 = sqlite3.connect("ban_user.db")
    cursor1 = connect1.cursor()
    cursor1.execute("""CREATE TABLE IF NOT EXISTS ban_id_db(
                            id INTEGER
                        )""")
    connect1.commit()
    cursor1.execute(f'SELECT * FROM ban_id_db WHERE id = {ban_id}')
    data1 = cursor1.fetchall()
    if call_1.data=="yes":
        if data1==[]:
            cursor1.execute("INSERT INTO ban_id_db (id) VALUES (?)", [ban_id])
            connect1.commit()
            bot.answer_callback_query(callback_query_id=call_1.id, show_alert=False, text="This person is banned.")
        else:
            bot.answer_callback_query(callback_query_id=call_1.id, show_alert=False, text="This person is already banned.")
    if call_1.data=="no":
        bot.answer_callback_query(callback_query_id=call_1.id, show_alert=False, text="This person is not banned.")
    bot.edit_message_text(chat_id=call_1.message.chat.id, message_id=call_1.message.message_id, text="Ok.",
                          reply_markup=None)
#first step to unban person
def acception_of_unban(message):
    global unban_id
    unban_id = int(message.text)
    if unban_id == 1083300266:
        bot.send_message(message.chat.id,"You can't unban yourself.")
    else:
        unban_keyboard = types.InlineKeyboardMarkup()
        unban_key_yes = types.InlineKeyboardButton(text="Yes", callback_data="yes_un")
        unban_keyboard.add(unban_key_yes)
        unban_key_no = types.InlineKeyboardButton(text="No", callback_data="no_un")
        unban_keyboard.add(unban_key_no)
        bot.send_message(message.chat.id, text="Are you sure?", reply_markup=unban_keyboard)
#second step to unban person
@bot.callback_query_handler(func = lambda un_call: un_call.data in ["yes_un","no_un"])
def unban_callback_worker(un_call):
    con = sqlite3.connect("ban_user.db")
    c = con.cursor()
    con.commit()
    c.execute(f"SELECT * FROM ban_id_db WHERE id = {unban_id}")
    data_un = list(c.fetchall())
    con.commit()
    if un_call.data=="yes_un":
        if data_un!=[]:
            c.execute(f"DELETE FROM ban_id_db WHERE id = {unban_id}")
            con.commit()
            bot.answer_callback_query(callback_query_id=un_call.id, show_alert=False, text="This person is unbanned.")
        else:
            bot.answer_callback_query(callback_query_id=un_call.id,show_alert=False,text="This person is already unbanned or you don't ban this person.")
    if un_call.data=="no_un":
        bot.answer_callback_query(callback_query_id=un_call.id, show_alert=False, text="This person is not unbanned.")
    bot.edit_message_text(chat_id=un_call.message.chat.id, message_id=un_call.message.message_id, text="Ok.",
                          reply_markup=None)
#first step to registrate -- input an email
def reg_email(message):
    global email,email1
    email1 = message.text
    if email1.find("@")==-1 or email1.find(".com")==-1:
        if email1.find("@")!=-1 and email1.find(".ru")!=-1:
            if (email1[email1.find("@") + 1:email1.find(".ru")]) not in russian_email_list:
                bot.reply_to(message, "Registration is failed. 😡 Example of email: user@example(mail,yandex).ru")
                bot.send_message(message.chat.id, "Hi! What is your email?")
                bot.register_next_step_handler(message, reg_email)
            else:
                bot.send_message(message.chat.id,
                                 "Thank you for adding your email! I need this to send you messages about technical works!")
                bot.send_message(message.chat.id, "What is your name?")
                bot.register_next_step_handler(message, reg_name)
        else:
            bot.reply_to(message, "Registration is failed. 😡 Example of email: user@example(gmail,yahoo,yandex).com or user@example(mail,yandex).ru")
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
#second step to registrate -- input a name
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
#second step to registrate -- input a surname
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
#second step to registrate -- input an age
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
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ok.",
                              reply_markup=None)
        connect = sqlite3.connect("users_2.db")
        cursor = connect.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS login_id(
                    id INTEGER,
                    email TEXT,
                    name TEXT,
                    surname TEXT,
                    age INTEGER
                )""")
        connect.commit()
        cursor.execute("INSERT INTO login_id (id,email,name,surname,age) VALUES (?,?,?,?,?)",
                       (user_id, email, name, surname, age))
        connect.commit()
        msg = MIMEMultipart()#sending email with user data
        to_email = 'my_first_mail'
        message = email+" "+name+" "+surname+" "+str(age)+" "+str(user_id)
        msg.attach(MIMEText(message, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()
        server.login("my_second_mail", "password_for_my_second_name")
        server.sendmail("my_second_mail", to_email, msg.as_string())
        server.quit()
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Registration is successful")
    if call.data=="No":
        bot.send_message(call.from_user.id,"Let's try again 🧐")
        bot.send_message(call.from_user.id, "Hi! What is your email?")
        bot.register_next_step_handler(call.message, reg_email)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ok.",reply_markup=None)
bot.infinity_polling(True)#сейчас поставил bot.polling(none_stop=True), иначе выдает ошибку
