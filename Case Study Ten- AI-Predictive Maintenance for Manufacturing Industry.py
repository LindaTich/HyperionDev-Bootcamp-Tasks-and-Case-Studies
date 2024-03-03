'''Start
Create and name file in python.
Import pandas.
Import train_test_split.
Import RandomForestClassifier.
import accuracy_score.
Assume machinery_data is panda dataframe.
With sensor data.
Split data into features, target variable.
Split data into training and testing sets.
Create random forest classifier.
Train the classifier.
Make predictions on testing set.
Evaluate accuracy of model.
Use advanced machine learning.
This is for predictive maintenance.
Concatenate original and additional data.
Split combined data into features, target variable.
Create new random forest classifier.
Train new classifier on combined data.
Make predictions on original test set.
Evaluating the accuarcy of the combined model.
Show additional evaluation metrics.
End'''

import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score

# I am assuming machinery_data is a Pandas Dataframe with sensor data

machinery_data = pd.DataFrame({

'Temperature': [45,50, 55, 60, 65, 70],

'Vibration_Level': [0.2, 0.5,0.8,1.2,1.5,1.8],

'Operational_Hours': [500, 600, 700, 800, 900, 1000],

'Failure_Status': [0,0,0,1,1,1] })

# 0 represents normal, 1 represents failure


# Split the data into features (X) and target variable (y)

X = machinery_data[['Temperature', 'Vibration_Level', 'Operational_Hours']]

y = machinery_data['Failure_Status']

# Splitting the data into training and testing sets

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
random_state=42)


# Created a random forest classifier

clf = RandomForestClassifier()

# Training the classifier

clf.fit(X_train, y_train)

# Making predictions on the test set
y_pred = clf.predict(X_test)

# Evaluates the accuracy of the model

accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy of the predictive maintenance model :(accuracy)")


# Advanced machine learning for predictive maintenance

from sklearn.metrics import classification_report, confusion_matrix

# I assume that additional sensor data is available fot training the model

additional_machinery_data = pd.DataFrame({
    'Temperature' : [75, 80, 85, 90, 95],
    'Vibration_Level': [2.0, 2.2, 2.5,2.8,3.0],
    'Operational_Hours': [1100, 1200, 1300, 1400, 1500],
    'Failure_Status': [1, 1, 1, 0, 0]})


# Concatenated the additional data with the original data

machinery_data = pd.concat([machinery_data, additional_machinery_data], 
ignore_index=True)

# Splitting the combined data into features (X) and target variable (y)

X_combined = machinery_data(['Temperature', 'Vibration_Level',
'Operational_Hours'])
y_combined = machinery_data['Failure_Status']

# Creating a new random forest classifier

clf_combined = RandomForestClassifier()

# Training the new classifier on the combined data

clf_combined.fit(X_combined, y_combined)

# Making predictions on the original test set

y_pred_combined = clf_combined.predict(X_test)

# Evaluating the accuracy of the combined model

accuracy_combined = accuracy_score(y_test. y_pred_combined)

# Displayed additional evaluation metrics

classification_rep = classification_report(y_test, y_pred_combined)
confusion_mat = confusion_matrix(y_test, y_pred_combined)

print(f"Accuracy of the combined predictive maintenance model:{accuracy_combined}")
print("\nClassification Report:")
print(classification_rep)
print("\nConfusion Matrix:")
print(confusion_mat)











