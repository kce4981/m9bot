import io
import discord
import requests
from datetime import datetime, timezone
from PIL import Image, ImageColor, ImageDraw
from Utils.database import db
from discord.ext import commands
from . import m9cog


def setup(bot):
    bot.add_cog(quote(bot))


class quote(m9cog.M9Cog):

    def __init__(self, bot):
        super().__init__(bot)
        self.db = db(db_name='quote.db', sql_query='quote_db.sql')

    @commands.is_owner()
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

    def insert_db(self, msg_id: int, msg_author_id: int, quote_creator_id: int, msg_content: str,
                  quote_timestamp: datetime):
        # add local utc offset
        # https://stackoverflow.com/a/13287083/13168925
        ctx_msg_time = quote_timestamp.replace(tzinfo=timezone.utc).astimezone(tz=None)
        ins = 'INSERT INTO Quotes (Message_id, Message_author_id, Quote_creator_id, Message_content, Quote_time) VALUES(?, ?, ?, ?, ?)'
        self.db.curs.execute(ins, (msg_id, msg_author_id, quote_creator_id, msg_content, ctx_msg_time.timestamp()))
        self.db.commit()

    @commands.command(name='addquote')
    @commands.is_owner()
    async def addquote(self, ctx):

        if ctx.message.reference is None:
            await ctx.send('no reference')
        else:
            quote_msg = await ctx.fetch_message(ctx.message.reference.message_id)
            self.insert_db(quote_msg.id, quote_msg.author.id, ctx.author.id, quote_msg.content, ctx.message.created_at)
        pass

    @commands.is_owner()
    @commands.command(name='validquote')
    async def vaildquote(self, ctx):
        # i think it's impossible, maybe delete?
        pass

    @commands.is_owner()
    @commands.command(name='avatar')
    async def generate_image(self, ctx):
        img = Image.open(requests.get(ctx.message.mentions[0].avatar_url, stream=True).raw)
        img = img.resize((16, 16), Image.ANTIALIAS)
        # https://stackoverflow.com/questions/63209888/send-pillow-image-on-discord-without-saving-the-image
        with io.BytesIO() as image_binary:
            img.save(image_binary, 'PNG')
            image_binary.seek(0)
            await ctx.send(file=discord.File(fp=image_binary, filename='image.png'))
