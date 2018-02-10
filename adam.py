import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "?")

@client.event
async def on_ready():
    print("hi brona is my gf")


@client.command(pass_context=True)
async def bae(ctx):
    await client.say("brona")

@client.command(pass_context=True)
async def kry(ctx):
    await client.say("is a cheater!!!!")

@client.command(pass_context=True)
async def eoin(ctx):
    await client.say("epic gamer nazi")

@client.command(pass_context=True)
async def belma(ctx):
    await client.say("super op gamer!!!!!!!! XD")

@client.command(pass_context=True)
async def gf(ctx):
    await client.say("brona ofc")


@client.command(pass_context=True)
async def cheater(ctx):
    await client.say("NEVER")

@client.command(pass_context=True)
async def mintie(ctx):
    await client.say("she dumb lole")

@client.command(pass_context=True)
async def mintieswirl(ctx):
    await client.say("she dumb lole")

@client.command (pass_context=True)
async def joke(ctx):
    await client.say("I'm not loyal to brona")

@client.command (pass_context=True)
async def mylove(ctx):
    await client.say("xbrona.")

@client.command(pass_context = True)
async def say(ctx, *args):
    mesg = ' '.join(args)
    await client.delete_message(ctx.message)
    return await client.say(mesg)



client.run("NDAwNjk1NDYzMTIyMDQyODgw.DV4VVw.dpCVT4Vw6D4HUJa2BrIbv4H8SUE")                            
