import asyncio
import websockets

SERVER = "ws://10.130.85.53:8765"

async def main():
    async with websockets.connect(SERVER) as ws:
        print("Connected to server!")

        async def send_loop():
            while True:
                msg = await asyncio.to_thread(input, "")
                await ws.send(msg)

        async def recv_loop():
            while True:
                message = await ws.recv()
                if message == "UPDATE":
                    # Ask server for latest chat
                    await ws.send("REQUEST_CHAT")
                else:
                    # Display chat content
                    print("=== Chat ===")
                    print(message)
                    print("=== End ===")

        await asyncio.gather(send_loop(), recv_loop())

asyncio.run(main())