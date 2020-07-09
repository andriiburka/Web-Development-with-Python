from module4_python_oop.dir1_defining_classes.ex8_spoopify.project.band import Band
from module4_python_oop.dir1_defining_classes.ex8_spoopify.project.song import Song


class Album:
    def __init__(self, name: str, songs=None):
        self.name = name
        self.songs = songs  # songs(one, many or none)
        self.published = False

    def add_song(self, song: Song):
        if isinstance(song, list):
            print(type(song), "IS LIST")
        else:
            print(type(song), "NOT LIST")

    def details(self):
        pass

    def publish(self):
        pass


################   INPUT   ######################
song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())
