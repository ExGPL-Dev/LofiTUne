from Aviyaa.core.bot import Aviyaa
from Aviyaa.core.dir import dirr
from Aviyaa.core.git import git
from Aviyaa.core.userbot import Userbot
from Aviyaa.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Aviyaa()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
