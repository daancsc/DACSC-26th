
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all()) # 設定 Discord bot

@bot.event
async def on_ready():
    print(f'bot on ready！')

# Say指令
@bot.command()
async def say(ctx, *msg):
    await ctx.channel.send(' '.join(msg))

# on_message事件
# !!!注意 請先移除@bot.command()，否則兩者會衝突!!!
@bot.event
async def on_message(msg):
    if msg.author == bot.user:
        return
    await msg.channel.send(msg.content)

#在colab上執行
# ================
async def main():
    await bot.start("你的token")

await main()
# ================

#在本地執行
# ================
bot.run('你的token')
# ================

#只要留一個就好