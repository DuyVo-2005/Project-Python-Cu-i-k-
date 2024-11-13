import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("company_sales_data.csv")
profitlist = df["total_profit"].tolist()
monthlist = df["month_number"].tolist()

print(profitlist)
print(monthlist)
plt.xlabel("Month number")
plt.ylabel("profit")
plt.plot(monthlist,profitlist)
plt.title("Company profit per month")
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12])
plt.yticks([100000,200000,300000,400000,500000])
plt.show()