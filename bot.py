import discord
import os
import random

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 100):
    await ctx.send("he" * count_heh)

@bot.command()
async def repetirMensaje(ctx,*,mensaje):
    await ctx.send(mensaje)

@bot.command()
async def Hey(ctx):
    await ctx.send(f"Hey!")

@bot.command()
async def Xd(ctx):
    await ctx.send(f"Xd")

@bot.command()
async def guardar_y_enviar(ctx,*,texto):
    canal_id="1234289818775851051"

    canal_destino=bot.get_channel(int(canal_id))

    if canal_destino is None:
        await ctx.send("el canal no existe")
        return
    await canal_destino.send(texto)
    await ctx.send("Mensaje enviado al canal juegos")


@bot.command()
async def mem(ctx):
    with open("img/meme1.jpg", "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

lista_contaminacion=(os.listdir("contaminacion"))
@bot.command()
async def contaminacion(ctx):
    contaminacion_seleccionado=random.choice(lista_contaminacion)
    ruta_contaminacion = os.path.join("contaminacion", contaminacion_seleccionado)
    with open(ruta_contaminacion, "rb") as contaminacion_file:
        await ctx.send(file=discord.File(contaminacion_file))

lista_memes=(os.listdir('img'))
@bot.command()
async def meme(ctx):
    meme_seleccionado=random.choice(lista_memes)
    ruta_meme = os.path.join('img', meme_seleccionado)
    with open(ruta_meme, 'rb') as meme_file:
        await ctx.send(file=discord.File(meme_file))


bot.run("MTI0MTUxNzU3NzQ1MzQzNjk3OQ.G1y-sS.GucpEkMxW013CKhRzBSsMnAqGkgbG0mF5B2RPs")
