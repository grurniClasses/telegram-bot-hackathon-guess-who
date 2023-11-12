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
from DictOfPeople import people_images, lst_names, basic_url, lst_of_cheers, hint_0
from PixledPhoto import pixelate_image
import bot_settings
import io
from datetime import datetime

INIT_PIX_SIZE = 15
INIT_SCORE = 5
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
    context.user_data["lst"] = lst_names.copy()
    context.bot.send_message(chat_id=chat_id, text="please choose 'photo' if you want to play", reply_markup=reply)


message_times = {}


def game(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    text = update.message.text
    logger.info(f"= Got on chat #{chat_id}: {text!r}")
    name_from_lst = random.choice(context.user_data["lst"])
    context.user_data["name"] = name_from_lst
    context.user_data['pix_size'] = INIT_PIX_SIZE
    context.user_data['score_for_pic'] = INIT_SCORE
    hint = hint_0(context.user_data["name"])
    context.user_data["lst"].remove(name_from_lst)
    pic_to_pix = people_images[name_from_lst]
    response = pixelate_image(pic_to_pix, context.user_data['pix_size'])
    save_path = basic_url + 'pixled\\' + context.user_data["name"] + ".jpg"
    response.save(save_path)
    message_times[chat_id] = datetime.now()
    with open(save_path, 'rb') as photo:
        context.bot.send_photo(chat_id=chat_id, photo=photo)
    context.bot.send_message(chat_id=chat_id, text = hint)

def reset(update: Update, context: CallbackContext) -> int:
    # Reset the total
    context.user_data["lst"] = lst_names.copy()


def respond(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    text = update.message.text
    logger.info(f"= Got on chat #{chat_id}: {text!r}")
    current_score = context.user_data.get("total", 0)
    sent_time = message_times[chat_id]
    response_time = datetime.now().timestamp() - sent_time.timestamp()
    score_to_add = context.user_data['score_for_pic']
    path = basic_url + context.user_data["name"] + ".jpg"
    if text == context.user_data["name"]:
        response = '🥳'
        if response_time < 5:
            score_to_add += 2
        new_score = current_score + score_to_add
        context.user_data["total"] = new_score
        context.bot.send_message(chat_id=chat_id, text=response)
        time.sleep(1)
        with open(path, 'rb') as photo:
            context.bot.send_photo(chat_id=chat_id, photo=photo)
        time.sleep(1)
        context.bot.send_message(chat_id=chat_id, text=f"your score is {new_score}\n")
        game(update, context)
    else:
        context.user_data['pix_size'] += 2
        pic_after_hint = pixelate_image(path, context.user_data['pix_size'])
        save_path = basic_url + 'pixled\\' + context.user_data["name"] + ".jpg"
        pic_after_hint.save(save_path)
        while context.user_data['score_for_pic'] > 0:
            context.user_data['score_for_pic'] -= 1

        response = random.choice(lst_of_cheers)
        context.bot.send_message(chat_id=chat_id, text=response)
        time.sleep(1)
        with open(save_path, 'rb') as photo:
            context.bot.send_photo(chat_id=chat_id, photo=photo)




my_bot = Updater(token=bot_settings.BOT_TOKEN, use_context=True)
my_bot.dispatcher.add_handler(CommandHandler("start", start))
my_bot.dispatcher.add_handler(CommandHandler("photo", game))
my_bot.dispatcher.add_handler(MessageHandler(Filters.text, respond))

logger.info("* Start polling...")
my_bot.start_polling()  # Starts polling in a background thread.
my_bot.idle()  # Wait until Ctrl+C is pressed
logger.info("* Bye!")

