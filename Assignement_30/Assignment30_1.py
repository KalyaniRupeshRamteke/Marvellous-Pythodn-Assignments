import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report,roc_auc_score,roc_curve


from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import ConfusionMatrixDisplay

import matplotlib.pyplot as plt







def bankDepositSubcribrPrediction(dataset):

    #make header in csv
    df = pd.read_csv(dataset, sep=';', header=0)

    #print(df)

     # split data set in x & Y
    x1 = df.drop(columns=['y'])
    y1 = df['y']

    #replace unknown values with Nan
    x1.replace('unknown', np.nan,inplace=True)
    print(x1)
    #get mean value
    mean_values = df.fillna(df.mean(numeric_only=True))
    #replace NAN value with mean
    x1.fillna(mean_values,inplace=True)

    print("Display basic statics of data")
    print(df.describe())

    # Apply LabelEncoder to each column and store in the dictionary
    for col in df.columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        #print(df[col])

    #Feature scaling using StandardScaler
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df)


    print("\nScaled Data (Mean=0, Std Dev=1 for each feature):")    
    print(scaled_data)


     # split data set in x & Y
    x = df.drop(columns=['y'])
    y = df['y']

    # 2. Split data into training and testing sets
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)


    #Train data using logistic regression
    model = LogisticRegression()
    model.fit(x_train,y_train)

    LT_y_predict = model.predict(x_test)

    accuracy = accuracy_score(y_test,LT_y_predict) * 100
    print(f"Model Accuracy for logisti00regreesion: {accuracy:.2f}")

    #confusion matrix
    cm = confusion_matrix(y_test, LT_y_predict)
    print(f"Model confusion matrix for logistic regreesion:")
    print(cm)

    class_report = classification_report(y_test, LT_y_predict,target_names=['Yes','No'])
    print("Classification Report for logistic regression:")
    print(class_report)

    auc_score = roc_auc_score(y_test, LT_y_predict)
    print(f"ROC AUC Score logistic regression: {auc_score:.2f}")

    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot(cmap=plt.cm.Blues) # Customize colormap
    plt.title('Logetstic regression Confusion Matrix')
    plt.xlabel("Predicted values")
    plt.ylabel("Actual Values")
    plt.show()

    # 5. Calculate False Positive Rate (FPR), True Positive Rate (TPR), and thresholds
    fpr, tpr, thresholds = roc_curve(y_test, LT_y_predict)


    # 7. Plot the ROC curve
    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (AUC = {auc_score:.2f})')
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--', label='logistic regression (AUC = 0.50)')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate (FPR)')
    plt.ylabel('True Positive Rate (TPR)')
    plt.title('Receiver Operating Characteristic (ROC) Curve (Logestic Regression)')
    plt.legend(loc='lower right')
    plt.grid(True)
    plt.show()




    #Train data using KNN
    KNNModel = KNeighborsClassifier(n_neighbors=3)
    KNNModel.fit(x_train,y_train)

    KNN_y_predict = KNNModel.predict(x_test)

    accuracy = accuracy_score(y_test,KNN_y_predict) * 100
    print(f"Model Accuracy for KNN classifier: {accuracy:.2f}")

    #confusion matrix
    cm = confusion_matrix(y_test, KNN_y_predict)
    print(f"Model confusion matrix for KNN classifier:")
    print(cm)

    class_report = classification_report(y_test, KNN_y_predict,target_names=['Yes','No'])
    print("Classification Report for KNN:")
    print(class_report)

    auc_score = roc_auc_score(y_test, KNN_y_predict)* 100
    print(f"ROC AUC Score logistic regression: {auc_score : .2f}")

    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot(cmap=plt.cm.Blues) # Customize colormap
    plt.title('KNN  Confusion Matrix')
    plt.xlabel("Predicted values")
    plt.ylabel("Actual Values")
    plt.show()

    # 5. Calculate False Positive Rate (FPR), True Positive Rate (TPR), and thresholds
    fpr, tpr, thresholds = roc_curve(y_test, KNN_y_predict)


    # 7. Plot the ROC curve
    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (AUC = {auc_score:.2f})')
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--', label='KNN (AUC = 0.50)')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate (FPR)')
    plt.ylabel('True Positive Rate (TPR)')
    plt.title('Receiver Operating Characteristic (ROC) Curve (KNN)')
    plt.legend(loc='lower right')
    plt.grid(True)
    plt.show()



    #Train data using Random Forest 
    classifier = RandomForestClassifier(n_estimators=100, random_state=42)

    # 5. Train the classifier
    classifier.fit(x_train, y_train)

    # 6. Make predictions on the test set
    rf_pred = classifier.predict(x_test)

    # 7. Evaluate the model
    accuracy = accuracy_score(y_test, rf_pred)*100
    print(f"Model Accuracy for Random forest classifier: {accuracy:.2f}")


    #confusion matrix
    cm = confusion_matrix(y_test, rf_pred)
    print(f"Model confusion matrix for Random forest classifier:")
    print(cm)

    class_report = classification_report(y_test, rf_pred,target_names=['Yes','No'])
    print("Classification Report for Random forest:")
    print(class_report)

    auc_score = roc_auc_score(y_test, rf_pred) * 100
    print(f"ROC AUC Score logistic regression: {auc_score:.2f}")

    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot(cmap=plt.cm.Blues) # Customize colormap
    plt.title('Random forest  Confusion Matrix')
    plt.xlabel("Predicted values")
    plt.ylabel("Actual Values")
    plt.show()

    # 5. Calculate False Positive Rate (FPR), True Positive Rate (TPR), and thresholds
    fpr, tpr, thresholds = roc_curve(y_test, rf_pred)


    # 7. Plot the ROC curve
    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (AUC = {auc_score:.2f})')
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--', label='Random forest (AUC = 0.50)')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate (FPR)')
    plt.ylabel('True Positive Rate (TPR)')
    plt.title('Receiver Operating Characteristic (ROC) Curve (Random forest)')
    plt.legend(loc='lower right')
    plt.grid(True)
    plt.show()


def main():

    bankDepositSubcribrPrediction('bank-full.csv')

if __name__ == "__main__":
    main()