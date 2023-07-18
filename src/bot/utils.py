from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def create_main_menu():
    keyboard = [
        [InlineKeyboardButton(text="Provas e Exercicios",
                              callback_data="materias")],
        [InlineKeyboardButton(text="Canais das Matérias",
                              callback_data="canais_materias")],
        [InlineKeyboardButton(text="Ajuda", callback_data="ajuda")]
    ]
    return InlineKeyboardMarkup(keyboard)


def create_materias_channels_menu(materias):
    keyboard = [
        [InlineKeyboardButton(text=materia["nome"], url=materia["link_canal"], callback_data=str(materia_id))]
        for materia_id, materia in materias.items()
    ]
    return InlineKeyboardMarkup(keyboard)


