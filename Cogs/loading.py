from . import m9cog
from discord.ext import commands


def setup(bot):
    bot.add_cog(Loading(bot))


class Loading(m9cog.M9Cog):
    def __init__(self, bot):
        super().__init__(bot)

    @commands.command(name='reload')
    @commands.is_owner()
    async def reload(self, ctx, arg):
        self.logger.info(arg)
        try:
            self.bot.reload_extension(arg)
        except (commands.ExtensionNotLoaded, commands.ExtensionNotFound, commands.NoEntryPointError, commands.ExtensionFailed) as e:
            await ctx.send(f'Error: {e}')
        else:
            await ctx.send(f'{arg} load')

        pass
