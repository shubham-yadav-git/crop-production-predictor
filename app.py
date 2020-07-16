from flask import Flask, request, jsonify, render_template
from joblib import load

app = Flask(__name__)

model = load("cpp27.joblib")

input_features = ["up", "bihar", "punjab", "uk", "kerala", "odisha", "chattisgarh", "jharkhand",
                  "hp", "ap", "jk", "tn", "kharif", "rabi", "wholeyear",
                  "summer", "winter", "rice", "wheat", "potato", "drychillies", "maize", "masoor", "moong", "onion",
                  "peas", "ragi", "rapeseed", "sesamum", "urad", "groundnut", "gram"]
features_dict = {}
for i in input_features:
    features_dict[i] = 0


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=["POST"])
def predict():
    # for rendering results in html gui
    # noinspection PyBroadException
    try:
        year = request.form["year"]
        area = request.form["area"]
        crop = request.form["crop_name"]
        rainfall = request.form["rain"]
        state = request.form["state"]
        season =request.form["season"]

        features_dict[state]=1
        features_dict[crop]=1
        features_dict[season]=1

        output = model.predict([[year, area, rainfall, features_dict["ap"], features_dict["bihar"],
                                 features_dict["chattisgarh"], features_dict["hp"], features_dict["jk"],
                                 features_dict["jharkhand"], features_dict["kerala"], features_dict["odisha"],
                                 features_dict["punjab"],
                                 features_dict["tn"], features_dict["up"], features_dict["uk"],
                                 features_dict["kharif"], features_dict["rabi"],
                                 features_dict["summer"], features_dict["wholeyear"],
                                 features_dict["winter"], features_dict["drychillies"],
                                 features_dict["gram"], features_dict["groundnut"], features_dict["maize"],
                                 features_dict["masoor"], features_dict["moong"], features_dict["onion"],
                                 features_dict["peas"],
                                 features_dict["potato"], features_dict["ragi"], features_dict["rapeseed"],
                                 features_dict["rice"],
                                 features_dict["sesamum"], features_dict["urad"], features_dict["wheat"]]])
        output = round(output[0], 2)

        # output = features_dict
        return render_template("index.html", output="The expected yield is : " + format(output) + " tons")

    except:
        return render_template("index.html", output="Please provide valid inputs:")


if __name__ == "__main__":
    app.run(debug=True)
