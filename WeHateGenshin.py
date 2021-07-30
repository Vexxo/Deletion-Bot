import discord
import re
import math
from discord.client import _ClientEventTask
from discord.ext import commands
import keyboard
import asyncio
from discord.ext import commands  
client = discord.Client()





#words = "Ganyu HuTao Venti Bennett Xingqui Zhongli Albedo Ayaka Klee Jean Diluc Yanfei Eula Mona Tartaglia Xiao Diona Sucrose Keqing Ningguang Razor Fischl Barbara Beidou Chongyun Kaeya Noelle Rosaria Qiqi Xiangling Xinyan Lisa Traveller Anemo Geo Amber"  
#words_list = words.split()
#print(words_list)

genshin = ['genshin','dvalin','kazuha','prettycrazycatlady', 'hypostasis', 'prettycrazycatlady', 'dainsleif', 'yae', 'aether', 'lumine', 'resin', '5star roll', 'Banner', 'Genshin', 'ganyu', 'hutao', 'venti', 'bennett', 'xingqui', 'zhongli', 'albedo', 'ayaka', 'klee', 'jean', 'diluc', 'yanfei', 'eula', 'mona', 'tartaglia', 'xiao', 'diona', 'sucrose', 'keqing', 'ningguang', 'razor', 'fischl', 'barbara', 'beidou', 'chongyun', 'kaeya', 'noelle', 'rosaria', 'qiqi', 'xiangling', 'xinyan', 'lisa', 'traveller', 'anemo', 'geo', 'amber', 'GENSHIN', 'GANYU', 'HUTAO', 'VENTI', 'BENNETT', 'XINGQUI', 'ZHONGLI', 'ALBEDO', 'AYAKA', 'KLEE', 'JEAN', 'DILUC', 'YANFEI', 'EULA', 'MONA', 'TARTAGLIA', 'XIAO', 'DIONA', 'SUCROSE', 'KEQING', 'NINGGUANG', 'RAZOR', 'FISCHL', 'BARBARA', 'BEIDOU', 'CHONGYUN', 'KAEYA', 'NOELLE', 'ROSARIA', 'QIQI', 'XIANGLING', 'XINYAN', 'LISA', 'TRAVELLER', 'ANEMO', 'GEO', 'AMBER' , 'Ganyu', 'HuTao', 'Venti', 'Bennett', 'Xingqui', 'Zhongli', 'Albedo', 'Ayaka', 'Klee', 'Jean', 'Diluc', 'Yanfei', 'Eula', 'Mona', 'Tartaglia', 'Xiao', 'Diona', 'Sucrose', 'Keqing', 'Ningguang', 'Razor', 'Fischl', 'Barbara', 'Beidou', 'Chongyun', 'Kaeya', 'Noelle', 'Rosaria', 'Qiqi', 'Xiangling', 'Xinyan', 'Lisa', 'Traveller', 'Anemo', 'Geo', 'Amber', 'Ganyu', 'HuTao', 'Venti', 'Bennett', 'Xingqui', 'Zhongli', 'Albedo', 'Ayaka', 'Klee', 'Jean', 'Diluc', 'Yanfei', 'Eula', 'Mona', 'Tartaglia', 'Xiao', 'Diona', 'Sucrose', 'Keqing', 'Ningguang', 'Razor', 'Fischl', 'Barbara', 'Beidou', 'Chongyun', 'Kaeya', 'Noelle', 'Rosaria', 'Qiqi', 'Xiangling', 'Xinyan', 'Lisa', 'Traveller', 'Anemo', 'Geo', 'Amber']

client = discord.Client()





@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    print("Ready to ping Arch.")
@client.event
async def on_message(message):


  print(genshin)
  if message.author == client.user:
    return

  while True:
    if any(word in message.content.lower() for word in genshin):
        await message.delete()
        await message.channel.send('https://cdn.discordapp.com/attachments/749285588703903775/864098290785583104/wda.jpg')
    else:
        await client.process_commands(message)




    




client.run('ODcwMTM3MTg3ODg5NDU5Mjgx.YQIYZw.hiLWa8NxQIoSu7UOXYWtmQG22gk')
