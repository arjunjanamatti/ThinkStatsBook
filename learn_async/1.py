import asyncio
import time

def square_num(num):
    return num**2

async def count(num):
    print(f'Square of {num}: {square_num(num)}')
    await asyncio.sleep(0.00000001)
    print(f'Square of {num+5}: {square_num(num+5)}')


async def main(num):
    await asyncio.gather(count(num), count(num), count(num))


if __name__ == '__main__':
    start_time = time.perf_counter()
    num = 10
    asyncio.run(main(num))
    end_time = time.perf_counter()
    total_time = end_time - start_time
    print(f'Total time: {total_time}')