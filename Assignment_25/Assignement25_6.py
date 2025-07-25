import pandas as pd 

def main():

    data = {'Grade':['A+','B','A','C','B+']}
    df = pd.DataFrame(data)

    df['Grade'] = df['Grade'].map({'A+': 'Excellant', 'A': 'Very Good' ,'B+': 'Good','B':'Average','C':'Poor'}) 
    print(df)

if __name__ == "__main__":
    main()