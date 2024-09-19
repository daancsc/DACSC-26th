import discord
from discord.ext import commands
import google.generativeai as genai

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all()) # 設定 Discord bot

genai.configure(api_key="你的api key") #記得放入自己的api key

generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "max_output_tokens": 2048,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.0-pro",
  generation_config=generation_config,
)


# 定義一個函式來方便呼叫api
def call_api(msg):
    chat_session = model.start_chat(
    history=[
])
    print(":" + msg)
    response = chat_session.send_message(msg)
    print(response.text)
    return response.text


@bot.event
async def on_ready():
    print(f'bot on ready！')

# on_message事件
@bot.event
async def on_message(msg):
    if msg.author == bot.user:
        return
    response = call_api(msg.content)
    await msg.channel.send(response)

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