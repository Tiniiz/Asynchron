import asyncio


async def handle_echo(reader, writer):
    data = await reader.read(100)
    msg = data.decode()
    addr = writer.get_extra_info('peername')
    print(f'Получил {msg} от {addr}')

    writer.write(data)
    await writer.drain()

    writer.close()