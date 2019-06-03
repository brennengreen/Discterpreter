import discord
from discord.ext import commands
import requests

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
	print("We have logged in as {0.user}".format(bot))

@bot.command(name="getuser")
async def get_user(ctx, arg):
	user_id = arg
	request_url = "https://api.roblox.com/users/{}".format(user_id)
	
	resp = requests.get(request_url)
	if resp.status_code != 200:
		await message.channel.send("Invalid UserId!\n```GET /users/{} Error Code:{}```".format(user_id, resp.status_code))
		return
	
	await ctx.send(resp.json()['Username'])

bot.run("NTg0MTY1OTkwMzM0NzI2MTY0.XPG9vA.BtYle3fZ0exIffEg8824Ja82FvY")