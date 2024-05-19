from flask import Flask, render_template

app = Flask(__name__)
# route -> marketboost.com/
# função -> o que você quer exibir naquela página
# template

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/dashboard")
def dashboard():
    return render_template("contatos.html")

# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)

    # servidor do heroku

