import asyncio
import time

async def count():
    print('One')
    await asyncio.sleep(0.00000001)
    print('Two')

async def main():
    await asyncio.gather(count(), count(), count())


if __name__ == '__main__':
    start_time = time.perf_counter()
    asyncio.run(main())
    end_time = time.perf_counter()
    total_time = end_time - start_time
    print(f'Total time: {total_time}')