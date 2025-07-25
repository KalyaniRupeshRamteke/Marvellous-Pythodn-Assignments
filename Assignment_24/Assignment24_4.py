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

    subject = ['Math', 'Science', 'English']
    marks = df[df['Name'] == 'Sagar'][['Math','Science','English']].values.flatten()

    def make_autopct(values):
        def my_autopct(pct):
            total = sum(values)
            val = int(round(pct * total / 100.0))
            return '{v:d}'.format(v=val)
        return my_autopct


    plt.pie(marks, labels=subject ,autopct=make_autopct(marks))

    plt.title('Marks of Sagar')
    plt.axis('equal')
    plt.show()

if __name__ == "__main__":
    main()