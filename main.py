from discord.ext import commands
from kimetzu import Kimetzu

whitelist = [] # aqui agrega ids de usuarios para bypass

bot = commands.Bot(command_prefix='<')
bot.remove_command('help') #puedes borrar esta linea si quieres que el bot tire help

@bot.listen()
async def on_message(message):
	await Kimetzu(message, bot = bot, whitelist = whitelist, muted_role='Muted', verified_role='Verified', logs_channel=914654620977070140) #aqui acomoda los nombres de los roles

bot.run('OTE0NjQ2NzMyNTIzMDQ5MDQw.YaQFJg.HIoVBkzCSByGeyNN7NvA3-3vUM8')

