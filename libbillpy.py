import billboard
import spotipy
import spotipy.util as util
import pprint

scope_read = "user-library-read"

print("Refreshing Billboard[R] charts>>>")
chart = billboard.ChartData('hot-100')
print("Done with: Refreshing Billboard[R] charts")

print("Initilizing Spotify[R] Web API>>>")
print("Logging you into Spotify...")
print("")
print("===================================================================")
username = input("Your Spotify[R] username: ")
print("===================================================================")
print("")
print("Logging in...")
token_read = util.prompt_for_user_token(username, scope_read, client_id="fd0faa7123584102b5893a4639ff7288", client_secret="347e543d63a94921b2455a26f0320481", redirect_uri="https://billpy.weebly.com")
spotify = spotipy.Spotify(auth=token_read)
print("Done with: Initilizing Spotify[R] Web API")

print("Welcome to BillPy. This project is based on billboard.py by guoguo12 and spotipy by plamere, all credits go to them!")

def refreshBillboard():
    chart = billboard.ChartData('hot-100')

def searchSpotify(songName, searchParam, searchLimit):
    results = spotify.search(q=songName, limit=searchLimit, type=searchParam)
    print(results)
    #print("No errors, but I'm still working on printing this output!")

def getTopSong():
    topSong = chart[0]
    print("Current top song on Billboard[R] is:")
    print("1>"+"'"+topSong.title+"'"+" by "+topSong.artist)
    searchSpotify(topSong.title, "track", 1)

def getMoreTopSongs():
    topSong1 = chart[0]
    topSong2 = chart[1]
    topSong3 = chart[2]
    topSong4 = chart[3]
    topSong5 = chart[4]
    print("Current top songs on Billboard are:")
    print("1>"+"'"+topSong1.title+"'"+" by "+topSong1.artist)
    print("2>"+"'"+topSong2.title+"'"+" by "+topSong2.artist)
    print("3>"+"'"+topSong3.title+"'"+" by "+topSong3.artist)
    print("4>"+"'"+topSong4.title+"'"+" by "+topSong4.artist)
    print("5>"+"'"+topSong5.title+"'"+" by "+topSong5.artist)  
getTopSong()