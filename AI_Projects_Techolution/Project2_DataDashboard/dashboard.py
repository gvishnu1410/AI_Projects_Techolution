import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data.csv")

# Show summary
print("Total Sales:", df["Sales"].sum())
print("Highest Sales:", df["Sales"].max())
print("Lowest Sales:", df["Sales"].min())

# Create chart
plt.bar(df["Month"], df["Sales"])

plt.title("Monthly Sales Dashboard")
plt.xlabel("Month")
plt.ylabel("Sales")

# Save chart
plt.savefig("sales_chart.png")

# Show chart
plt.show()