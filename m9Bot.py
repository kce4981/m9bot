from Utils import logger
from Utils.database import config
from discord.ext import commands
import Cogs.m9cog


class M9bot(commands.Bot):

    def __init__(self):
        super().__init__(command_prefix=config.PREFIX)
        for extension in Cogs.extensions:
            logger.m9Bot_logger.info(f'Loaded extension: {extension}')
            self.load_extension(extension)