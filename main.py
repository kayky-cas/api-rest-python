from flask import Flask, request
from flask_restful import Api, Resource
import uuid
import json


from models.album import Album

app = Flask(__name__)
api = Api(app)


class AlbumData(Album):
    def __init__(self, id, name, author, price):
        super().__init__(name, author, price)
        self.id = id


albums = {}


class AlbumResource(Resource):
    def get(self, id):

        album = None

        if hasattr(albums, id):
            album = albums[id]

        return {""+id: album}

    def put(self):
        album = json.loads(request.form['data'])
        print(album)
        id = str(uuid.uuid1())
        albums[id] = AlbumData(
            name=album['name'], author=album['author'], price=album['price'], id=id).__dict__

        print(albums)
        return {""+id: albums[id]}


api.add_resource(AlbumResource, '/album/<string:id>')


if __name__ == "__main__":
    app.run(debug=True)
