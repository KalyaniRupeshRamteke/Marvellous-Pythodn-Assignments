
import pandas as pd 
import DataFrameModule

def sortTotalMarks():

    df = DataFrameModule.getDataFrame()
    print("Get Sorted data:")

    df.insert(4, 'Total', df['Math'] + df['Science'] + df['English']) # index 1, column name, values

    sorted_df = df.sort_values(by=['Total'], ascending=False)
    print(sorted_df)


def main():
    sortTotalMarks()

if __name__ == "__main__":
    main()