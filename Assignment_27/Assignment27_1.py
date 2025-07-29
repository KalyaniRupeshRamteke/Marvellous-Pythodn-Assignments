import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import  LinearRegression
import matplotlib.pyplot as plt




def salePredictor(dataSet):
    df = pd.read_csv(dataSet)

    print("Data is as follows:")
    print(df.head())

    df.drop(columns=['Unnamed: 0'], axis=1, inplace=True)

    print("After removing unwanted coloumns")
    print(df.head())

    x = df.drop(columns=['sales'])
    y = df['sales']

    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.5,random_state=42)

    model = LinearRegression()
    model.fit(x_train,y_train)
    y_predict = model.predict(x_test)

    #plt.scatter(x, y, label='Actual')
    plt.scatter(y_test,y_predict,color='blue',label='Predicted')
    plt.xlabel("Actual sales")
    plt.ylabel("Predicted sale")
    plt.title("Linear Regression: Actual vs. Predicted")
    plt.legend()
    plt.grid(True)
    plt.show()





def main():
    salePredictor("Advertising.csv")

if __name__ == "__main__":
    main()