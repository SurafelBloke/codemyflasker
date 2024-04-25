from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    first_name = "wick"
    stuff = "this is bold text"
    favorite_pizza = ["pepperoni","Cheese","Mushrooms", 41]
    return render_template("index.html", 
                           first_name=first_name,
                           stuff =stuff,
                           favorite_pizza = favorite_pizza)


@app.route("/user/<name>")
def user(name):
    return render_template("user.html", user_name=name) 


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500


if __name__ in "__main__":
    app.run(debug=True)

