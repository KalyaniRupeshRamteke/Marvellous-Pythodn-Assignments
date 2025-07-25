import pandas as pd
from sklearn.model_selection import train_test_split

def main():

    data = {
        'Salary':[50000,60000,80000,65000,45000],
        'Age': [25,30,45,35,22],
        'Purchased':[1,0,1,0,1]
        }
    df = pd.DataFrame(data)
    X = df.drop('Purchased', axis=1) # Features
    y = df['Purchased']             # Target variable

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print("X Train data:")
    print(X_train)
    print("Y Train data:")
    print(y_train)

    print("X test data:")
    print(X_test)
    print("Y test data:")
    print(y_test)

if __name__ == "__main__":
    main()