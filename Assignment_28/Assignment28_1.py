
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix



def winePredictorForData(dataset):

    #load data
    df = pd.read_csv(dataset)

    #
    x = df.drop(columns=['Class'])
    y= df['Class']

    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(x_train,y_train)
    y_predict = model.predict(x_test)

    accuracy = accuracy_score(y_test,y_predict)*100

    print("The model accuracy is:",accuracy)


def main():
    winePredictorForData("WinePredictor.csv")

if __name__ == "__main__":
    main()