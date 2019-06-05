from discord.ext import commands
from interpreter import Interpreter
import requests, json

config = json.load(open("config.json")) # Thanks Colton

bot = commands.Bot(command_prefix=config["prefix"])

#def create_auth_session(request):
#	request.post("https://auth.roblox.com/v2/login", request)
	

@bot.event
async def on_ready():
	#create_auth_session(config["bot_auth"])
	print("We have logged in as {0.user}".format(bot))

@bot.command(name="getuser")
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

@bot.command(name="run")
async def run_code(ctx, arg):
	parse = arg[3:len(arg)-3]
	await ctx.send(Interpreter(parse).expr())
	
bot.run(config["token"])
