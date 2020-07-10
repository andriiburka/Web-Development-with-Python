class PhotoAlbum:
    def __init__(self, pages):
        """self.photos is an empty matrix initially"""
        self.pages, self.photos = pages, [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        """New instance maker"""
        return cls(photos_count // 4)

    def add_photo(self, label):
        for i in range(len(self.photos)):

            if len(self.photos[i]) < 4:
                self.photos[i].append(label)
                return "{} photo added successfully on page {} slot {}" \
                    .format(label, i + 1, len(self.photos[i]))

        return "No more free spots"

    def display(self):
        result = '{:->11}\n'.format('')
        for page in self.photos:
            if page:
                result += ''.join('[] ' for _ in range(len(page)))[:-1]
            result += '\n{:->11}\n'.format('')
        return result
