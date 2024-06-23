import flask
from flask import jsonify, request

app= flask.Flask(__name__)
app.config["DEBUG"] = True #Can defind debug 1

games=[{'console': 'PS5',
       'name': 'Call of Duty'},
      {'console': 'XBOX',
       'name': 'GTA 5'},
      {'console': 'XBOX',
       'name': 'Minecraft'},
      {'console': 'XBOX',
       'name': 'Mad Max'},
      {'console': 'Nintendo Switch',
       'name': 'Super Mario Bros.™ Wonder'},
      {'console': 'Nintendo Switch',
       'name': "Luigi's Mansion™ 2 HD"},
      {'console': 'Nintendo Switch',
       'name': "Mario Kart™ 8 Deluxe"}]

# All games
@app.route("/all", methods =['GET'])
def  run_app():
    return jsonify(games)

# Specific console
@app.route("/api", methods =['GET'])
def  getGames():
    console=request.args['console']
    result =[]
    for game in games:
        if game['console']== console:
            result.append(game)

    return jsonify(result)

if __name__=="__main__":
    # app.run(host="127.0.0.1", port= 5571, debug= True) #Define Debug 2
    app.run(host="127.0.0.1", port= 5571)
