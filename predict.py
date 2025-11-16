import joblib
import pandas as pd

area =float(input("Enter area in square feet: "))
bedrooms =float(input("Enter bedrooms  in home: "))              
age =float(input("Enter age: "))

model=joblib.load("model.joblib")  
scaler=joblib.load("scaler.joblib")
features_names=joblib.load("features_name.joblib")

input_data ={
    'Area': area,
    'Bedrooms' : bedrooms,
    'Age' : age
}

X_new = pd.DataFrame([input_data], columns=features_names)  
X_new_scaled = scaler.transform(X_new)

predicted_price = model.predict(X_new_scaled)   
print(f"Predicted Price: ${predicted_price[0]:,.2f}")