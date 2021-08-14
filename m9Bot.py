import logging

import discord
from discord.ext.commands import Cog
from Utils import logger
from Utils.database import config
from discord.ext import commands
import Cogs.m9cog

# add intents here
intents = discord.Intents.default()
intents.members = True


class M9bot(commands.Bot):

    def __init__(self):
        self.logger = logging.getLogger('m9bot')
        super().__init__(command_prefix=config.PREFIX, intents=intents)
        for extension in Cogs.extensions:
            logger.m9Bot_logger.info(f'Loaded extension: {extension}')
            self.load_extension(extension)

        @self.check
        def no_dm(ctx):
            if isinstance(ctx.channel, discord.channel.DMChannel):
                ctx.send('走開')
                return False
            else:
                return True

    async def on_command_error(self, context, exception):
        if config.Debug:
            await super().on_command_error(context, exception)
        else:
            if self.extra_events.get('on_command_error', None):
                return

            if hasattr(context.command, 'on_error'):
                return

            cog = context.cog
            if cog and Cog._get_overridden_method(cog.cog_command_error) is not None:
                return
        await context.send(f"E: {exception}")
        self.logger.error(f'E: {exception}, cause by -> {context.message.content}, author -> {context.author}')
