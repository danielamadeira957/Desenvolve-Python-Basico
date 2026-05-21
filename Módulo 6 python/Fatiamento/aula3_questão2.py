urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]
#O fatiamento [4:-4] remove os 4 primeiros caracteres ("www.")
#e os 4 últimoa caracteres (".com")
dominios = [url[4:-4]for url in urls]

print (f"ULs: {urls}")
print (f"dominios: {dominios}")