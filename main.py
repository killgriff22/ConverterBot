import discord
import config
from os import listdir, mkdir, system
from PIL import Image
token = config.pymint.decode_string(config.encrypted, config.rot, config.seed)
client = discord.Client(intents=discord.Intents.all())


@client.event
async def on_ready():
    print(f"logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if not message.attachments:
        return
    for i,attachment in enumerate(message.attachments):
        if attachment.filename.split(".")[-1] in ["png", "jpg", "jpeg"]:
            pass
        elif attachment.filename.split(".")[-1] in ["webp"]:
            await attachment.save(fp=attachment.filename)
            im = Image.open(attachment.filename)
            im.save(attachment.filename.split(".")[0] + ".png")
            system("rm "+attachment.filename)
            channel = message.channel.id
            if channel in config.allowedchannels[message.guild.id]['NSFW']:
                channel = client.get_channel(config.dump_channels[message.guild.id]['NSFW'])
                await channel.send(f"{message.author.name} sent a webp in {message.channel.name} {i+1}/{len(message.attachments)}",file=discord.File(attachment.filename.split(".")[0] + ".png"))
            elif channel in config.allowedchannels[message.guild.id]['SFW']:
                channel = client.get_channel(config.dump_channels[message.guild.id]['SFW'])
                await channel.send(f"{message.author.name} sent a webp in {message.channel.name} {i+1}/{len(message.attachments)}",file=discord.File(attachment.filename.split(".")[0] + ".png"))
            system(f"rm {attachment.filename.split('.')[0]}.png")

client.run(token)
