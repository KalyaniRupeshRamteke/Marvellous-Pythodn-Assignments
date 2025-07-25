import pandas as pd 
from sklearn.preprocessing import LabelEncoder

def main():

    data = {'City':['Pune','Mumbai','Delhi','Pune','Delhi']}
    df = pd.DataFrame(data)
    le = LabelEncoder()
    df['Category_encoded'] = le.fit_transform(df['City'])
    print("Data after label encoding")
    print(df)

if __name__ == "__main__":
    main()