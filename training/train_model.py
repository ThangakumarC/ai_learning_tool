import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

data = pd.read_csv('data/training_data.csv')

x = data[["time_spent", "score"]]
y = data["completed"]

model = LogisticRegression()
model.fit(x, y)

joblib.dump(model, 'models/completion_model.pkl')

print("Model Trained and saved...")