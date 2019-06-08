from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/portfolio/google/")
def google():
    return render_template("google.html")

@app.route("/portfolio/peluqueria/")
def peluqueria():
    return render_template("peluqueria.html")

@app.route("/portfolio/facebook/")
def facebook():

    mensaje = "Don't give a shit today, probably won't give a fuck tomorrow."
    return render_template("facebook.html")

@app.route("/about/")
def about():
    mensaje = "Tampoco mucho más, sorry"
    return render_template("about.html")



if __name__ == '__main__':
    app.run()

