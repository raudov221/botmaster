from vkbottle.bot import Bot, Message
from vkbottle.keyboard import Keyboard, Text
import random
import random as r
import json

token = "fec3aaf303910eb963600399516f0625f73b9c2d4c1826b61c732bf90abf5efb5ad4792d620e264e36b84"
group_id = 200759417

bot = Bot(token)

def reg( ans ):
    data = json.load( open( "data.json", "r" ) )
    if str( ans.from_id ) in data[ "user" ]:
        pass
    else:
        data[ "user" ][ str( ans.from_id ) ] = "reg"
        data[ "balance" ][ str( ans.from_id ) ] = "0"
        data[ "balancer" ][ str( ans.from_id ) ] = "0"
        data[ "idr" ][ str( ans.from_id ) ] = "0"
        data[ "id" ][ str( ans.from_id ) ] = str( len( data[ "user" ] ) )
        json.dump( data, open( "data.json", "w" ) )

@bot.on.message_handler(text=["Проф", "Профиль", "проф", "профиль", "я", "Я"])
async def wrapper(ans: Message):
    reg(ans)
    data = json.load( open( "data.json", "r" ) )
    await ans(f"🦊 Ваш профиль: \n\n💵 Баланс: {data[ 'balance' ][ str( ans.from_id ) ]}\n🏆 Айди: {data[ 'id' ][ str( ans.from_id ) ]}\n📄 У кого ты работаешь: [Пользователь|id{data[ 'idr' ][ str( ans.from_id ) ]}]")

@bot.on.message_handler(text=["Реф <ref>", "реф <ref>", "/реф <ref>"])
async def wrapper(ans: Message, ref):
    reg(ans)
    data = json.load( open( "data.json", "r" ) )
    if int(ref) < 581563779:
        brawl = ref
        await bot.api.messages.send(user_id=brawl, random_id=0, message=f'🔮 У тебя новый раб: @id{ans.from_id}')
        await ans(f"🔮 Вы теперь работаете у [Пользователя|id{ref}]") 
        data[ "idr" ][ str( ans.from_id ) ] = int(ref)
        data[ "balancer" ][ str( ref ) ] + 1
        json.dump( data, open( "data.json", "w" ) ) 
    else:
        await ans("🚫 Такого пользователя не существует!")

@bot.on.message_handler(text=["получить", "Получить", "пол"])
async def wrapper(ans: Message):
    data = json.load( open( "data.json", "r" ) )
    balancer = data[ "balancer" ][ str( ans.from_id ) ] 
    if int(balancer) == 0:
        await ans(f"🔮 У вас нету рабов!")
    if int(balancer) == 1:
        b = data[ "balancer" ][ str( ans.from_id ) ] 
        c = int(b) / 2
        data[ "balance" ][ str( ans.from_id ) ] + int(c) 
        data[ "balancer" ][ str( ans.from_id ) ] = b
        await ans(f"🔮 Вы получили от 1 раба {c}₽")
    if int(balancer) < 2:
        b = data[ "balancer" ][ str( ans.from_id ) ] 
        c = int(b) / 2
        data[ "balance" ][ str( ans.from_id ) ] + int(c)
        data[ "balancer" ][ str( ans.from_id ) ] = b
        await ans(f"🔮 Вы получили от {data[ 'balancer' ][ str( ans.from_id ) ]} рабов {c}₽")
    json.dump( data, open( "data.json", "w" ) ) 

bot.run_polling( skip_updates = False )
