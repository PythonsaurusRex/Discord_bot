import discord
from psw import gen_pass
from coin import flip_coin

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)
user_bot = 1305527429858594937

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$pass'):
        await message.channel.send(gen_pass(8))
    elif message.content.startswith('$coin'):
        await message.channel.send(flip_coin())
    else:
        await message.channel.send(message.content)

token = 'MTMwODA1NjI1ODA5NTQ4MDg3NA.G8HtM3.QmT_qhn-UXEzVvVuGB4oSIWBzJ56J87KRHq16A'
client.run(token)