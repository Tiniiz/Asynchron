import asyncio


async def tcp_echo_client(msg):
    reader, writer = await asyncio.open_connection('127.0.0.1', port)
    print(f'Отправил сообщение: {msg}')
    writer.write(msg.encode())
    await writer.drain()

    data = await reader.read(100)
    print(f'Получил: {data.decode()}')
    writer.close()
