import pandas as pd

def main():

    data = {
        'Name' : ['Amit','Sagar','Pooja'],
        'Math' : [85,90,78],
        'Science' : [92,88,80],
        'English' : [75,85,82]
    }

    df = pd.DataFrame(data)
    df['normalized_value'] = (df['Math'] - df['Math'].min()) / (df['Math'].max() - df['Math'].min())
    #normalize function
    #(x-xmin)/(xMax-xMin)
    #(85-78)/(90-78) = 7/12 = 0.58333
    #(90-78)/(90-78) = 12/12 =1.00000
    #(78-78)/(90-78) = 0/12 = 0.00000
    print(df['normalized_value'])

if __name__ == "__main__":
    main()