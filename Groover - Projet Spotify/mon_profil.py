from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
import pprint

client_id = "7e2ac52d061a45f3a98aed587fa98e6a"
client_secret = "307b35a1a965460a803eaf1c1fd16b73"


if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    username = '21zgphtkhjwbbepxhkdvxtuxy'

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace = True
user = sp.user(username)
pprint.pprint(user)

l=sp.current_user_followed_artists(limit=10,after=None)
print(l)