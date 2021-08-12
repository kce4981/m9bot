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
        self.log_usage(ctx)
        self.bot.reload_extension(f'Cogs.{arg}')
        await ctx.send(f'"{arg}" > reloaded')

    @commands.command(name='disable')
    @commands.is_owner()
    async def disable(self, ctx, arg):
        self.log_usage(ctx)
        try:
            self.bot.unload_extension(f'Cogs.{arg}')
        except BaseException as e:
            #await self.catch_error(ctx, e)
            pass
        else:
            await ctx.send(f'"{arg}" > disabled')


