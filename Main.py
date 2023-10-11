import  pandas as pd
import matplotlib.pyplot as plt
Data = pd.read_csv("car data.csv")
Data = Data.drop(["Owner"], axis=1)
Y = Data.iloc[:,2].values
from sklearn.preprocessing import LabelEncoder
Le = LabelEncoder()
Data["Car_Name"]=Le.fit_transform(Data["Car_Name"])
Data["Transmission"]=Le.fit_transform(Data["Transmission"])
Data["Selling_type"]=Le.fit_transform(Data["Selling_type"])
Data["Fuel_Type"] =Le.fit_transform(Data["Fuel_Type"])
X = Data.drop(["Selling_Price"] , axis=1).values

from sklearn.model_selection import train_test_split
X_train , X_test , Y_train , Y_test = train_test_split(X, Y , test_size=0.3 , random_state=42)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
model = regressor.fit(X_train,Y_train)

Y_predict  = model.predict(X_test)

Accuracy = model.score(X_test, Y_test)

import matplotlib.pyplot as plt
plt.scatter(Data["Selling_Price"] , Data["Fuel_Type"] , color = "Blue")
plt.scatter(Data["Selling_Price"] , Data["Car_Name"] , color = "Red")
plt.title("Selling Prize Comparison with Feul Type & CarName ")
plt.show()