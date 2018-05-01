import billboard
import spotipy
print("Refreshing Billboard[R] charts, please wait...")
chart = billboard.ChartData('hot-100')
print("Initilizing Spotify Web API...")
sp = spotipy.Spotify()
print("Welcome to BillPy. This project is based on billboard.py by guoguo12 and spotipy by plamere, all credits go to them!")
print("For help, type 'help' into the prompt below.")
def getTopSong():
    topSong = chart[0]
    print("Current top song on Billboard[R] is:")
    print("'"+topSong.title+"'"+" by "+topSong.artist)
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
def commanderSh():
    print("billpy>")
    getMoreTopSongs()
commanderSh()    