import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

# ID сообщения, на которое ставятся реакции
reaction_message_id = 1386926602788540496 # Заменить на свой ID

# Словарь: emoji → role_id
emoji_role_map = {
    "💙": 1233257245601566751,  # Роль "Friends"
    "💕": 1386918631123845181,  # Роль "Majestic"
    "🔥": 1386919024222277792,  # Роль "Dota2"
    "💋": 1386892442204114944,  # Роль "Bestie"
    "👓": 1386892145310568520,  # Роль "Bro"
    "🎮": 1386899464681422868,  # Роль "Free Game"
    "🔫": 1386899359764840588,  # Роль "ты Valorant"
    "🗡": 1386899418397282344,  # Роль "PoE2 player"
}

@bot.event
async def on_ready():
    print(f'✅ Бот запущен как {bot.user}')

@bot.event
async def on_raw_reaction_add(payload):
    if payload.message_id != reaction_message_id:
        return

    guild = bot.get_guild(payload.guild_id)
    role_id = emoji_role_map.get(str(payload.emoji))
    if role_id is None:
        return

    role = guild.get_role(role_id)
    member = guild.get_member(payload.user_id)

    if role and member:
        await member.add_roles(role)

        channel = bot.get_channel(payload.channel_id)
        if channel:
            msg = await channel.send(f"✅ {member.mention} получил роль **{role.name}**")
            await msg.delete(delay=5)  # Удалить сообщение через 5 секунд

@bot.event
async def on_raw_reaction_remove(payload):
    if payload.message_id != reaction_message_id:
        return

    guild = bot.get_guild(payload.guild_id)
    role_id = emoji_role_map.get(str(payload.emoji))
    if role_id is None:
        return

    role = guild.get_role(role_id)
    member = guild.get_member(payload.user_id)

    if role and member:
        await member.remove_roles(role)

        channel = bot.get_channel(payload.channel_id)
        if channel:
            msg = await channel.send(f"❌ {member.mention} потерял роль **{role.name}**")
            await msg.delete(delay=5)  # Удалить сообщение через 5 секунд

bot.run("MTM4NjkwMzMwOTA2NzIyMzI0MA.G_suaC.LVdiPPLT6EEL9kvF5-bhkOB9Mxs225im01zXVg")
