from Utils import logger
from Utils.config import config
from discord.ext import commands
import Cogs.m9cog


class M9bot:

    def __init__(self):
        self.bot = commands.Bot(command_prefix='$')
        for extension in Cogs.extensions:
            logger.m9Bot_logger.info(f'Loaded extension: {extension}')
            self.bot.load_extension(extension)


if __name__ == '__main__':
    bot = M9bot()
    bot.bot.run(config.Token)

