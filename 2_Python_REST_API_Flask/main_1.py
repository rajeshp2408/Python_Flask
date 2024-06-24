from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'data':'Hello World!'}

class HelloName(Resource):
    def get(self, name):
        # self.name=name
        # return {"data": "Hello, {}".format(name)}
        return {"data": f"Hello, {name}"}

# api end point
api.add_resource(HelloWorld, '/hello')
api.add_resource(HelloName, '/hello/<string:name>')

@app.route("/")
def test_app():
    return "This is api page!!"



if __name__=="__main__":
    app.run(host="127.0.0.1", port=5571, debug=True)
