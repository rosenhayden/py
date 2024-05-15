import urllib.request
import json
#https://api.quotable.io
def readURL(url):
    resp = urllib.request.urlopen(url)
    raw = resp.read()
    data = json.loads(raw)
    return data

def getData(author):
    url = "https://api.quotable.io/authors?query=" + author
    req = urllib.request.Request(url, headers={ "User-Agent": "Mozilla/5.0" })
    data = readURL(url)
    slug = data["results"][0]["slug"]
    
    quotesurl = "https://api.quotable.io/quotes?author=" + slug
    data = readURL(quotesurl)
    
    results = data["results"]
    for result in results:
        print(result["content"])
def main():
    author = input("Enter author: ")
    getData(author)

if __name__ == "__main__":
    main()
