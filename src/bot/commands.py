from telegram import Update
from telegram.ext import CallbackContext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from .utils import create_main_menu
from ..data.load_data import load_materias_from_json


async def start(update: Update, context: CallbackContext) -> None:
    user_first_name = update.message.from_user.first_name
    reply_markup = create_main_menu()
    welcome_message = f"Olá, {user_first_name}! Selecione uma opção do menu abaixo."
    await update.message.reply_text(welcome_message, reply_markup=reply_markup)


async def help_command(update: Update, context: CallbackContext) -> None:
    help_message = (
        "Este bot permite que você envie imagens e documentos para diferentes matérias. "
        "Use /iniciar para ter acesso ao menu principal. "
        "Use /materias para ver a lista de matérias disponíveis. "
        "Depois de selecionar uma matéria, você pode enviar um documento ou imagem. "
        "Se quiser mudar a matéria selecionada, use /cancelar e depois /materias. "
        "Se quiser cancelar a matéria selecionada sem escolher uma nova, use /cancelar."
    )
    await update.message.reply_text(help_message)


async def cancel(update: Update, context: CallbackContext) -> None:
    context.chat_data.pop('materia', None)
    await update.message.reply_text('A matéria selecionada foi cancelada. Você pode selecionar uma nova matéria com o comando /materias.')


async def voltar(update: Update, context: CallbackContext) -> None:
    reply_markup = create_main_menu()
    await update.message.reply_text('Selecione uma opção do menu abaixo.', reply_markup=reply_markup)


async def back(update: Update, context: CallbackContext) -> None:
    materias = await load_materias_from_json("materias.json")
    keyboard = [[InlineKeyboardButton(text=materia["nome"], callback_data=str(materia_id))] for materia_id, materia in materias.items()]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Selecione uma matéria da lista abaixo:', reply_markup=reply_markup)
