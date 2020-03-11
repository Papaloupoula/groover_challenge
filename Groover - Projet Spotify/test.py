# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 14:29:15 2020

@author: Charles
"""

#SET SPOTIPY_CLIENT_ID = 7e2ac52d061a45f3a98aed587fa98e6a
#SET SPOTIPY_CLIENT_SECRET = 307b35a1a965460a803eaf1c1fd16b73

#username = '21zgphtkhjwbbepxhkdvxtuxy'

client_id = "7e2ac52d061a45f3a98aed587fa98e6a"
client_secret = "307b35a1a965460a803eaf1c1fd16b73"


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from parseur import ids

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))


## Test
results = sp.search(q='Booba+92i', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])
    
    
##☻

l=sp.current_user_followed_artists()
print(l)

##

sp.user_follow_artists(ids)


