import time
import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования')
    ball = 0
    while ball <= 4:
        ball += 1
        await asyncio.sleep(power)
        print(f'Силач {name} поднял {ball}')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():  # в которой создаются 3 задачи для функций start_strongman
    task_1 = asyncio.create_task(start_strongman('Pasha', 2))
    task_2 = asyncio.create_task(start_strongman('Denis', 5))
    task_3 = asyncio.create_task(start_strongman('Apollon', 8))
    await task_1
    await task_2
    await task_3


start = time.time()
asyncio.run(start_tournament())
finish = time.time()

print(f'--------время работы = {round(finish - start, 2)} секунд--------')
