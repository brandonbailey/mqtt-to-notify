from flask import Flask, render_template
import notify

app = Flask(__name__)

@app.route("/")
def index():
    return "This is the homepage"

@app.route("/bindings")
def bindings():
    binding_list = notify.get_bindings()
    print(binding_list)
    return render_template('bindings.html', binding_list=binding_list)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)