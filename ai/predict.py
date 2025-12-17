import joblib

model = joblib.load('models/completion_model.pkl')

def predict_completion(time_spent: float, score: float):
    prediction = model.predict([[time_spent, score]])[0]
    
    if prediction == 1:
         return "LIKELY TO COMPLETE", "LOW"
    else:
        return "NOT LIKELY", "HIGH"
