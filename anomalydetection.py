#importing modules needed
import numpy as np
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

#read file
data_file = 'currency_exchange_rates.csv'
data_frame = pd.read_csv(data_file)

#get the features (in this case: currencies that we care about)
euros = np.array(data_frame.iloc[1:,2])
#jpy = topFew.iloc[1:,3]
label = np.array(data_frame.iloc[1:,-1])

#calling the K-nearest neighbors function
knn = KNeighborsClassifier(n_neighbors=3)

#Split the data population into train & test population
X_train, X_test, Y_train, Y_test = train_test_split(euros,label,train_size=0.8,random_state=3)

#Fit\train the model
knn.fit(X_train.reshape(-1,1),Y_train) #reshape because it's expecting a 2x2 (if 2 features are chosen)

#Prediction & Accuracy Score
Y_predictor = knn.predict(X_test.reshape(-1,1))
print(Y_test,Y_predictor)
acc = accuracy_score(Y_test,Y_predictor)
print("Accuracy: ",acc)

#Plotting data
plt.scatter(X_test, Y_predictor)
plt.title('Exchange Rate Anomaly Detection')
plt.xlabel('Difference in Exchange Rates')
plt.ylabel('Normal or Anomaly')
plt.show()

#If we want to trace the data, we could use a dictionary with the date being the key. 
#When Y_predictor = a certain value, we trace that back to the X_test values - trace it back to the key. 