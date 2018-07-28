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



start_handler = CommandHandler('start',start)
dispatcher.add_handler(start_handler)
graph_handler = CommandHandler('1',graph)
dispatcher.add_handler(graph_handler)

updater.start_polling()