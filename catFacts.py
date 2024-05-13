import json
import urllib.request
import pprint
import urllib.parse


def main():
    url = "https://cat-fact.herokuapp.com/facts"
    req = urllib.request.urlopen(url)
    resp = req.read()
    data = json.loads(resp)
    for fact in data:
        print(fact["text"])
if __name__ == "__main__":
    main()
