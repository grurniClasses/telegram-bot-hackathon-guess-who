# 🚧 Hyde

## The Team
- 🚧 Doron
- 🚧 Yael
- 🚧 Hadas

## About this bot

🚧 Our bot is a game of identifying famous people. Each time the bot sends a pixelated image of a celebrity and the participant guesses. If he is right, the bot will return a sticker of the famous person with a famous quote from him. If the participant made a mistake, he will receive a funny "encouragement" sentence. In addition, the bot updates the participant's score at each stage.

🚧 https://t.me/HadasDoronYaelBot

![start.png](screenshots%2Fstart.png)
![menu.png](screenshots%2Fmenu.png)
![introduction.png](screenshots%2Fintroduction.png)
![first_photo.png](screenshots%2Ffirst_photo.png)
![mistake.png](screenshots%2Fmistake.png)
![success.png](screenshots%2Fsuccess.png)
![second_photo.png](screenshots%2Fsecond_photo.png)
![end_game.png](screenshots%2Fend_game.png)


 
## Instructions for Developers 
### Prerequisites
- Python 3.11
- Poetry
- 🚧 ADD ANY OTHER PREREQUISITE HERE (MONGODB?)

### Setup
- git clone this repository 
- cd into the project directory
- Install dependencies:
    
      poetry install


- Get an API Token for a bot via the [BotFather](https://telegram.me/BotFather)
- Create a `bot_settings.py` file with your bot token:

      BOT_TOKEN = 'xxxxxxx'

### Running the bot        
- Run the bot:

      poetry run python bot.py
