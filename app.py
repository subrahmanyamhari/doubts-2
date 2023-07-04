from flask import Flask, render_template, request, jsonify
from model_prediction import *

app = Flask(__name__)

text=""
predicted_emotion=""
predicted_emotion_img_url=""

@app.route("/")
def home():
    entries = show_entry()
    return render_template("index.html", entries=entries)
    

@app.route("/predict-emotion", methods=["POST"])
def predict_emotion():
    input_text = request.json.get("text")
    if not input_text:
        return jsonify({
            "status": "error",
            "message": "Please enter some text to predict emotion!"
        }), 400
    else:
        predicted_emotion, predicted_emotion_img_url = predict(input_text)                         
        return jsonify({
            "data": {
                "predicted_emotion": predicted_emotion,
                # "predicted_emotion_img_url": predicted_emotion_img_url
            },
            "status": "success"
        }), 200
        
#Write the code for API here
@app.route("/saveentry", methods=["POST"])
def saveentry():
    save_text=request.json.get("text")
    save_date=request.json.get("date")
    save_emotion=request.json.get("emotion")
    data = f"'{save_text}','{save_date}','{save_emotion}'"
    with open("static/assets/data_files/data_entry.csv") as f :
        f.write(data)
    return jsonify("success")


if __name__ == "__main__":
    app.run(debug=True)