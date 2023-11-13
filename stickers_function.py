def send_local_png_as_sticker(update, context,file_name) -> None:
    # Get the chat ID
    chat_id = update.message.chat_id
    # Upload the local PNG file to Telegram
    #file_path = path to the stickers folder
    file_path = r'C:\Users\97252\Documents\בוטקאמפ\botP\stickers'

    with open(fr"{file_path}\{file_name}"+".png", 'rb') as file:
        context.bot.send_sticker(chat_id=chat_id, sticker=file)