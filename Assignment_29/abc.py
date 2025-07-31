import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

    # Sample DataFrame
data = {'Category': np.random.choice(['A', 'B', 'C'], 100),
            'Value': np.random.randn(100)}
df = pd.DataFrame(data)

df.hist(column='Value', by='Category', bins=10, figsize=(10, 5))
plt.suptitle('Distribution of Value by Category')
plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # Adjust layout to prevent title overlap
plt.show()   # ... (df from previous example)

df[df['Category'] == 'A']['Value'].plot.kde(label='Category A')
df[df['Category'] == 'B']['Value'].plot.kde(label='Category B')
df[df['Category'] == 'C']['Value'].plot.kde(label='Category C')
plt.title('KDE of Value by Category')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()
plt.show()