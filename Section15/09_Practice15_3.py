class Song:
    def set_song(self,song,genre):
        self.song = song
        self.genre = genre

    def print_song(self):
        print(f'노래 제목 : {self.song}({self.genre})')

class Singer:
    def set_singer(self,singer):
        self.singer = singer

    def hit_song(self,song):
        self.song = song

    def print_singer(self):
        print('가수이름 : {}'.format(self.singer))
        self.song.print_song()

song = Song()
song.set_song("취중진담","발라드")

singer = Singer()
singer.set_singer("김동률")
singer.hit_song(song)

singer.print_singer()