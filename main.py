from telegram.ext import Updater,CommandHandler,CallbackContext,MessageHandler,Filters
from telegram import Update,ReplyKeyboardMarkup
import os

# get token from env
TOKEN = os.environ['TOKEN']



def start(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id

    keyboar = ReplyKeyboardMarkup([
        ['MENU'],
        ['MANZIL','SAVATCHA']
    ])
    bot = context.bot
    bot.sendMessage(
    chat_id=chat_id,
    text='Assalom alaykum xush kelibsiz botimizga 👍',
    reply_markup=keyboar
    )

def menu(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id

    keyboar = ReplyKeyboardMarkup([
        ['Ovqatlar','Boshqalar'],
        ['Main menu']
    ])
    bot = context.bot
    bot.sendMessage(
    chat_id=chat_id,
    text='Assalom alaykum xush kelibsiz botimizga 👍',
    reply_markup=keyboar
    )
def ovqatlar(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id

    keyboar = ReplyKeyboardMarkup([
        ['Tovuq kulcha 8900 sum','Baliq kulcha 8900 sum'],
        ['Yupqa 8900 sum','Somsa 8900 sum'],
        ['Main menu']
    ])
    bot = context.bot
    bot.sendMessage(
    chat_id=chat_id,
    text='Assalom alaykum xush kelibsiz botimizga 👍',
    reply_markup=keyboar
    )
def Boshqalar(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id

    keyboar = ReplyKeyboardMarkup([
        ['sous',],
        ['ichimliklar'],
        ['salat'],
        ['Main menu']
    ])
    bot = context.bot
    bot.sendMessage(
    chat_id=chat_id,
    text='Assalom alaykum xush kelibsiz botimizga 👍',
    reply_markup=keyboar
    )
def sous(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id

    keyboar = ReplyKeyboardMarkup([
        ['tar-tar 8900 sum','qaymoq 8900 sum','chili 8900 sum'],
        ['Main menu']
        
    ])
    bot = context.bot
    bot.sendMessage(
    chat_id=chat_id,
    text='Assalom alaykum xush kelibsiz botimizga 👍',
    reply_markup=keyboar
    )
def ichimliklar(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id

    keyboar = ReplyKeyboardMarkup([
        ['kofi 8900 sum','pepsi 8900 sum'],
        ['choy 8900 sum','coca-cola 8900 sum'],
        ['Main menu']
       
    ])
    bot = context.bot
    bot.sendMessage(
    chat_id=chat_id,
    text='Assalom alaykum xush kelibsiz botimizga 👍',
    reply_markup=keyboar
    )
def salat(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id

    keyboar = ReplyKeyboardMarkup([
        ['suzma 8900 sum'],
        ['shakarob 8900 sum','tuzlama 8900 sum'],
        ['Main menu']
       
    ])
    bot = context.bot
    bot.sendMessage(
    chat_id=chat_id,
    text='Assalom alaykum xush kelibsiz botimizga 👍',
    reply_markup=keyboar
    )

updater = Updater(token=TOKEN)

updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(MessageHandler(Filters.text('MENU'),menu))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Main menu'),start))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Ovqatlar'),ovqatlar))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Boshqalar'),Boshqalar))
updater.dispatcher.add_handler(MessageHandler(Filters.text('sous'),sous))
updater.dispatcher.add_handler(MessageHandler(Filters.text('ichimliklar'),ichimliklar))
updater.dispatcher.add_handler(MessageHandler(Filters.text('salat'),salat))

updater.start_polling()
updater.idle()