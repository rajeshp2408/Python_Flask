from flask import Flask, render_template,request
import requests

app = Flask(__name__,template_folder="templates")

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/check", methods=['POST'] )
def check():
    url= request.form.get('url')
    if not url.startswith(('http://','https://')):
        url = 'http://'+ url
    try:
        response= requests.get(url, timeout=10)
        if response.status_code <400:
            status = 'UP'
        else:
            status = 'DOWN'
    except requests.RequestException:
        status = "Exception!!"

    return render_template("check.html", url=url, status=status)

if __name__ =="__main__":
    app.run(host="127.0.0.1", port=5571, debug=True)