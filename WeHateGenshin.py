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

genshin = ['genshin','dvalin','kazuha','prettycrazycatlady', 'hypostasis', 'prettycrazycatlady', 'dainsleif', 'yae', 'aether', 'lumine', 'resin', '5star roll', 'banner', 'genshin', 'ganyu', 'hutao', 'venti', 'bennett', 'xingqui', 'zhongli', 'albedo', 'ayaka', 'klee', 'jean', 'diluc', 'yanfei', 'eula', 'mona', 'tartaglia', 'xiao', 'diona', 'sucrose', 'keqing', 'ningguang', 'razor', 'fischl', 'barbara', 'beidou', 'chongyun', 'kaeya', 'noelle', 'rosaria', 'qiqi', 'xiangling', 'xinyan', 'lisa', 'traveller', 'anemo', 'geo', 'amber', 'adeptusbridges', 'adventurerank', 'adventurerhandbook', 'aerosiderite', 'agnidusagate', 'alchemy', 'allogenes', 'amberrock', 'amenomaart', 'rime', 'anemograna', 'archon', 'quests', 'commision', 'commissions', 'cyno', 'yaoyao', 'lyney', 'lynette', 'yunjin', 'iansan', 'dottore', 'pulcinella', 'yoimiya', 'miko', 'aloy', 'kate', 'shenhe', 'shenli', 'collei', 'signora', 'baizhu', 'daipai', 'daler', 'dalong', 'dandan', 'dandy', 'darknight', 'hero', 'davy', 'degui', 'domon', 'dongdong', 'dongsheng', 'donna', 'doolan', 'dr.edith', 'dr.livingstone', 'dr', 'livingstone', 'dugu', 'shuo', 'durin', 'dusky', 'ming', 'dvalin', 'ebina', 'gonshirou', 'echo', 'edna', 'ekaterina', 'ella', 'musk', 'ellin', 'elzer', 'erge', 'eroch', 'esther', 'eury', 'fan', 'farrah', 'fei', 'the', 'flyer', 'felix', 'fengyan', 'ferrylady', 'flagpolecheng', 'flash-fistling', 'flora', 'francis', 'freckle', 'huang', 'frederica', 'gunnhildr', 'freki', 'fritz', 'fugui', 'fujiwara', 'toshiko', 'furong', 'furuta', 'furuya', 'noboru', 'futaba', 'gaiman', 'gaofei', 'gaothesixth', 'gendou', 'ringo', 'gentryde', 'gentrymaocai', 'genzou', 'xingqui']
client = discord.Client()





@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    print("Ready to delete genshin impact words.")
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




    




client.run('token')
