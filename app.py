from flask import Flask, render_template, request
import pandas as pd
import joblib

app=Flask(__name__)

MODEL_PATH="model.joblib"
SCALER_PATH="scaler.joblib"
FEATS_PATH="features_name.joblib"

model=joblib.load(MODEL_PATH)
scaler=joblib.load(SCALER_PATH)
feature_names=joblib.load(FEATS_PATH)

def predict_price(payload):
    row=pd.DataFrame([payload])[feature_names]
    row_scaled=scaler.transform(row)
    return float(model.predict(row_scaled)[0])


@app.route("/",methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict():
    try:
        area=float(request.form.get("Area","").strip())
        bedrooms=int(request.form.get("Bedrooms","").strip())
        age=int(request.form.get("Age","").strip())
        
        payload={"Area":area,"Bedrooms":bedrooms,"Age":age}
        
        yhat=predict_price(payload)
        
        return render_template(
            "index.html",
            result=f"{yhat:,.2f}",
            last_input=payload,
            unit_label="lakhs"
        )
    except Exception as e:
        return render_template("index.html",error=str(e)),400
    
if __name__=="__main__":
    
    app.run(host="0.0.0.0", port=5000, debug=False)