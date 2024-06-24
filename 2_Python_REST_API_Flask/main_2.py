from flask import Flask
from flask_restful import Resource, Api, reqparse, abort

#
app=Flask(__name__)
api = Api(app)

# To store in dictionary
todos={
    1:{"task":"Taking a walk", "summary":"Night walk after lunch is good for health"},
    2:{"task":"Nap for the relax", "summary":"Nap is good for relax and peace"},
    3:{"task":"Learn programming", "summary":"Python is very good and easy to learn language"}
}

# Post parse message- body
task_post_args = reqparse.RequestParser()
task_post_args.add_argument("task", type=str,help="Task is required", required= True)
task_post_args.add_argument("summary", type=str, help="Summary is required", required= True)

class ToDo(Resource):
    def get(self, todo_id):
        return todos[todo_id]

    def post(self, todo_id):
        args = task_post_args.parse_args()
        if todo_id in todos:
            abort(401, "Task Id Exist")
        else:
            todos[todo_id]={"task": args["task"],"summary":args["summary"]}
        return todos[todo_id]

class ToDoList(Resource):
    def get(self):
        return todos


#
api.add_resource(ToDo, '/todos/<int:todo_id>')
api.add_resource(ToDoList, '/todos')


if __name__=="__main__":
    app.run(host="127.0.0.1", port=5571, debug=True)