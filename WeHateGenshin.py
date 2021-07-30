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

genshin = ['genshin','dvalin','kazuha','prettycrazycatlady', 'hypostasis', 'prettycrazycatlady', 'dainsleif', 'yae', 'aether', 'lumine', 'resin', '5star roll', 'Banner', 'Genshin', 'ganyu', 'hutao', 'venti', 'bennett', 'xingqui', 'zhongli', 'albedo', 'ayaka', 'klee', 'jean', 'diluc', 'yanfei', 'eula', 'mona', 'tartaglia', 'xiao', 'diona', 'sucrose', 'keqing', 'ningguang', 'razor', 'fischl', 'barbara', 'beidou', 'chongyun', 'kaeya', 'noelle', 'rosaria', 'qiqi', 'xiangling', 'xinyan', 'lisa', 'traveller', 'anemo', 'geo', 'amber', 'GENSHIN', 'GANYU', 'HUTAO', 'VENTI', 'BENNETT', 'XINGQUI', 'ZHONGLI', 'ALBEDO', 'AYAKA', 'KLEE', 'JEAN', 'DILUC', 'YANFEI', 'EULA', 'MONA', 'TARTAGLIA', 'XIAO', 'DIONA', 'SUCROSE', 'KEQING', 'NINGGUANG', 'RAZOR', 'FISCHL', 'BARBARA', 'BEIDOU', 'CHONGYUN', 'KAEYA', 'NOELLE', 'ROSARIA', 'QIQI', 'XIANGLING', 'XINYAN', 'LISA', 'TRAVELLER', 'ANEMO', 'GEO', 'AMBER' , 'Ganyu', 'HuTao', 'Venti', 'Bennett', 'Xingqui', 'Zhongli', 'Albedo', 'Ayaka', 'Klee', 'Jean', 'Diluc', 'Yanfei', 'Eula', 'Mona', 'Tartaglia', 'Xiao', 'Diona', 'Sucrose', 'Keqing', 'Ningguang', 'Razor', 'Fischl', 'Barbara', 'Beidou', 'Chongyun', 'Kaeya', 'Noelle', 'Rosaria', 'Qiqi', 'Xiangling', 'Xinyan', 'Lisa', 'Traveller', 'Anemo', 'Geo', 'Amber', 'Ganyu', 'HuTao', 'Venti', 'Bennett', 'Xingqui', 'Zhongli', 'Albedo', 'Ayaka', 'Klee', 'Jean', 'Diluc', 'Yanfei', 'Eula', 'Mona', 'Tartaglia', 'Xiao', 'Diona', 'Sucrose', 'Keqing', 'Ningguang', 'Razor', 'Fischl', 'Barbara', 'Beidou', 'Chongyun', 'Kaeya', 'Noelle', 'Rosaria', 'Qiqi', 'Xiangling', 'Xinyan', 'Lisa', 'Traveller', 'Anemo', 'Geo', 'Amber', 'adeptusbridges', 'adeptusbridges', 'adventurerank', 'adventurerank', 'adventurerhandbook', 'adventurerhandbook', 'aerosiderite', 'aerosiderite', 'agnidusagate', 'agnidusagate', 'alchemy', 'alchemy', 'allogenes', 'amberrock', 'amberrock', 'amenomaart', 'rime', 'anemo',  'anemo', 'anemograna', 'anemograna', 'archon', 'quests', 'archon', 'quests', 'archon', 'commision', 'commissions', 'cyno', 'yaoyao', 'lyney', 'lynette', 'yunjin', 'iansan', 'dottore', 'pulcinella', 'yoimiya', 'miko', 'aloy', 'kate', 'shenhe', 'shenli', 'collei', 'signora', 'baizhu', 'daipai', 'daipai', 'daler', 'daler', 'dalong', 'dalong', 'dandan', 'dandan', 'dandy', 'dandy', 'darknight', 'hero', 'darknight', 'hero', 'davy', 'davy', 'degui', 'degui', 'domon', 'domon', 'dongdong', 'dongdong', 'dongsheng', 'dongsheng', 'donna', 'donna', 'doolan', 'doolan', 'dr.edith', 'dr.edith', 'dr.livingstone', 'dr', 'livingstone', 'dugu', 'shuo', 'dugu', 'shuo', 'durin', 'durin', 'dusky', 'ming', 'dusky', 'ming', 'dvalin', 'dvalin', 'ebina', 'gonshirou', 'ebina', 'gonshirou', 'echo', 'echo', 'edna', 'edna', 'ekaterina', 'ekaterina', 'ella', 'musk', 'ella', 'musk', 'ellin', 'ellin', 'elzer', 'elzer', 'erge', 'ernest', 'ernest', 'eroch', 'eroch', 'esther', 'esther', 'eury', 'eury', 'fan', "er'ye", 'fan', "er'ye", 'farrah', 'farrah', 'fei', 'the', 'flyer', 'fei', 'the', 'flyer', 'felix', 'felix', 'fengyan', 'fengyan', 'ferrylady', 'ferrylady', 'flagpolecheng', 'flagpolecheng', 'flash-fistling', 'flash-fistling', 'flora', 'flora', 'francis', 'francis', 'freckle', 'huang', 'freckle', 'huang', 'frederica', 'gunnhildr', 'freki', 'freki', 'fritz', "fusan'er", "fusan'er", 'fugui', 'fugui', 'fujiwara', 'toshiko', 'fujiwara', 'toshiko', 'furong', 'furong', 'furuta', 'furuta', 'furuya', 'noboru', 'furuya', 'noboru', 'futaba', 'futaba', 'gaiman', 'gaiman', 'gaofei', 'gaofei', 'gaothesixth', 'gaothesixth', 'gendou', 'ringo', 'gendou', 'ringo', "gentryde'an", "gentryde'an", 'gentrymaocai', 'gentrymaocai', 'genzou', 'genzou', 'xingqui']

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
