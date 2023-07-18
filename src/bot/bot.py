from config import *
from telegram.ext import Application
from .handlers import add_handlers_to_dispatcher

# Carrega o token do arquivo do arquivo de configuração


def run_bot():
    app = Application.builder().token(TOKEN).build()

    add_handlers_to_dispatcher(app)

    app.run_polling()
    app.idle()
