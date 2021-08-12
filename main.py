from m9Bot import M9bot
from Utils.database import token

if __name__ == '__main__':
    M9bot = M9bot()
    M9bot.run(token.Discord)


