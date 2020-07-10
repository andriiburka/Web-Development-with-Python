path = (input().split('\\')[-1]).split('.')
file = {'name': path[0], 'extension': path[1]}
print(f"File name: {file['name']}\nFile extension: {file['extension']}")

