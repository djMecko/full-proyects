def palabra(url):
    from urllib import request
    from urllib.error import URLError
    try:
        file = request.urlopen(url)
    except URLError:
        return("La url: ",url,"No existe")   #Si imprimes el archivo file se va a ir a la mrd todo , imprime la url nomas
    else:
        contenido=file.read()
        return len(contenido.split())

print(palabra('https://www.gutenberg.org/cache/epub/2000/pg2000.txt'))
print(palabra('https://no-existe.txt'))