import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("C:/test.csv")
data_subset = data.head(1000)
missing = data_subset.isnull().sum()
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

sns.boxplot(x="Rooms", y="Square", data=data_subset, ax=axes[0])
axes[0].set_yscale("log")
axes[0].set_title("Логарифмическая шкала")

sns.histplot(data_subset['Square'], bins=30, kde=True, ax=axes[1])
axes[1].set_yscale('log')
axes[1].set_title("Гистограмма")

plt.show()

num_columns = data_subset.select_dtypes(include=[np.number]).columns
data_subset.loc[:, num_columns] = data_subset.loc[:, num_columns].fillna(data_subset.loc[:, num_columns].mean())

q_low = data_subset["Square"].quantile(0.01)
q_high = data_subset["Square"].quantile(0.99)
data_subset = data_subset[(data_subset["Square"] > q_low) & (data_subset["Square"] < q_high)]

room_counts = data_subset["Rooms"].value_counts()

pivot_table = pd.pivot_table(data_subset, values="Square", index="DistrictId", columns="Rooms", aggfunc="count", fill_value=0)
data_subset.to_csv('C:/LOVETS.csv', index=False)

