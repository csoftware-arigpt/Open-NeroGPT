# Open-NeroGPT
Open-NeroGPT is a Telegram bot that uses GPT-3 to generate natural language responses based on user prompts. It is written in Python and uses the openai-async and aiogram libraries. The source code is open and available on GitHub.

# Installation
To install the required dependencies, run:
```
pip install -r requirements.txt
```
You will also need to obtain an OpenAI API key from https://openai.com and a Telegram API key from @BotFather.

Then, edit the main.py file and enter your keys in the following lines:
```
openai_api = "" # Enter your OpenAI API
telegram_api = "" # Enter your Telegram API
```
# Usage
To run the bot, execute:
```
python3 main.py
```
To interact with the bot, send it a message with one of the following commands:

/nerogpt <prompt>: The bot will generate a response based on the prompt. For example, /nerogpt What is GPT-3?
/wipedialog: The bot will delete its history of previous messages.
The bot keeps a history of its conversations with each user in a text file named after the user’s ID. The files are stored in the root folder of the project.

# License
This project is licensed under the MIT License - see the LICENSE file for details.
