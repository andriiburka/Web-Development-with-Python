class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = []
        # [input().split(' ') for i in range(int(input()))]

    def add_photo(self, param):
        """ """

    def display(self):
        """ expected print
        -----------
        [] [] [] []
        -----------
        [] []
        -----------
        """


album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
