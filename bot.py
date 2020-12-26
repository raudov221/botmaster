from vkbottle.bot import Bot, Message
from vkbottle.keyboard import Keyboard, Text
from googlesearch import search
import random
import random as r
import json

token = "be63361da09dc7eb87fd452d690d65646f391b002a28d21b3e5d086a704d464a0652995880826f0d76bb5"
group_id = 201396822

bot = Bot(token)

def reg( ans ):
    data = json.load( open( "data.json", "r" ) )
    if str( ans.from_id ) in data[ "user" ]:
        pass
    else:
        data[ "user" ][ str( ans.from_id ) ] = "reg"
        data[ "balance" ][ str( ans.from_id ) ] = "0"
        data[ "rabota" ][ str( ans.from_id ) ] = "0"
        data[ "nick"][ str( ans.from_id ) ] = ""
        data[ "rabota1" ][ str( ans.from_id ) ] = "0"
        data[ "id" ][ str( ans.from_id ) ] = str( len( data[ "user" ] ) )
        json.dump( data, open( "data.json", "w" ) )

@bot.on.chat_message(text=["Проф", "Профиль", "проф", "профиль"])
async def wrapper(ans: Message):
    reg(ans)
    data = json.load( open( "data.json", "r" ) )
    await ans(f"Ваш профиль: \n\nБаланс: {data[ 'balance' ][ str( ans.from_id ) ]}\nАйди: {data[ 'id' ][ str( ans.from_id ) ]}\nРабота: {data[ 'rabota1' ][ str( ans.from_id ) ]}")

@bot.on.chat_message(text=["устроиться 1", "Устроиться 1"])
async def wrapper(ans: Message):
    reg(ans)
    data = json.load( open( "data.json", "r" ) )
    if data[ "rabota" ][ str( ans.from_id ) ] == "0":
        await ans(f"Вы начали работать таксистом!")
        data[ "rabota" ][ str( ans.from_id ) ] = int( data[ "rabota" ][ str( ans.from_id ) ] ) + 1
        data["rabota1"][str(ans.from_id)] = "Таксист"
        json.dump(data, open("data.json", "w"))
    else:
        await ans(f"У вас уже есть работа или вы уже устроены на работу таксист!")

@bot.on.chat_message(text=["Таксист", "Такси", "такси", "таксист"])
async def wrapper(ans: Message):
    reg(ans)
    data = json.load( open( "data.json", "r" ) )
    if data[ "rabota" ][ str( ans.from_id ) ] == "0":
        await ans(f"Вы не устроены на работу таксист!")
    else:
        data[ "balance" ][ str( ans.from_id ) ] = int( data[ "balance" ][ str( ans.from_id ) ] ) + 500
        await ans(f"Вы успешно заработали 500$\n\nВаш баланс: {data['balance'][str(ans.from_id)]}")
        json.dump(data, open("data.json", "w"))

@bot.on.chat_message(text=["казино <sum>", "Казино <sum>"])
async def wrapper(ans: Message, sum):
    reg(ans)
    data = json.load( open( "data.json", "r" ) )
    if data[ "balance" ][ str( ans.from_id ) ] < int(sum):
        await ans(f"Ваша сумма больше баланса!")
    else:
        random1 = random.randint(1,5)
        if random1 == 1:
            await ans(f"Вы проиграли (x0)")
            data["balance"][str(ans.from_id)] = int(data["balance"][str(ans.from_id)]) - int(sum)
            json.dump(data, open("data.json", "w"))
        if random1 == 2:
            await ans(f"Вы проиграли (x0)")
            data["balance"][str(ans.from_id)] = int(data["balance"][str(ans.from_id)]) - int(sum)
            json.dump(data, open("data.json", "w"))
        if random1 == 3:
            await ans(f"Вы выйграли (x2)")
            int(sum) + int(sum) *2
            data["balance"][str(ans.from_id)] = int(data["balance"][str(ans.from_id)]) + int(sum)
            json.dump(data, open("data.json", "w"))
        if random1 == 4:
            await ans(f"Вы выйграли (x5)")
            int(sum) + int(sum) *5
            data["balance"][str(ans.from_id)] = int(data["balance"][str(ans.from_id)]) + int(sum)
            json.dump(data, open("data.json", "w"))
        if random1 == 5:
            await ans(f"Вы выйграли (x50)")
            int(sum) + int(sum) *50
            data["balance"][str(ans.from_id)] = int(data["balance"][str(ans.from_id)]) + int(sum)
            json.dump(data, open("data.json", "w"))

@bot.on.chat_message(text=["стаканчик <sum> <stak>", "Стаканчик <sum> <stak>"])
async def wrapper(ans: Message, sum, stak):
    reg(ans)
    data = json.load( open( "data.json", "r" ) )
    if data[ "balance" ][ str( ans.from_id ) ] < int(sum):
        await ans(f"Ваша сумма больше баланса!\n\nПример: (Стаканчик сумма стаканчик, стаканчик 400 3)")
    if int(stak) > 3:
        await ans(f"Ваш Стаканчик больше 3!\n\nПример: (Стаканчик сумма стаканчик, стаканчик 400 3)")
    if int(stak) < 4:
        if data[ "balance" ][ str( ans.from_id ) ] > int(sum):
            random1 = random.randint(1,3)
            if random1 == int(stak):
                await ans(f"Вы угадали мячик был под {random1}! Ваша ставка умножается в 2 раза!")
                int(sum) + int(sum) * 2
                data["balance"][str(ans.from_id)] = int(data["balance"][str(ans.from_id)]) + int(sum)
                json.dump(data, open("data.json", "w"))
            else:
                await ans(f"Вы не угадали мячик был под {random1}!")
                data["balance"][str(ans.from_id)] = int(data["balance"][str(ans.from_id)]) - int(sum)
                json.dump(data, open("data.json", "w"))

@bot.on.chat_message(text=["<da>"])
async def wrapper(ans: Message, da):
    reg(ans)
    data = json.load( open( "data.json", "r" ) )
    if data[ "rabota" ][ str( ans.from_id ) ] == "0":
        data["rabota1"][str(ans.from_id)] = "Без работный"
        json.dump(data, open("data.json", "w"))

bot.run_polling( skip_updates = False )