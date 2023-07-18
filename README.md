# Study Python Bot

Este repositório contém os arquivos do meu projeto de estudo em Python, que é um bot criado para auxiliar nos meus estudos de Engenharia de Software e para praticar minhas habilidades em Python.

## Descrição 

O bot foi projetado para ajudar a gerenciar meus estudos. Ele usa um arquivo JSON para armazenar informações sobre diferentes matérias, incluindo o nome da matéria, o ID do canal e o link do canal. O bot é executado usando um token de bot, um nome de usuário de bot e um ID do Telegram, que são armazenados em um arquivo de configuração separado.

## Instalação

Para instalar e executar este projeto, você precisará ter Python instalado em seu sistema. Em seguida, você pode clonar este repositório e instalar as dependências necessárias usando pip:

```bash
git clone https://github.com/PauloHenriqueJr/study_python.git
cd study_python
pip install -r requirements.txt
```

## Uso 

Depois de instalar as dependências, você pode executar o bot com o seguinte comando:

```python
python run.py
```

Por favor, note que você precisará fornecer seu próprio arquivo config.py e materias.json. O config.py deve ter a seguinte estrutura:

```python
TOKEN = 'seu_token_de_bot' 
BOT_USERNAME = '@seu_nome_de_usuário_do_bot'
MY_TELEGRAM_ID = seu_id_do_telegram
```

E o materias.json deve ter a seguinte estrutura:

```json
{
  "1": {
    "nome": "nome_da_materia",
    "id_canal": "id_do_canal", 
    "link_canal": "link_do_canal"
  },
  // Adicione mais matérias conforme necessário 
}
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.