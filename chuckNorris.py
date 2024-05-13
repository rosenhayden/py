import json
import urllib.request
import urllib.parse
def getData():
    url = "https://api.chucknorris.io/jokes/random"
    req = urllib.request.Request(url, headers={ "User-Agent": "Mozilla/5.0" })
    resp = urllib.request.urlopen(req)
    raw = resp.read()
    data = json.loads(raw)
    print(data["value"])

def main():
    getData()


if __name__ == "__main__":
    main()
