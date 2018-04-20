import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import praw
import random

Client = discord.Client()
client = commands.Bot(command_prefix = "?")

reddit = praw.Reddit(client_id='SInQqtYzEYKiGQ',
                     client_secret='XzlfPf9-36WmiPdyGOiR0SzeYy0',
                     user_agent='RALF:com.smileys.freesmileys:v0.1')

@client.command()
async def smiley():
    memes_submissions = reddit.subreddit('freesmiley').hot()
    post_to_pick = random.randint(1, 10)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await client.say(submission.url)


@client.event
async def on_ready():
    print("hi brona is my gf")
    await client.change_status(discord.Game(name="brona's favorite game"))

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

@client.command(pass_context=True)
async def kate(ctx):
    await client.say("more like cat-eeh lole")

@client.command (pass_context=True)
async def tsukiest(ctx):
    await client.say("i swear to god TSUKIEST if i see ur fucking face anywhere i dont fucking care where it is you dead you fucking motherfucker son of a bitch PIECE OF SHIT i hope you quit cafe and take your nasty bullshit with you bithc homosexual faggot")

@client.command (pass_context=True)
async def kryparro (ctx):
    await client.say ("KRYPRRO SHUTT HE FUCK UP UR SO BAD AND UR SO UNFUNNY AND QUIT CAFE ALREADY OMG I HATE U SO MUCH AND UR SO FZCKNG RETARE I HATE U OMG UCK OF")


@client.command(pass_context=True)
async def sami (ctx):
    await client.say("Are you seriously considering even for a moment that the gutter taste of Pepsi comes even close to the nirvana that is COCA-COLA®? Only philistines prefer the soft sugar garbage that is Pepsi, why drink it when you can enjoy the more refined and sharp crisp zing of COCA-COLA®? Drinking the leading brand has clinically proven that the opposite genders desire those who can enjoy the sophisticated essence that only COCA-COLA® can inspire within you.")

@client.command(pass_context=True)
async def luke(ctx):
    await client.say("LOL WHITE BOYYYYY")
    
@client.command(pass_context=True)
async def mugi(ctx):
    await client.say("fat nigger")

@client.command(pass_context=True)
async def brona(ctx):
    await client.say("brona where are you :(")

@client.command(pass_context=True)
async def clayfingers(ctx):
    await client.say("Clay, if you don't have positive thing to say or good thing to say, SHUT YOUR BIG VAJINA MOUTH, because you're just projecting yourself as nasty as junk foods thats why you deserve to be flushed down the toilet with your POOPS")

client.run("NDAwNjk1NDYzMTIyMDQyODgw.DV4VVw.dpCVT4Vw6D4HUJa2BrIbv4H8SUE")           
