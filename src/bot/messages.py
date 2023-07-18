import time
import logging
from config import *
from telegram import Update
from telegram.ext import CallbackContext
from ..data.save_data import save_materias_to_json
from ..data.load_data import load_materias_from_json

# Dicionário para armazenar o último tempo de notificação para cada usuário e canal
last_notification_time = {}  # formato: {(user_id, channel_id): time}
NOTIFICATION_INTERVAL = 60 * 2  # 2 minutos

async def send_file_or_image(update: Update, context: CallbackContext) -> None:
    materia = context.chat_data.get('materia')
    if materia is None:
        await update.message.reply_text('Por favor, selecione uma matéria primeiro usando o comando /iniciar.')
    else:
        file_id = None
        if update.message.document:
            # Checa se o arquivo é um vídeo ou gif
            if update.message.document.mime_type == "video/mp4":
                await update.message.reply_text('Desculpe, vídeos e gifs não são permitidos.')
                return
            file_id = update.message.document.file_id
        elif update.message.photo:
            file_id = update.message.photo[-1].file_id
        elif update.message.video:
            await update.message.reply_text('Desculpe, vídeos e gifs não são permitidos.')
            return

        if file_id:
            file = await context.bot.get_file(file_id)
            filename = f"{materia['nome']}.jpg" 
            await file.download(filename) 
            
            # envia foto ou documento para o canal
            user = update.effective_user
            channel_id = materia['id_canal']
            if update.message.document:
                document = update.message.document
                await context.bot.send_document(channel_id, document=document.file_id, caption=f'Enviado por {user.id, user.first_name}')
                await update.message.reply_text('Arquivo enviado com sucesso!')
            elif update.message.photo:
                photo = update.message.photo[-1]
                await context.bot.send_photo(channel_id, photo=photo.file_id, caption=f'Enviado por {user.id, user.first_name}')
                await send_notification(update, context, channel_id, user, materia) # chamar a função de notificação aqui
                await update.message.reply_text('Imagem enviada com sucesso!')
        else:
            await update.message.reply_text('Por favor, envie um arquivo ou imagem.')
        
        materias = await load_materias_from_json("materias.json")
        save_materias_to_json(materias, "materias.json")


async def send_notification(update, context, channel_id, user, materia):
    current_time = time.time()
    if (user.id, channel_id) in last_notification_time:
        if current_time - last_notification_time[(user.id, channel_id)] >= NOTIFICATION_INTERVAL:
            try:
                await context.bot.send_message(MY_TELEGRAM_ID, f'Uma foto foi enviada para o canal {materia["nome"]} - {materia["link_canal"]} por {user.id, user.first_name}')
                last_notification_time[(user.id, channel_id)] = current_time
            except Exception as e:
                logging.error(f"Erro ao enviar mensagem: {e}")
    else:
        try:
            await context.bot.send_message(MY_TELEGRAM_ID, f'Uma foto foi enviada para o canal {materia["nome"]} - {materia["link_canal"]} por {user.id, user.first_name}')
            last_notification_time[(user.id, channel_id)] = current_time
        except Exception as e:
            logging.error(f"Erro ao enviar mensagem: {e}")


async def handle_text(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Por favor, envie um arquivo ou imagem.')

async def unknown_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Comando desconhecido. Por favor, use /iniciar para retornar ao menu principal.')
