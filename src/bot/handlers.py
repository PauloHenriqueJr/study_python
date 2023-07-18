from telegram.ext import CommandHandler, CallbackQueryHandler, MessageHandler, filters
from .commands import start, help_command, cancel, back
from .callbacks import button
from .messages import send_file_or_image, handle_text, unknown_command


def add_handlers_to_dispatcher(dp):
    dp.add_handler(CommandHandler("iniciar", start))
    dp.add_handler(CommandHandler("ajuda", help_command))
    dp.add_handler(CommandHandler("cancelar", cancel))
    dp.add_handler(CommandHandler("materias", back))

    dp.add_handler(CallbackQueryHandler(button))
    dp.add_handler(MessageHandler(
        filters.ALL | filters.PHOTO, send_file_or_image))
    dp.add_handler(MessageHandler(filters.TEXT, handle_text))
    dp.add_handler(MessageHandler(filters.ALL, unknown_command))
