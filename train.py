import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import joblib

df=pd.read_csv("data/property.csv")
X=df.drop(columns=["Price"])
features_name = X.columns.to_list()
print("Features used for training :", features_name)
y=df["Price"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)   
scaler=StandardScaler()

X_train_scaled=scaler.fit_transform(X_train)
X_test_scaled=scaler.transform(X_test)

model = LinearRegression()
model.fit(X_train_scaled, y_train)
joblib.dump(model, "model.joblib")  
joblib.dump(scaler,"scaler.joblib")
joblib.dump(features_name, "features_name.joblib")
