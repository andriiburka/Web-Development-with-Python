books_collection = input().split("&")
while True:
    command_line = input()
    if 'Done' in command_line:
        break
    else:
        command_line = command_line.split(' | ')
        operation = command_line[0]
        book = command_line[1]

        if 'Add Book' in operation and book not in books_collection:
            books_collection.insert(0, book)

        elif 'Take Book' in operation and book in books_collection:
            books_collection.remove(book)

        elif 'Swap Books' in operation and book in books_collection and command_line[2] in books_collection:
            book2 = command_line[2]
            index_book, index_book2 = \
                books_collection.index(book), \
                books_collection.index(book2)
            books_collection[index_book], books_collection[index_book2] = \
                books_collection[index_book2], \
                books_collection[index_book]

        elif 'Insert Book' in operation:
            books_collection.append(book)

        elif 'Check Book' in operation and int(book) <= len(books_collection):
            print(books_collection[int(book)])

print(f'{", ".join(books_collection)}')