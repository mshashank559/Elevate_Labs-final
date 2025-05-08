import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(df):
    # Drop non-feature columns
    df = df.drop(['EmployeeNumber'], axis=1, errors='ignore')
    
    # Encode categoricals
    df = pd.get_dummies(df, drop_first=True)
    
    # Scale numerical features
    scaler = StandardScaler()
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])
    
    return df
