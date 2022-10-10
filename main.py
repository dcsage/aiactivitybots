import discord
import random
import string
import asyncio
from neuralintents import GenericAssistant


chatbot = GenericAssistant('intents.json')
chatbot.train_model()
chatbot.save_model()

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        channelto = client.get_channel(977514601564479491)
        await channelto.send("hi")

    async def on_message(self, message):
        if message.author.id != 997869002359578714:
            return
        if message.channel.id != 977514601564479491:
            return
        async with message.channel.typing():
            timetosleep = random.randint(1,5)
            await asyncio.sleep(timetosleep)
            response = chatbot.request(message.content)
            await message.channel.send(response)



client = MyClient()
client.run('OTczNjYyOTA3NDA3Njc5NDg4.GBor4I.Pw6QiCqKX6faEDSuLgYdRYg3lKUKHJAXSFQpaE') # lmao

