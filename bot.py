import logging
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import (
    CommandHandler,
    CallbackContext,
    MessageHandler,
    Filters,
    Updater,
)
import time
from DictOfPeople import people_images, lst_names, basic_url
from PixledPhoto import pixelate_image
import bot_settings
import io
from datetime import datetime

logging.basicConfig(
    format="[%(levelname)s %(asctime)s %(module)s:%(lineno)d] %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)

keyboard = [["/photo"]]
reply = ReplyKeyboardMarkup(keyboard)
def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    logger.info(f"> Start chat #{chat_id}")
    reset(update, context)
    #context.bot.send_message(chat_id=chat_id, text="💣 Welcome! 💣")
    # keyboard = [["/photo"]]
    # reply = ReplyKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=chat_id, text= "please choose 'photo' if you want to play", reply_markup =reply  )

name = ''
lst = lst_names
message_times = {}
def game(update: Update, context: CallbackContext):
    global name
    chat_id = update.effective_chat.id
    text = update.message.text
    logger.info(f"= Got on chat #{chat_id}: {text!r}")
    context.user_data["lst"] = lst
    name = random.choice(context.user_data["lst"])
    context.user_data["lst"].remove(name)
    pic_to_pix = people_images[name]
    size_pix = 10
    response = pixelate_image(pic_to_pix, size_pix)
    save_path = basic_url + 'pixled\\' + name +".jpg"
    response.save(save_path)
    message_times[chat_id] = datetime.now()
    with open(save_path, 'rb') as photo:
        context.bot.send_photo(chat_id=chat_id, photo=photo)
        return name

def reset(update: Update, context: CallbackContext) -> int:
    # Reset the total
    context.user_data["lst"] = lst_names


def respond(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    text = update.message.text
    logger.info(f"= Got on chat #{chat_id}: {text!r}")
    current_score = context.user_data.get("total", 0)
    sent_time = message_times[chat_id]
    response_time = datetime.now().timestamp() - sent_time.timestamp()
    number_to_add = 2
    if text == name:
        response = '🥳'
        if response_time <5:
            number_to_add+=2
        new_score = current_score + number_to_add
        context.user_data["total"] = new_score
        context.bot.send_message(chat_id=chat_id, text = response)
        time.sleep(1)
        path = basic_url + name + ".jpg"
        with open(path, 'rb') as photo:
            context.bot.send_photo(chat_id=chat_id, photo=photo)
        time.sleep(1)
        context.bot.send_message(chat_id=chat_id, text=f"your score is {new_score}\n")
        game(update, context)
    else:
        response = 'נסה שוב'
        context.bot.send_message(chat_id=chat_id, text= response)





my_bot = Updater(token=bot_settings.BOT_TOKEN, use_context=True)
my_bot.dispatcher.add_handler(CommandHandler("start", start))
my_bot.dispatcher.add_handler(CommandHandler("photo", game))
my_bot.dispatcher.add_handler(MessageHandler(Filters.text, respond))

logger.info("* Start polling...")
my_bot.start_polling()  # Starts polling in a background thread.
my_bot.idle()  # Wait until Ctrl+C is pressed
logger.info("* Bye!")
