import random
import sqlite3

class Music():

    def __init__(self, name, singer, album, date, duration):

        self.name = name
        self.singer = singer
        self.album = album
        self.date = date
        self.duration = duration

    def __str__(self):

        return "song:{}\nsinger:{}\nalbum:{}\ndate:{}\nduration:{}\n".format(self.name, self.singer, self.album, self.date, self.duration)

class Storage():

    current_music = ""

    def __init__(self):

        self.connection()

    def connection(self):

        self.connect = sqlite3.connect("spotify.db")
        self.cursor = self.connect.cursor()

        command = "create table if not exists Spotify_Musics(name TEXT,singer TEXT,album TEXT,date INT,duration FLOAT)"
        self.cursor.execute(command)
        self.connect.commit()

    def disconnection(self):

        self.connect.close()

    def music_library(self):

        command = "select * from Spotify_Musics"
        self.cursor.execute(command)
        list1 = self.cursor.fetchall()

        if(len(list1) == 0):
            print("music library is empty")

        else:
            for i in list1:
                print(i[0] + "\n")

    def music_infos(self):

        command = "select * from Spotify_Musics where name=?"
        self.cursor.execute(command, (self.current_music,))
        list2 = self.cursor.fetchall()

        if(len(list2) == 0):
            print("song not found")

        else:
            for i in list2:
                music = Music(i[0], i[1], i[2], i[3], i[4])
                print(music)

    def add_music(self, song):

        command="insert into Spotify_Musics values(?,?,?,?,?)"
        self.cursor.execute(command, (song.name, song.singer, song.album, song.date, song.duration))
        self.connect.commit()

    def delete_music(self, song_name):

        command = "delete from Spotify_Musics where name=?"
        self.cursor.execute(command, (song_name,))
        self.connect.commit()

    def play_music(self, song_name):

        command = "select * from Spotify_Musics where name=?"
        self.cursor.execute(command, (song_name,))
        list3 = self.cursor.fetchall()

        if(len(list3) == 0):
            print("song not found")

        else:
            print("""
|------------------|
|Next ">"          |
|------------------|         
|Back "<"          |
|------------------|         
|Stop "|"          |
|------------------| 
|Info "i"          |
|------------------|        
|To Go Back "back" |
|------------------|
""")
            self.current_music = list3[0][0]
            print("playing {}".format(self.current_music))

        self.connect.commit()

    def play_random_music(self):

        print("""
|------------------|
|Next ">"          |
|------------------|         
|Back "<"          |
|------------------|         
|Stop "|"          |
|------------------| 
|Info "i"          |
|------------------|        
|To Go Back "back" |
|------------------|
""")

        command = "select name from Spotify_Musics"
        self.cursor.execute(command)
        list4 = self.cursor.fetchall()

        self.current_music = (list4[random.randint(0, len(list4) - 1)])[0]
        print("playing {}".format(self.current_music))

        self.connect.commit()

    def go_next_music(self):

        command = "select name from Spotify_Musics"
        self.cursor.execute(command)
        list5 = (self.cursor.fetchall())

        j = -1

        for i in list5:
            j+=1

            if(j == len(list5)-1):
                j=0
                self.current_music = (list5[j])[0]

                break

            else:
                if(i[0]==self.current_music):
                    j+=1
                    self.current_music = (list5[j])[0]

                    break

        print("playing {}".format(self.current_music))

        self.connect.commit()

    def go_previous_music(self):

        command = "select name from Spotify_Musics"
        self.cursor.execute(command)
        list6 = self.cursor.fetchall()

        j = -1

        for i in list6:
            j += 1

            if(i[0] == self.current_music):
                if(j == 0):
                    j = len(list6) - 1
                    self.current_music = (list6[j])[0]

                    break

                else:
                    j -= 1
                    self.current_music = (list6[j])[0]

        print("playing {}".format(self.current_music))

        self.connect.commit()

    def playing_music(self):

        if(self.current_music == ""):
            print("no music playing")

        else:
            print("playing {}".format(self.current_music))


    def stop_music(self):

        self.current_music = ""