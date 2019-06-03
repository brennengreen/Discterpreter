from discord.ext import commands
import requests, json

config = json.load(open("config.json")) # Thanks Colton

bot = commands.Bot(command_prefix=config["prefix"])

@bot.event
async def on_ready():
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
bot.run(config["token"])