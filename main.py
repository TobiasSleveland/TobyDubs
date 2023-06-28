from discord.ext import commands
import discord
import cloudscraper

s = cloudscraper.create_scraper()
bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())

def crashPoint(num):
    info = s.get('https://api.bloxflip.com/games/crash').json()['history'][num]['crashPoint']
    print(info)
    return info



@bot.command(name="crash", description="Get prediction for the crash game")
async def slash_crash(ctx):
    six_crash_points = []
    twelve_crash_points = []
    eighteen_crash_points = []
    twentyfour_crash_points = []

    existing_crash_points = []

    # Import existing crash points
    for i in range(24):
        result = crashPoint(i)
        existing_crash_points.append(result)

    # Continue counting without recounting
    for i in range(6, 24):
        six_crash_points.append(existing_crash_points[i])

    for i in range(12, 24):
        twelve_crash_points.append(existing_crash_points[i])

    for i in range(18, 24):
        eighteen_crash_points.append(existing_crash_points[i])

    for i in range(24):
        twentyfour_crash_points.append(existing_crash_points[i])

    # get average of past 3 games
    average = float(sum(six_crash_points)) / len(six_crash_points)
    average2 = float(sum(twelve_crash_points)) / len(twelve_crash_points)
    average3 = float(sum(eighteen_crash_points)) / len(eighteen_crash_points)
    average4 = float(sum(twentyfour_crash_points)) / len(twentyfour_crash_points)
    print(average)
    prediction = (1 / (average - 2) / 1)
    prediction2 = (1 / (average2 - 2) / 1)
    prediction3 = (1 / (average3 - 2) / 1)
    prediction4 = (1 / (average4 - 2) / 1)
    if prediction < 1:
        prediction = 1. + prediction
    if prediction2 < 1:
        prediction2 = 1. + prediction2
    if prediction3 < 1:
        prediction3 = 1. + prediction3
    if prediction4 < 1:
        prediction4 = 1. + prediction4
    safe = ''
    safe2 = ''
    safe3 = ''
    safe4 = ''
    if prediction > 3:
        safe = 'Above 2x'
    elif prediction < 3:
        safe = "Less than 1.5x"
    elif prediction > 4:
        safe = 'Above 4x'
    prediction = "{:.2f}".format(prediction)

    if prediction2 > 3:
        safe2 = 'Above 2x'
    elif prediction2 < 3:
        safe2 = "Less than 1.5x"
    elif prediction2 > 4:
        safe2 = 'Above 4x'
    prediction2 = "{:.2f}".format(prediction2)

    if prediction3 > 3:
        safe3 = 'Above 2x'
    elif prediction3 < 3:
        safe3 = "Less than 1.5x"
    elif prediction3 > 4:
        safe3 = 'Above 4x'
    prediction3 = "{:.2f}".format(prediction3)

    if prediction4 > 3:
        safe4 = 'Above 2x'
    elif prediction4 < 3:
        safe4 = "Less than 1.5x"
    elif prediction4 > 4:
        safe4 = 'Above 4x'
    prediction4 = "{:.2f}".format(prediction4)

    em = discord.Embed(color=0xff55ff)
    em.add_field(name="TobyDubs Prediction Bot | (In development)", value="*- This is under development, so please use with care.*", inline=False)
    
    em.add_field(name="6-Api-based prediction:", value=f"**Prediction:** {prediction}x\n**Average:** {float(average)}\n**Safe bet:** {safe}", inline=False)
    em.add_field(name="12-Api-based prediction:", value=f"**Prediction:**  {prediction2}x\n**Average:** {float(average2)}\n**Safe bet:** {safe2}", inline=False)
    em.add_field(name="18-Api-based prediction:", value=f"**Prediction:**  {prediction3}x\n**Average:** {float(average3)}\n**Safe bet:** {safe3}", inline=False)
    em.add_field(name="24-Api-based prediction:", value=f"**Prediction:**  {prediction4}x\n**Average:** {float(average4)}\n**Safe bet:** {safe4}", inline=False)
    em.add_field(name="Crash History:", value=f"**Last Result:** {crashPoint(0)} \n**All results:** {twentyfour_crash_points}", inline=False)
    await ctx.reply(embed=em)

## @bot.command(name="crashhistory", description="Prints the history of crash.")
#async def slash_crashhistory(ctx, n: int):
  #  crash_points = []

  #  for i in range(n):
  #      crash_points.append(crashPoint(i))

  #  last_hit_1 = next((i for i, cp in enumerate(crash_points[::-1]) if cp == 1), None)
 #   last_hit_over_10 = next((i for i, cp in enumerate(crash_points[::-1]) if cp > 10), None)

  # response = f"Last {n} Crash Points:\n\n"
#    for i, cp in enumerate(crash_points, start=1):
 #       response += f"#{i}: {cp}\n"

 #   if last_hit_1 is not None:
 #       response += f"\nLast time it hit 1: #{n - last_hit_1}"
   # if last_hit_over_10 is not None:
   #     response += f"\nLast time it hit over 10: #{n - last_hit_over_10}"

   # await ctx.send(response)

@bot.command(name="mines", description="Placeholder command for mines game")
async def slash_mines(ctx):
    # Add your implementation for the /mines command here
    await ctx.reply("Mines game command")

@bot.command(name="roulette", description="Placeholder command for roulette game")
async def slash_roulette(ctx):
    # Add your implementation for the /roulette command here
    await ctx.reply("Roulette game command")

@bot.command(name="plinko", description="Placeholder command for plinko game")
async def slash_plinko(ctx):
    # Add your implementation for the /plinko command here
    await ctx.reply("Plinko game command")

@bot.command(name="towers", description="Placeholder command for towers game")
async def slash_towers(ctx):
    # Add your implementation for the /towers command here
    await ctx.reply("Towers game command")

bot.run('MTEyMDA4Mjk4NTY0MzkzMzY5Ng.GKgbRY.nND1NbeeKfEnwuh56_48LP5r_J7jbkWqxx49XY')
