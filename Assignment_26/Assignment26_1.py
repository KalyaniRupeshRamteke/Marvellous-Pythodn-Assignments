import pandas as pd

from sklearn.model_selection  import train_test_split
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import accuracy_score

from sklearn.preprocessing import LabelEncoder



def playPredictor(dataset):

    #step 1 : get Data
    df = pd.read_csv(dataset)

    df.drop(columns=['Unnamed: 0'], axis=1, inplace=True)

    #step 2 : encoding data
    le = LabelEncoder()

    #le.fit_transform(df[['Whether'],['Temperature']])
    df['Whether']= le.fit_transform(df['Whether'])
    df['Temperature']= le.fit_transform(df['Temperature'])
    print(df)

    # train data
    x = df.drop(columns=['Play'])
    y = df['Play']

    x_train , x_test ,y_train , y_test = train_test_split(x,y,test_size=0.2,random_state=42)

    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(x_train,y_train)
    y_predict = model.predict(x_test)

    new_data_point = [[0 ,	1]] # Example features for prediction play
    predicted_class = model.predict(new_data_point)
    print(f"Predicted class for the new data point: {predicted_class}")


    new_data_point = [[2 ,	1]] # Example features for a new 
    predicted_class = model.predict(new_data_point)
    print(f"Predicted class for the new data point: {predicted_class}")

    new_data_point = [[1 ,	0]] # Example features for a new flower
    print(f"Predicted class for the new data point: {predicted_class}")

    accuracy = accuracy_score(y_test,y_predict)*100
    print(accuracy)


    for i in range(2,8):

        model = KNeighborsClassifier(n_neighbors=i)
        model.fit(x_train,y_train)
        y_predict = model.predict(x_test)
        accuracy = accuracy_score(y_test,y_predict)*100
        print(accuracy)


def main():
    playPredictor("PlayPredictor.csv")
    

if __name__ == "__main__":
    main()