class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6014072313"
    sudo_users = "5005777092", "6014072313"
    GROUP_ID = -1001945999343
    TOKEN = "6997813229:AAEnU-K_dSCLC7z9ed0tB-P53PX8RfY6Eos"
    mongo_url = "mongodb+srv://HaremDBBot:ThisIsPasswordForHaremDB@haremdb.swzjngj.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "SD_Botssupport"
    UPDATE_CHAT = "Collect_em_support"
    BOT_USERNAME = "Kidnap_your_waifu_Bot"
    CHARA_CHANNEL_ID = "-1002091841088"
    api_id = 26626068
    api_hash = "bf423698bcbe33cfd58b11c78c42caa2"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
