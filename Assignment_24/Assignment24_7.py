import pandas as pd
import numpy as np
def main():
    
    data = {
        'Name' : ['Amit','Sagar','Pooja'],
        'Math' : [85,90,78],
        'Science' : [92,88,80],
        'English' : [75,85,82]
    }

    df = pd.DataFrame(data)
    df.insert(4,'Total',df['Math']+df['Science']+df['English'])

    conditional_series = np.where(df['Total'] >= 250, 'Pass', 'Fail')
    df.insert(5,'Status',conditional_series)

    df.to_csv('studantMarkData.csv', header=True, index=False)



if __name__ == "__main__":
    main()