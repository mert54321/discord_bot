
from config import TOKEN

import random
import discord
from discord.ext import commands

izinler = discord.Intents.all()
izinler.message_content = True

bot = commands.Bot(command_prefix="bot ",intents=izinler)
chars = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

@bot.event
async def on_ready():
    print(f"{bot.user.name} bağlandı")



@bot.command("topla")
async def islem(ctx, sayi1, sayi2):
    toplam = int(sayi1) + int(sayi2)
    await ctx.channel.send(f"toplam: {toplam}")
    
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith("hello"):
        await message.channel.send(f"hello I am {bot.user.name}")

@bot.command("çıkar")
async def islem(ctx, sayi1, sayi2):
    eksil = int(sayi1) - int(sayi2)
    await ctx.channel.send(f"fark: {eksil}")

@bot.command("böl")
async def islem(ctx, sayi1, sayi2):
    bolum = int(sayi1) / int(sayi2)
    await ctx.channel.send(f"bölüm: {bolum}"),

@bot.command("çarp")
async def islem(ctx, sayi1, sayi2):
    sonuc = int(sayi1) * int(sayi2)
    await ctx.channel.send(f"sonuç: {sonuc}")

@bot.command("şifre")
async def islem(ctx, adet):
    sifre = ""
    for i in range(int(adet)):
        sifre += random.choice(chars)
    await ctx.channel.send(f"şifre: {sifre}")

     #ve bu yaptıracağnız şeyi türkçe harf kullanmadan yazınız

@bot.command("yardım")
async def islem(ctx):
    await ctx.channel.send(f"bana birşey demek için bot yazınız, bana birşey yaptırmak için botun sonuna yaptıracağnızı yazın iyi şanslar😎")

bot.run(TOKEN)