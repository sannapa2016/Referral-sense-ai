from sklearn.ensemble import RandomForestClassifier

def train_referral_model(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def rank_physicians(model, X_new):
    # Get the probability of being a 'High Referral' target
    probabilities = model.predict_proba(X_new)[:, 1]
    return probabilities
