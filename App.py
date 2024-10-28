from flask import Flask, jsonify, request
from flask_restful import Api, Resource


app = Flask(name)
api = Api(app)


items = []



class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return jsonify(item)
        return {'message': 'Item not found'}, 404

    def post(self):
        data = request.get_json()
        new_item = {
            'name': data['name'],
            'price': data['price']
        }
        items.append(new_item)
        return jsonify(new_item)

    def delete(self, name):
        global items
        items = [item for item in items if item['name'] != name]
        return {'message': 'Item deleted'}

api.add_resource(Item, '/item/<string:name>')

class ItemList(Resource):
    def get(self):
        return jsonify(items)

    def post(self):
        data = request.get_json()
        new_item = {
            'name': data['name'],
            'price': data['price']
        }
        items.append(new_item)
        return jsonify(new_item)




api.add_resource(ItemList, '/item')




if name == 'main':
    app.run(debug=True)
