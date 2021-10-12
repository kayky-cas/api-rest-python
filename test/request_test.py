import requests

BASE = "http://localhost:5000/"


def debug(type, path):
    print(type + " on \"/" + path + "\"")


def get(path=""):
    debug('GET', path)
    return requests.get(BASE + path).json()


def post(path=""):
    debug('POST', path)
    return requests.post(BASE + path).json()


# GET on "/hello/:name"
print(get("album/1"))
