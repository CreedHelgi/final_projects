import discord # Подключаем библиотеку
from discord.ext import commands
import random

intents = discord.Intents.default() # Подключаем "Разрешения"
intents.message_content = True
# Задаём префикс и интенты
bot = commands.Bot(command_prefix='>', intents=intents) 

fac = [
    "Глобальное потепление - это длительный процесс увеличения средней температуры Земли.",
    "Изменение климата вызвано в основном антропогенными факторами, такими как выбросы парниковых газов, в особенности углекислого газа (CO2).",
    "Согласно научным исследованиям, уровень CO2 в атмосфере сейчас выше, чем он был за последние несколько сотен тысяч лет.",
    "Расплавление ледников и полярных льдовых щитов приводит к подъему уровня мирового океана, что угрожает побережным городам и экосистемам.",
    "Экстремальные погодные явления, такие как ураганы, засухи и наводнения, становятся более частыми и сильными из-за изменения климата.",
    "Изменение климата влияет на сезонные циклы и зоны распространения живых организмов, вызывая сдвиги в экосистемах.",
    "Глобальное потепление также влияет на сельское хозяйство, приводя к изменениям в урожайности и распределении культурных растений.",
    "Изменение климата оказывает негативное воздействие на здоровье человека, увеличивая риск заболеваний, связанных с тепловым стрессом и распространением инфекций.",
    "Океаны поглощают большую часть дополнительного тепла, что приводит к изменениям в морских течениях и морской жизни.",
    "Разрушение коралловых рифов, вызванное повышением температуры воды и изменением pH, является одним из прямых последствий глобального потепления.",
    "Снег и лед отражают солнечные лучи обратно в космос, но с уменьшением площади ледников и снега увеличивается поглощение тепла, что ускоряет глобальное потепление.",
    "В отдаленных регионах, таких как Арктика, изменения климата происходят гораздо быстрее и имеют более серьезные последствия, чем в других частях мира.",
    "Мировые рынки и экономики также подвержены риску из-за глобального потепления, поскольку экстремальные погодные условия могут наносить ущерб сельскому хозяйству, торговле и инфраструктуре.",
    "Парниковые газы, такие как метан и диоксид азота, также вносят вклад в глобальное потепление, хотя их концентрация в атмосфере ниже, чем у CO2.",
    "Увеличение температуры ведет к таянию вечной мерзлоты, что может освобождать дополнительные объемы парниковых газов, усиливая эффект парникового эффекта.",
    "Научные модели предсказывают, что без дальнейших усилий по снижению выбросов парниковых газов глобальное потепление продолжится, и его последствия станут более серьезными.",
    "Международные соглашения, такие как Парижское соглашение, призваны координировать усилия стран по снижению выбросов и приспособлению к изменению климата.",
    "Технологии возобновляемой энергии, такие как солнечная и ветряная энергия, играют важную роль в снижении зависимости от источников энергии, способных усиливать глобальное потепление.",
    "Образование и информирование общественности о глобальном потеплении и его последствиях являются важными шагами в борьбе с этим явлением.",
    "Совместные усилия государств, предприятий и общественных организаций могут привести к сокращению выбросов парниковых газов и смягчению негативных последствий глобального потепления."]

# С помощью декоратора создаём первую команду
@bot.command()
async def fact(ctx):
    await ctx.send(fac[random.randint(0,19)])


bot.run('MTEzOTE5NDcwMzQzMTA4MjA2Ng.G3yTqH.ghNxfMZdIjNuMCq2JUJJZJf88cefdUSctbHkR4')