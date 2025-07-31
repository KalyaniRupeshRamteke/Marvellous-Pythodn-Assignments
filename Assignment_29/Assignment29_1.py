import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,precision_score,recall_score,f1_score

from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import ConfusionMatrixDisplay






def diabeticPredictor(dataset):
    
    #load data
    df = pd.read_csv(dataset)

    #Display first 5 rows
    print("First five rows are:")
    print(df.head())

    #Display info of coloums
    print("Display information of column")
    print(df.info)

    #display data type of coloums
    print("Data Types ofcoloumn")
    print(df.dtypes)

    #check is any null values
    print("Check for null values")
    print(df.isnull().any().any())


    print("Display basic statics of data")
    print(df.describe())

    #display the distibution of outcome col
    df['Outcome'].hist(bins=30)  # Adjust 'bins' as needed
    plt.title('Distribution of Target Variable')
    plt.xlabel('Target Variable Value')
    plt.ylabel('Frequency')
    plt.show()

    #boxplot
    plt.boxplot(df)
    plt.title('Basic Boxplot')
    plt.ylabel('Values')
    plt.show()

    #pairplot
    sns.pairplot(df)
    plt.suptitle("Pairplot of independant Features", y = 1.02)
    plt.show()


    # split data set in x & Y
    x = df.drop(columns=['Outcome'])
    y = df['Outcome']

    #replace 0 values with Nan4
    x.replace(0, np.nan,inplace=True)
    #get mean value
    mean_values = x.mean()
    #replace NAN value with mean
    x.fillna(mean_values,inplace=True)

    #print(df.head())
    #print(x)

    #Feature scaling using StandardScaler
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df)


    print("\nScaled Data (Mean=0, Std Dev=1 for each feature):")    
    print(scaled_data)

    # calculated mean and standard deviation
    print("\nMean of each feature:", scaler.mean_)
    print("Standard Deviation of each feature:", np.sqrt(scaler.var_))

    # 2. Split data into training and testing sets
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

    #Train data using logistic regression
    model = LogisticRegression()
    model.fit(x_train,y_train)

    y_predict = model.predict(x_test)

    accuracy = accuracy_score(y_test,y_predict) * 100
    print(f"Model Accuracy for logisti00regreesion: {accuracy:.2f}")

    #confusion matrix
    cm = confusion_matrix(y_test, y_predict)
    print(f"Model confusion matrix for logistic regreesion:")
    print(cm)

    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot(cmap=plt.cm.Blues) # Customize colormap
    plt.title('Logetstic regression Confusion Matrix')
    plt.xlabel("Predicted values")
    plt.ylabel("Actual Values")
    plt.show()

    # Calculate precision
    precision = precision_score(y_test, y_predict, average="weighted")*100 # 'weighted' for multi-class
    print(f"Logetstic regression Precision: {precision:.2f}")

    #Calulate recall
    recall = recall_score(y_test, y_predict)*100
    print(f"Logetstic regression Recall: {recall:.4f}")

    #calculate F1 score
    f1Scr = f1_score(y_test, y_predict, average='weighted')*100 # or 'binary', 'macro', 'micro'
    print(f"Logetstic regression F1 score: {f1Scr:.4f}")

    LT_y_predict = y_predict

    #Train data using KNN
    KNNModel = KNeighborsClassifier(n_neighbors=3)
    KNNModel.fit(x_train,y_train)

    y_predict = KNNModel.predict(x_test)

    accuracy = accuracy_score(y_test,y_predict) * 100
    print(f"Model Accuracy for KNN classifier: {accuracy:.2f}")

    #confusion matrix
    cm = confusion_matrix(y_test, y_predict)
    print(f"Model confusion matrix for KNN classifier:")
    print(cm)

    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot(cmap=plt.cm.Blues) # Customize colormap
    plt.title('KNN Confusion Matrix')
    plt.xlabel("Predicted values")
    plt.ylabel("Actual Values")
    plt.show()

    # Calculate precision
    precision = precision_score(y_test, y_predict, average="weighted")*100 # 'weighted' for multi-class
    print(f"KNN Precision: {precision:.2f}")

    #Calulate recall
    recall_knn = recall_score(y_test, y_predict)*100
    print(f"KNN Recall: {recall_knn:.4f}")

    #calculate F1 score
    f1Scr = f1_score(y_test, y_predict, average='weighted')*100 # or 'binary', 'macro', 'micro'
    print(f"KNN F1 score: {f1Scr:.4f}")

    KNN_y_predict = y_predict


    #decision tree classifier
    decTreeModel = DecisionTreeClassifier()
    decTreeModel.fit(x_train,y_train)

    y_predict = decTreeModel.predict(x_test)

    accuracy = accuracy_score(y_test,y_predict)*100
    print(f"Model Accuracy for Decision tree classifier: {accuracy:.2f}")

    #confusion matrix
    cm = confusion_matrix(y_test, y_predict)
    print(f"Model confusion matrix for Decision Tree classifier:")
    print(cm)

    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot(cmap=plt.cm.Blues) # Customize colormap
    plt.title('Decision Tree Classifier Confusion Matrix')
    plt.xlabel("Predicted values")
    plt.ylabel("Actual Values")
    plt.show()

    # Calculate precision
    precision = precision_score(y_test, y_predict, average="weighted") *100# 'weighted' for multi-class
    print(f"Decision Tree Classifier Precision: {precision:.2f}")

    #Calulate recall    
    recall_dt = recall_score(y_test, y_predict)*100
    print(f"Decision Tree Recall: {recall_dt:.4f}")

    #calculate F1 score
    f1Scr = f1_score(y_test, y_predict, average='weighted')*100 # or 'binary', 'macro', 'micro'
    print(f"Decision Tree F1 score: {f1Scr:.4f}")

    DT_y_predict = y_predict

    # Define a mapping dictionary
    mapping = {0: 'Diabetic', 1: 'Non Diabetic'}

    # Apply the mapping to convert numeric predictions to strings
    LR_alg1_str = [mapping[pred] for pred in LT_y_predict]
    KNN_alg2_str = [mapping[pred] for pred in KNN_y_predict]
    DT_alg3_str = [mapping[pred] for pred in DT_y_predict]


    data = {
        'Sr.No': range(len(DT_y_predict)), # Or your actual IDs
        'Linear Regression': LR_alg1_str,
        'KNN': KNN_alg2_str,
        'Decision Tree': DT_alg3_str
    }

    df = pd.DataFrame(data)
     # Save the DataFrame to a CSV file
    df.to_csv('predictions_All_Algorithm.csv', index=False)



def main():
    diabeticPredictor("diabetes.csv")

if __name__ == "__main__":
    main()