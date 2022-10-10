import discord
import random
import string
import asyncio
from neuralintents import GenericAssistant


chatbot = GenericAssistant('intents.json')
chatbot.train_model()
chatbot.save_model()

class MyClientT(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author.id != 973662907407679488:
            return
        if message.channel.id != 977514601564479491:
            return
        async with message.channel.typing():
            timetosleep = random.randint(1,5)
            await asyncio.sleep(timetosleep)
            response = chatbot.request(message.content)
            await message.channel.send(response)

client = MyClientT()
client.run('x') # sage
