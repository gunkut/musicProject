from spotify import *
import time

print("""
|----------------------------|
|    Welcome to Spotify      |
|----------------------------|
|    View Playlist "all"     |
|----------------------------|
|    Current Music   "1"     |
|----------------------------|
|    Play Music     "play"   |
|----------------------------|
|    To Add Music     "2"    |
|----------------------------|
|    To Delete Music  "3"    |
|----------------------------|
|    To Play Random   "4"    |
|----------------------------|
|    Press "exit" To Exit    |
|----------------------------|
""")

spotify = Storage()

while True:
    operation = input("request:")

    if(operation == "exit"):

        print("exiting program...")
        time.sleep(1)
        print("done")

        break

    elif(operation == "all"):
        spotify.music_library()

    elif(operation == "1"):

        spotify.playing_music()

    elif(operation == "play"):

        playing_music = input("which song:")
        spotify.play_music(playing_music)

        while True:
            operation2 = input("request for play:")

            if(operation2 == ">"):
                spotify.go_next_music()

            elif (operation2 == "<"):
                spotify.go_previous_music()

            elif (operation2 == "|"):
                print("stopping music...")
                time.sleep(1)
                spotify.stop_music()
                print("music stopped")

            elif (operation2 == "i"):
                spotify.music_infos()

            elif(operation2 == "back"):
                break

            else:

                print("invalid command")

    elif(operation == "2"):

        name = input("name:")
        singer = input("singer::")
        album = input("album:")
        date = input("date:")
        duration = input("duration:")

        new_song = Music(name, singer, album, date, duration)
        spotify.add_music(new_song)

    elif(operation == "3"):
        delete_name = input("which one:")
        spotify.delete_music(delete_name)

    elif(operation == "4"):
        spotify.play_random_music()

        while True:
            operation2 = input("request for play:")

            if(operation2 == ">"):
                spotify.go_next_music()

            elif (operation2 == "<"):
                spotify.go_previous_music()

            elif (operation2 == "|"):
                print("stopping music...")
                time.sleep(1)
                spotify.stop_music()
                print("music stopped")

            elif (operation2 == "i"):
                spotify.music_infos()

            elif(operation2 == "back"):
                break

            else:
                print("invalid command")

    else:

        print("invalid command")