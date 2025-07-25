import numpy as np
def outlier_detection_IQR(data):

    Q1 = np.percentile(data,25)
    Q3 = np.percentile(data,75)

    IQR = Q3-Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    Outliers = []
    for x in data :
        if(x < lower_bound or upper_bound < x):
            Outliers.append(x)
    return Outliers,lower_bound,upper_bound


def main():

    data = {'Salary':[25000,27000,29000,31000,50000,100000]}
    
    sal_data = data['Salary']
    outliers, lower, upper = outlier_detection_IQR(sal_data)

    print(f"Lower Bound: {lower}")
    print(f"Upper Bound: {upper}")
    print(f"Detected Outliers: {outliers}")

if __name__ == "__main__":
    main()