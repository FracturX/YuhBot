import discord
from discord.ext import commands

import subprocess

import shutil
import youtube_dl
import os


from pathlib import Path

import asyncio

import opus_api
import ffmpeg

import random

queuelist = []


carmelSongs = {
    "Survival": "https://youtu.be/s0_8THQ9LI4",
    "Maxima": "https://youtu.be/KaidiP1giQ8",
    "Man Up": "https://youtu.be/_zgHuXGBKNQ",
    "Parachute": "https://youtu.be/uD4rHiT7uCg",
    "Cowboy Bebop": "https://youtu.be/E_IsrpGBrMA",
    "Backpack": "https://youtu.be/F7c7BhSN_tw",
    "Heart": "https://youtu.be/b7nz2_6-bzY",
    "Roundabouts": "https://youtu.be/Iw5MnS2fcrc",
    "Conditioned": "https://youtu.be/zXXGK2tX0qE",
    "Perspectives": "https://youtu.be/j5ZJNrNRdac",
    "Sunshine:": "https://youtu.be/x6ty1m3NEvk",
    "Peace:": "https://youtu.be/tEYCfadMOso",
    "Fight or Flight": "https://youtu.be/fPOG5zcVym0",
    "Skydream": "https://youtu.be/zs2RmEB9YKg",
    "Free Bird": "https://youtu.be/IpxSYJgC_zA",
    "Carmel": "https://youtu.be/yh7IGrqVSSE",
    "Dead To Me": "https://youtu.be/ztzvlpPY1_w",
    "Committed": "https://youtu.be/rWbi9ulSUmE",
    "Raptor": "https://youtu.be/wRtzZ4hwKAY",
    "Picture Me": "https://youtu.be/5hqxJoZIcVs",
    "A+": "https://youtu.be/QHg5ncpwdho",
    "Out Now": "https://youtu.be/y8JSojvhXs4",
    "A Little Bit": "https://youtu.be/DVR7QBw4gLY",
    "Fake Friends": "https://youtu.be/w6SC5VBSHrI",
    "Nothing New": "https://youtu.be/AjT_9tx7hYA",
    "You and I": "https://youtu.be/o-OmTNl7pYs",
    "Oh Well": "https://youtu.be/8Dgx5OlDhrQ",
    "Flight Risk": "https://youtu.be/E2g7R4XBzms",

}

client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("bot is ready")

cache = []
players = {}
queues = {}

# list of possible quotes

quotes = [
    "Make it your mission to bring positivity into fruition.",
    "Whip up that love that you cook in the kitchen",
    "YUH",
    "Salty Liberal",
    "I wrote it down I told my mama that I loved her, I told everyone my sister and my brother, that this was not a game, this was everything to me, this was everything that i see, and everything I wanna be so now I'm spitting out a track, tryna take everything and I wanna take that shit back and that's real.",
    "You know the vibe, A+ A+, yuhh.",
    "So there's a buddhist in the neighborhood still practicing his customs",
    "Just across the way some Christans Just across the way some Muslims",
    "AND THAT'S JUST PEACE",
    "AND WE ALL GET ALONG",
    "STREAMING COMETS, TAILWINDS OF OUR DREAMS PROPELLING ROCKETS,",
    "A CULTURE OF LATE NIGHT HALFWAY AWAITS CHASING A FLEETING FEELING WE ARE THE NIGHT",
    "let's switch the condition",
    "All of my students are so satisfactory, we stay working til we get that mastery yuh.",
    "sometimes u gotta pop off and let em know oh all ah yah ded to meh",
    "GOTTA RUN SOME HEAT BACK WHEN I WANNA TALK THIS WAY. ALL I GOTTA DO IS GET EM FOCUSED. IN THE MIDST OF THE GAME YOU A LOCUST.",
    "But my childish heart and soulful intentiosn were divided by a systemt that had explicit definition of what, made a man a man a woman a woman",
    "Inside my soul was love for every single person that I new",
    "The focus has shifted turned technologically it bothers me that people are so obsessed with they property, as if the fragility of this masculinity had us acting like we was enemies, instead of god's centerpiece.",
    "Man that's what the advertisements sold us ain't not to take the time with paintings rather take the time with payments huh.",
    "I'm feeling like a charizard, I'm so evolved. I don't need that simplicity, rather dig in and get it. See the money I'm spending, I'm hot. Hotter than the lava coming from Mount Fuji."
    ]

#sending the quote





@client.command()
async def quote(ctx):
    await ctx.send(random.choice(quotes))




@client.command()
async def lol(ctx):
    dude = ctx.message.content.split(" ", 1)
    lament = dude[1]
    if lament in carmelSongs:
        await ctx.send(carmelSongs[lament])




@client.command()
async def join(ctx, *, channel: discord.VoiceChannel):
    

    if ctx.voice_client is not None:
        return await ctx.voice_client.move_to(channel)

    await channel.connect()

async def currentMusic(ctx):
    await ctx.send(f"Now playing: {cache[-1]}")




@client.command()
async def play(ctx, *, query):

    async def check_queue():
        Queue_infile = os.path.isdir("./Queue")
        if Queue_infile is True:
            DIR = os.path.abspath(os.path.realpath("Queue"))
            length = len(os.listdir(DIR))
            still_q = length - 1
            listdirs = os.listdir(DIR)
            sorted_DIR = sorted(listdirs)
            try:
                first_file = sorted_DIR[0]
            except:
                print("No more queued song(s)\n")
                queues.clear()
                queuelist.clear()
                return
            main_location = os.path.dirname(os.path.realpath(__file__))
            song_path = os.path.abspath(os.path.realpath("Queue") + "/" + first_file)
            if length != 0:
                print("Song done, playing next queued\n")
                print(f"Songs still in queue: {still_q}")
                song_there = os.path.isfile("song.mp3")
                if song_there:
                    os.remove("song.mp3")
                shutil.move(song_path, main_location)
                thedir = os.getcwd()
                for file in os.listdir(thedir):
                    if file.endswith(".mp3"):
                        os.rename(file, 'song.mp3')


                voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: check_queue())
                voice.source = discord.PCMVolumeTransformer(voice.source)
                voice.source.volume = 0.40
                poopy = queuelist.pop(0)
                cache.append(poopy)
                await ctx.send(f"Now Playing: {cache[-1]}.")
                
                
    

            else:
                queues.clear()
                queuelist.clear()
                cache.clear()
                return

        else:
            queues.clear()
            queuelist.clear()
            cache.clear()
            print("No songs were queued before the ending of the last song\n")





    if ctx.voice_client is not None:
        if query in carmelSongs:
            await ctx.send("Please be patient while I download " + query + ".")

            song_there = os.path.isfile("song.mp3")
            try:
                if song_there:
                    os.remove("song.mp3")
                    queues.clear()
                    print("Removed old song file")
            except PermissionError:
                print("Trying to delete song file, but it's being played")
                await ctx.send("ERROR: Music Playing. Please use !queue to queue another Cal Combs song.")
                return


            Queue_infile = os.path.isdir("./Queue")
            try:
                Queue_folder = "./Queue"
                if Queue_infile is True:
                    print("Removed old Queue Folder")
                    shutil.rmtree(Queue_folder)
            except:
                print("No old Queue folder")

            await ctx.send("Getting everything ready now")

            voice = ctx.voice_client

            ydl_opts = {
                'format': 'bestaudio/best',
                'quiet': True,
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                print("Downloading audio now\n")
                ydl.download([carmelSongs[query]])

            for file in os.listdir("./"):
                if file.endswith(".mp3"):
                    name = file
                    print(f"Renamed File: {file}\n")
                    os.rename(file, "song.mp3")

            voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: check_queue())
            voice.source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = 0.40

            nname = name.rsplit("-", 2)
            await ctx.send(f"Playing: {nname[0]}")
            print("playing\n")
        else:
                await ctx.send("Not a valid Cal Combs song. Make sure the first letter is capitalized.")
    
    else:
        await ctx.send("Use !join [channel_name_here] to make the bot join a channel!")

        




@client.command()
async def viewqueue(ctx):

    if queuelist:
        for i in queuelist:
            await ctx.send(i)
    else:
        await ctx.send("No queue currently.")

@client.command()
async def viewplayers(ctx):
    for i in players.items():
        await ctx.send(i)


@client.command()
async def queue(ctx, *, query):
    if ctx.voice_client:
        if query in carmelSongs:
            if ctx.voice_client.is_playing():
                queuelist.append(query)
                await ctx.send("Adding " + query + " to the queue.")
                Queue_infile = os.path.isdir("./Queue")
                if Queue_infile is False:
                    os.mkdir("Queue")
                    print("Directory created.")
                DIR = os.path.abspath(os.path.realpath("Queue"))
                q_num = len(os.listdir(DIR))
                q_num += 1
                add_queue = True
                while add_queue:
                    if q_num in queues:
                        q_num += 1
                    else:
                        add_queue = False
                        queues[q_num] = q_num

                queue_path = os.path.abspath(os.path.realpath("Queue") + f"/song{q_num}.%(ext)s")
                print(str(queue_path))
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'quiet': True,
                    'outtmpl': queue_path,
                    'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }

                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    print("Downloading audio now\n")
                    ydl.download([carmelSongs[query]])
                    
                await ctx.send("Added " + queuelist[-1] + " to the queue")
                print("Song added to queue\n")
            else:
                await ctx.send("Please use !play instead.")
        else:
            await ctx.send("Make sure the song you request is from Cal Combs, and that the first letter is capitalized.")
    else:
        await ctx.send("You must be in a voice channel.")
    


@client.command()
async def stop(ctx):
    queues.clear()
    queuelist.clear()
    cache.clear()

    if ctx.voice_client is not None:
        ctx.voice_client.stop()


        await ctx.voice_client.disconnect()

        
        Queue_infile = os.path.isdir("/Queue")
        if Queue_infile is True:
                shutil.rmtree("Queue")
        else:
            print("no directory")
        
        myDir = os.getcwd()
        test = os.listdir(myDir)
        mysuffixes = (".mp3", ".m4a")
        for item in test:
            if item.endswith(mysuffixes):
                os.remove(os.path.join(myDir, item))



    
    


@client.command()
async def skip(ctx):
    ctx.voice_client.stop()
    mydir = os.getcwd()
    suffixes = (".mp3", ".m4a")
    test = os.listdir(mydir)

    for item in test:
        if item.endswith(suffixes):
            os.remove(os.path.join(mydir, item))


    await ctx.send("smh imagine not liking a cal combs song. here u go hater")

@client.command()
async def troubleshoot(ctx):
    for item in os.listdir("Queue"):
        print(item)
        await ctx.send(item)











    





survival = "Survival"
maxima = "Maxima"
manUp = "Man Up"
pchute = "Parachute"
cb = "Cowboy Bebop"
back =   "Backpack"
heart =   "Heart"
roundabouts = "Roundabouts"
condition =    "Conditioned"
perspectives =    "Perspectives" 
sun =    "Sunshine"
peace =    "Peace"
fof =    "Fight or Flight" 
skydream =    "Skydream"
fb =    "Free Bird" 
carmel =    "Carmel"




client.run(os.environ['TOKEN'])
    


