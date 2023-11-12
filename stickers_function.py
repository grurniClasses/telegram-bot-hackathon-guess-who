def send_local_png_as_sticker(update, context,file_name) -> None:
    # Get the chat ID
    chat_id = update.message.chat_id
    # Upload the local PNG file to Telegram
    #file_path = path to the stickers folder
    file_path = r'C:\Users\user\Downloads\stickers'

    with open(fr"{file_path}\{file_name}", 'rb') as file:
        sticker = context.bot.send_sticker(chat_id=chat_id, sticker=file)