from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    titulo_pagina = "Inicio - Richard Casares"
    mensaje = "Por aquí poco, utiliza el menú de navegación"
    return render_template("index.html", titulo_pagina=titulo_pagina, mensaje=mensaje )

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/portfolio/google/")
def google():
    titulo_pagina = "Google - Richard Casares"
    mensaje = "Scusa se lo cancello"
    return render_template("google.html", titulo_pagina=titulo_pagina, mensaje=mensaje )

@app.route("/portfolio/peluqueria/")
def peluqueria():
    titulo_pagina = "Mi peluquería - Richard Casares"
    return render_template("peluqueria.html",titulo_pagina=titulo_pagina)

@app.route("/portfolio/facebook/")
def facebook():
    titulo_pagina = "Face de bouc - Richard Casares"
    mensaje = "Don't give a shit today, probably won't give a fuck tomorrow."
    return render_template("facebook.html",titulo_pagina=titulo_pagina, mensaje=mensaje )

@app.route("/about/")
def about():
    titulo_pagina = "Sobre mí - Richard Casares"
    mensaje = "Tampoco mucho más, sorry"
    return render_template("about.html",titulo_pagina=titulo_pagina, mensaje=mensaje)



if __name__ == '__main__':
    app.run()

