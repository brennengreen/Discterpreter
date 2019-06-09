import discord
from interpreter import Interpreter
import requests, json

config = json.load(open("config.json")) # Thanks Colton

client = discord.Client()

#def create_auth_session(request):
#	request.post("https://auth.roblox.com/v2/login", request)


@client.event
async def on_ready():
	#create_auth_session(config["bot_auth"])
	print("We have logged in as {0.user}".format(client))

"""@bot.command(name="getuser")
async def get_user(ctx, arg):
	user_id = arg
	request_url = "https://api.roblox.com/users/{}".format(user_id)
	
	resp = requests.get(request_url)
	if resp.status_code != 200:
		await ctx.send("Invalid UserId!\n```GET /users/{} Error Code:{}```".format(user_id, resp.status_code))
		return
	
	await ctx.send(resp.json()['Username'])

@bot.command(name="getbot")
async def get_bot_repo(ctx):
	await ctx.send("Here's a link to my code! {}".format("https://www.github.com/brennengreen/DiscordBotTesting"))
"""

def parse(msg):
	stream = msg[3:len(msg)-3]
	return Interpreter(stream).expr()

@client.event
async def on_message(msg):
	if msg.author == client.user:
		return

	if msg.content.startswith("!run"):
		await msg.channel.send(parse(msg.content[5:]))
	elif msg.content.startswith("!repo"):
		await msg.channel.send(
			"Here's a link to my GitHub Repository! {}".format("https://www.github.com/brennengreen/DiscordBotTesting")
		)
	elif msg.content.startswith("!website"):
		await msg.channel.send("Sorry :grimacing:, I'm still learning this command") 
	elif msg.content.startswith("!feedback"):
		await msg.channel.send("You can message Drey#5314 on Discord with feedback!")
client.run(config["token"])
