
import pandas as pd 
import DataFrameModule
import matplotlib.pyplot as plt
import numpy as np

 

def barDiagramForStudentVsTotal():

    df = DataFrameModule.getDataFrame()
    #print("Get Sorted data:")

    #df.insert(4, 'Total', df['Math'] + df['Science'] + df['English']) # index 1, column name, values

    x = np.array(['Math', 'Science', 'English'])
    marks = df[df['Name'] == 'Amit'][['Math','Science','English']].values.flatten()

    #print(marks)

    plt.plot(x, marks, marker='o')

    #plt.bar(df['Name'], df['Total'])

    plt.xlabel('Subject')
    plt.ylabel('Marks')
    plt.title('Amit line Plot')
    plt.grid(True)

    plt.show()

def main():
    barDiagramForStudentVsTotal()

if __name__ == "__main__":
    main()