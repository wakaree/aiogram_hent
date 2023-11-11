"""
Simple asyncio using example.
"""

import asyncio


async def foo(x: int) -> None:
    """
    Use this function just to print "Foo"
    param x: The value that will be printed as "Foo x"
    """
    await asyncio.sleep(1)
    print("Foo {}!".format(x))  # noqa: T201


async def bar(x: int) -> None:
    """
    Use this function just to print "Bar"
    param x: The value that will be printed as "Bar x"
    """
    await asyncio.sleep(1)
    print("Bar {}!".format(x))  # noqa: T201


async def main() -> None:
    """
    Main function. Creating 200 tasks and running in concurrently
    """
    tasks = []

    for i in range(100):
        tasks.append(asyncio.create_task(foo(i)))
        tasks.append(asyncio.create_task(bar(i)))

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
