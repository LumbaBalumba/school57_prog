import asyncio
import time


async def request(i: int):
    time.sleep(0.01)
    return {"username": f"user{i}"}


async def main():
    users = []
    for i in range(100):
        users.append(request(i))
    print("usernames requested")
    time.sleep(1)
    for user in users:
        user_a = await user
        print(user_a["username"])


asyncio.run(main())
