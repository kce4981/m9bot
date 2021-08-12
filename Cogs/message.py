import io
import discord
import requests
from PIL import Image, ImageColor, ImageDraw

from discord.ext import commands
from . import m9cog


def setup(bot):
    bot.add_cog(quote(bot))


class quote(m9cog.M9Cog):

    def __init__(self, bot):
        super().__init__(bot)

    @commands.command(name='quote')
    async def quote(self, ctx):
        # https://discordpy.readthedocs.io/en/stable/api.html#discord.TextChannel.fetch_message
        # ctx.send(generated_image)
        # <t:unix time:d>
        self.generate_image()
        pass

    async def quote_test(self, ctx):
        self.generate_image()
        pass

    @commands.command(name='addquote')
    async def addquote(self, ctx):
        pass

    @commands.command(name='validquote')
    async def vaildquote(self, ctx):
        # valid if the quote is real or not
        # should return valid, deleted or not existed
        # https://discordpy.readthedocs.io/en/stable/api.html#deletedreferencedmessage
        pass

    @commands.command(name='avatar')
    async def generate_image(self, ctx):
        img = Image.open(requests.get(ctx.message.mentions[0].avatar_url, stream=True).raw)
        img = img.resize((16,16), Image.ANTIALIAS)
        # https://stackoverflow.com/questions/63209888/send-pillow-image-on-discord-without-saving-the-image
        with io.BytesIO() as image_binary:
            img.save(image_binary, 'PNG')
            image_binary.seek(0)
            await ctx.send(file=discord.File(fp=image_binary, filename='image.png'))


