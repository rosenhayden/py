import json
import urllib.request
import urllib.parse
def getData(userInput):
    url = "http://ZiptasticAPI.com/" + userInput
    req = urllib.request.Request(url, headers={ "User-Agent": "Mozilla/5.0" })
    resp = urllib.request.urlopen(req)
    raw = resp.read()
    data = json.loads(raw)
    print("The zip is for:" + data["city"] + ", " + data["state"])    

def main():
    userInput = input("Enter a zip: ")
    getData(userInput)




if __name__ == "__main__":
    main()
