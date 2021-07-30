import os
import discord
import re
import math
from discord.client import _ClientEventTask
from discord.ext import commands
import asyncio
from discord.ext import commands 
from discord.ext.commands import check, Context, has_permissions, CheckFailure

from keep_alive import keep_alive 

my_secret = os.environ['TOKEN']

client = discord.Client()





#words = "Ganyu HuTao Venti Bennett Xingqui Zhongli Albedo Ayaka Klee Jean Diluc Yanfei Eula Mona Tartaglia Xiao Diona Sucrose Keqing Ningguang Razor Fischl Barbara Beidou Chongyun Kaeya Noelle Rosaria Qiqi Xiangling Xinyan Lisa Traveller Anemo Geo Amber"  
#words_list = words.split()
#print(words_list)

genshin = ['genshin','dvalin','kazuha','prettycrazycatlady', 'hypostasis', 'prettycrazycatlady', 'dainsleif', 'yae', 'aether', 'lumine', 'resin', '5star roll', 'banner', 'genshin', 'ganyu', 'hutao', 'venti', 'bennett', 'xingqui', 'zhongli', 'albedo', 'ayaka', 'klee', 'jean', 'diluc', 'yanfei', 'eula', 'mona', 'tartaglia', 'xiao', 'diona', 'sucrose', 'keqing', 'ningguang', 'razor', 'fischl', 'beidou', 'chongyun',  'noelle', 'rosaria', 'qiqi', 'xiangling', 'xinyan', 'lisa', 'traveller', 'anemo', 'geo', 'amber', 'furong', 'noboru', 'futaba', 'gaiman', 'xingqui','primogem', 'primogems']

client = discord.Client()


ids = ['434885992172748808']


client = commands.Bot(command_prefix = '.')


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    print("Bot Status: Active")
@client.event
async def on_message(message):
      if message.author.id == 434885992172748808:
        print("User Immune")
      
      elif any(word in message.content.lower() for word in genshin):
        await message.delete()
        await message.channel.send('Do not say that!')
        await message.channel.send ('Have a problem with a blacklisted word? Request a pull here: https://github.com/Vexxo/Deletion-Bot')
      else:
        await client.process_commands(message)
  





keep_alive()

client.run(os.getenv('TOKEN'))
