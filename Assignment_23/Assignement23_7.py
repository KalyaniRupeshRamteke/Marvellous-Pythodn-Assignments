
import pandas as pd 
import DataFrameModule
import matplotlib.pyplot as plt
 

def barDiagramForStudentVsTotal():

    df = DataFrameModule.getDataFrame()
    print("Get Sorted data:")

    df.insert(4, 'Total', df['Math'] + df['Science'] + df['English']) # index 1, column name, values

    plt.bar(df['Name'], df['Total'])

    plt.xlabel('Name')
    plt.ylabel('Total')
    plt.title('Student Bar Plot')

    plt.show()

def main():
    barDiagramForStudentVsTotal()

if __name__ == "__main__":
    main()