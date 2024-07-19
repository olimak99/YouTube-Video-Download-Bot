# ©️ LISA-KOREA | @LISA_FAN_LK | NT_BOT_CHANNEL | LISA-KOREA/YouTube-Video-Download-Bot

# [⚠️ Do not change this repo link ⚠️] :- https://github.com/LISA-KOREA/YouTube-Video-Download-Bot



from pyrogram import Client, filters
from Youtube.config import Config

# Create a Pyrogram client
app = Client(
    "TikTok_Downlloader_Bot",
    api_id=Config.29581147, 
    api_hash=Config.1fb9c7eb257dac875ec1a99b17528cfb, 
    bot_token=Config.6862774279:AAEG8o9zdyZGAdDsu7X4YlVZz8vwI_QSnJY,
    plugins=dict(root="Youtube")
)



# Start the bot
print("🎊 I AM ALIVE 🎊")
app.run()
