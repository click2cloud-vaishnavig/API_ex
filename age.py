from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def hello_world():
    if request.method=="GET":
        return jsonify({"response":"GET Request"})

    elif request.method=="POST":
        reqJson=request.json
        name=reqJson['name']
        return jsonify({"response":"POST Request by " + name})
    



if __name__=="__main__":
    app.run(debug=True,port= 6000)
