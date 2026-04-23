def read_file():
    with open('readme.txt', 'r', encoding= 'utf-8') as file:
        content = file.read()
    print(content)