import asyncio
import random



async def set_first_value():
    summa = 0
    await asyncio.sleep(0)
    for i in range(random.randint(500,700)):
        summa +=i
    future_one.set_result(summa)


async def set_second_value():
    summa = 0
    await asyncio.sleep(0)
    for i in range(random.randint(1,10)):
        summa +=i
    future_two.set_result(summa)

    
async def divide_on_two():
    get_from_future_one = await future_one
    get_from_future_two = await future_two
    future_three.set_result(get_from_future_one//get_from_future_two)

async def is_even_or_odd():
    get_from_future_three = await future_three
    if get_from_future_three % 2 == 0:
        print(f"{get_from_future_three} is even") 
    else:
        print(f"{get_from_future_three} is odd") 

async def close_event(event_time_limit):
    await asyncio.sleep(event_time_limit)
    event_loop.stop()



future_one = asyncio.Future()
future_two = asyncio.Future()
future_three = asyncio.Future()



event_loop = asyncio.get_event_loop()

event_loop.create_task(set_first_value())
event_loop.create_task(set_second_value())
event_loop.create_task(divide_on_two())
event_loop.create_task(is_even_or_odd())
event_loop.create_task(close_event(1))

event_loop.run_forever()
