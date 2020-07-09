class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [input().split(' ') for i in range(int(input()))]
