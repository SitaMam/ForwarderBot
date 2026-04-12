# Telegram Auto Forward Bot
# Works even if you're not admin of the source channel (uses your own account)
# Created by: SubhoBhai

from telethon import TelegramClient, events

# 1. Replace with your own API credentials from https://my.telegram.org
api_id = 20166660  # your API ID
api_hash = 'ac8d8536e2869da1e2388cea87d3e5f7'

# 2. Replace with your actual channel/chat IDs
source_channel = -1001234567890   # channel you want to read from
target_chat = -1002734643756           # friend, group, or channel to forward to

# 3. Create a TelegramClient session (stores login info)
client = TelegramClient('session', api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel))
async def forward_new_message(event):
    """Auto-forwards new messages from source_channel to target_chat"""
    try:
        await client.forward_messages(target_chat, event.message)
        print("✅ Message forwarded successfully.")
    except Exception as e:
        print(f"⚠️ Error forwarding message: {e}")

print("🚀 Auto-forward bot is running... Waiting for messages.")
client.start()
client.run_until_disconnected()
