class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6014072313"
    sudo_users = "5005777092", "6014072313"
    GROUP_ID = -1001945999343
    TOKEN = "6997813229:AAEnU-K_dSCLC7z9ed0tB-P53PX8RfY6Eos"
    mongo_url = ""
    PHOTO_URL = ["https://graph.org/file/dd023dd7a7d59e53815a7.jpg", "https://graph.org/file/983c0d9ef32c50b43c91e.jpg"]
    SUPPORT_CHAT = "SD_Botssupport"
    UPDATE_CHAT = "SD_Botssupport"
    BOT_USERNAME = "Kidnap_your_waifu_Bot"
    CHARA_CHANNEL_ID = "-1001855181135"
    api_id = 
    api_hash = ""

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
