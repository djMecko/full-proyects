def pib(url,country='AT'):
    from urllib import request
    from urllib.error import URLError
    try:
        archivo=request.urlopen(url)
    except URLError:
        print("¡La URL ",url," no existe")
    else:
        f= archivo.read().decode('utf-8').split('\n')
        f = [i.split('\t') for i in f]
        f = [list(map(str.strip, i)) for i in f]
        print(f)
        
pib("https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true")
