from flask import Flask,render_template
import pandas as pd

app=Flask(__name__)


@app.route("/")
@app.route("/home")
def home_page():
    # return render_template("home.html",data = [df.to_html()], titles=[])
    # df = pd.read_csv("data.csv", index=False)

    df = pd.read_csv("data.csv").drop(['Unnamed: 0'],axis=1)
    df = df[1:]  # take the data less the header row

    print(df)
    return render_template("home.html",data = df)



if __name__=="__main__":
    app.run(host="127.0.0.1", port=5588, debug=True)