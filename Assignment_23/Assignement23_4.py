
import pandas as pd 
import DataFrameModule

def getMaxScoreInSci():

    df = DataFrameModule.getDataFrame()
    print("Get student name who has more score than:")

    filtered_df = df.loc[df['Science'] > 85]
    print(filtered_df)

    print(df[df['Science']>85])


def main():
    getMaxScoreInSci()

if __name__ == "__main__":
    main()