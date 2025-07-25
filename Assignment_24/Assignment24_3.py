import pandas as pd

def main():

    data = {
        'Name' : ['Amit','Sagar','Pooja'],
        'Math' : [85,90,78],
        'Science' : [92,88,80],
        'English' : [75,85,82]
    }

    df = pd.DataFrame(data)
    df.insert(4,'Gender',['Male','Male','Female'])
    
    grouped_data = df.groupby('Gender')
    # This creates a GroupBy object. To see results, you need to apply an aggregation.
    #print(grouped_data)
    for x, y in grouped_data:
        print(f'{x}\n{y}\n')
    
    print("Average Data of group by values")
    avg_data = grouped_data[['Math','Science','English']].mean()
    # This creates a GroupBy object. To see results, you need to apply an aggregation.
    print(avg_data)
    #for x in grouped_data:
        #print(f'{x}')
    


if __name__ == "__main__":
    main()