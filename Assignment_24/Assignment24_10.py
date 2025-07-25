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
    x = df['English']

    plt.boxplot(x)
    plt.title('Box Plot of English mark Data Distribution and Outliers')
    plt.ylabel('Value')
    plt.show()




if __name__ == "__main__":
    main()