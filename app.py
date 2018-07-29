from telegram.ext import Updater,CommandHandler
import logging

TOKEN = "699729314:AAEDVx5PJmkWtOczxNupwRqifIqDEkWCdco"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

updater = Updater(token = TOKEN)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

def start(bot,update):
	bot.send_message(chat_id=update.message.chat_id,text="TGL2018 UST10 Chat bot! Press 1 to begin!")

def graph(bot,update):
	bot.send_photo(chat_id=update.message.chat_id, photo=open('gender.png', 'rb'))

def anomaly222(bot,update):
	bot.send_photo(chat_id=update.message.chat_id, photo =open('Card222.PNG', 'rb'))

def anomaly880(bot,update):
	bot.send_photo(chat_id=update.message.chat_id, photo=open('Card880.PNG','rb'))	

def anomaly555(bot,update):
	bot.send_photo(chat_id=update.message.chat_id, photo=open('Card555.PNG','rb'))


start_handler = CommandHandler('start',start)
dispatcher.add_handler(start_handler)

graph_handler = CommandHandler('graph',graph)
dispatcher.add_handler(graph_handler)

anomaly222_handler = CommandHandler('222',anomaly222)
dispatcher.add_handler(anomaly222_handler)

anomaly880_handler = CommandHandler('880',anomaly880)
dispatcher.add_handler(anomaly880_handler)

anomaly555_handler = CommandHandler('555',anomaly555)
dispatcher.add_handler(anomaly555_handler)

updater.start_polling()