from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/age/<int:n>")
def age(n):
    

    if(n>18):
        result = {
            "age": n,
            "valid": True,
            "Port":"154.521.45"
        }

    else:
        result = {
            "age": n,
            "valid": False,
            "Port":"154.521.45"
        }     

    return jsonify(result)     

if __name__=="__main__":
    app.run(debug=True)
