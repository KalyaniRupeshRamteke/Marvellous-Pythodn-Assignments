import pandas as pd 

def main():

    data = {'Age':[18,22,25,30,35]}
    df = pd.DataFrame(data)

    df['normalized_value'] = (df['Age'] - df['Age'].min()) / (df['Age'].max() - df['Age'].min())

    print(df)

if __name__ == "__main__":
    main()