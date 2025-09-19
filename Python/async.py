import asyncio

async def wait():
    print("wait start")
    await asyncio.sleep(2)
    print("wait end")
    
async def test(x:int):
    return x



async def main():
    await asyncio.gather(
        wait(),
        wait()
    )
    t1 = asyncio.create_task(test(1))
    t2 = asyncio.create_task(test(2))
    done, pending = await asyncio.wait({t1, t2},return_when=asyncio.ALL_COMPLETED)
    for d in done:
        print(d.result())    

asyncio.run(main())
