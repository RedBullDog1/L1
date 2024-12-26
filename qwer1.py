from telethon import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch

api_id = 123123123
api_hash = 123123123
phone = '+380123123123'
client = TelegramClient('session', api_id, api_hash)

async def fetch_channel_participants(channel_username, limit=2):
    await client.start()
    channel = await client.get_entity(channel_username)

    participants = await client(GetParticipantsRequest(
        channel,
        ChannelParticipantsSearch(''),
        offset=0,
        limit=limit,
        hash=0
    ))

    for user in participants.users:
        print(user.id, user.first_name, user.last_name)
async def send_message_to_saved():
    saved_message = "Тестовое сообщение"
    await client.send_message('me', saved_message)
    print("Сообщение отправлено.")
async def main():
    channel_username = '123'
    await fetch_channel_participants(channel_username)
    await send_message_to_saved()

with client:
    client.loop.run_until_complete(main())