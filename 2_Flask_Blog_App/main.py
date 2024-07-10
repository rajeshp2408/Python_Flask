from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def main_page():
    return render_template("home.html")

if __name__=="__main__":
    app.run(host="127.0.0.10", port=5588, debug=True)