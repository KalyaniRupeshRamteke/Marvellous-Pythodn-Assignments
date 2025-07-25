import pandas as pd
import matplotlib.pyplot as plt
def main():
    
    data = {
        'Name' : ['Amit','Sagar','Pooja'],
        'Math' : [85,90,78],
        'Science' : [92,88,80],
        'English' : [75,85,82]
    }

    df = pd.DataFrame(data)
    x = df['Name']
    y = df['Math']

    plt.hist(y,bins=100,color="skyblue",edgecolor = "black")

    plt.xlabel("Math Marks")
    plt.ylabel("Fequency")
    plt.title("Marvellous Histogram for math marks")

    plt.show()



if __name__ == "__main__":
    main()