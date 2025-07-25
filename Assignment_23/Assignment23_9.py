
import pandas as pd
import numpy as np

def getMaxScoreInSci():

    data = {
        'Name' : ['Amit','Sagar','Pooja'],
        'Math' : [np.nan,76,88],
        'English' :[80,np.nan,90]
    }
    
    df = pd.DataFrame(data)
    print(df)
    df.fillna(df.mean(numeric_only = True),inplace=True)
    print(df)

def main():
    getMaxScoreInSci()

if __name__ == "__main__":
    main()