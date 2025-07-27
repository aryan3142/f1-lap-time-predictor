from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def train_model(data):
    # Prepare features (X) and target variable (y)
    X = data[["S1", "S2", "S3", "TyreLife", "CompoundEncoded"]]
    y = data["LapTime"]  # Changed from LapTimeSec to LapTime
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train the model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Make predictions and calculate score
    y_pred = model.predict(X_test)
    score = r2_score(y_test, y_pred)
    
    return score