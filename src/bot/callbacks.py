from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from .utils import create_materias_channels_menu
from ..data.load_data import load_materias_from_json

async def button(update: Update, context: CallbackContext) -> None:
    materias = await load_materias_from_json("materias.json")
    query = update.callback_query
    query_data = query.data

    if query_data == "materias":
        keyboard = [[InlineKeyboardButton(text=materia["nome"], callback_data=str(materia_id))] for materia_id, materia in materias.items()]

        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text('Selecione uma matéria da lista abaixo:', reply_markup=reply_markup)
    elif query_data == "canais_materias":
        reply_markup = create_materias_channels_menu(materias)
        await query.edit_message_text('Selecione um canal da lista abaixo:', reply_markup=reply_markup)
    elif query_data == "ajuda":
        help_message = (
            "Este bot permite que você envie imagens e documentos para diferentes matérias. "
            "Use /iniciar para ter acesso ao menu principal. "
            "Use /materias para ver a lista de matérias disponíveis. "
            "Depois de selecionar uma matéria, você pode enviar um documento ou imagem. "
            "Se quiser mudar a matéria selecionada, use /cancelar e depois /materias. "
        )
        await query.edit_message_text(help_message)
    else:
        materia = None
        for materia_id, data in materias.items():
            if str(materia_id) == query_data:
                materia = data
                break

        if materia:
            context.chat_data['materia'] = materia
            await query.answer()
            await query.edit_message_text(f'Você selecionou {materia["nome"]}. Agora, você pode enviar um documento ou imagem para essa matéria, usar /iniciar para retornar ao menu principal, ou usar /materias para voltar à lista de matérias.')
        else:
            await query.answer("Matéria inválida. Por favor, selecione uma matéria válida.")
