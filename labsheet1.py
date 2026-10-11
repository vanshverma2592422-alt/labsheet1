from pathlib import Path

content =  MCA III Semester - Lab Sheet 01
# Python Libraries, Jupyter Notebook, and Dataset Loading
# All 35 Programs - Source Code Only (No Outputs)

# ------------------------------------------------------------
# Program 1: Verify Python Version
#------------------------------------------------------------
import sys
print(sys.version)
print(sys.version_info)


# ------------------------------------------------------------
# Program 2: Install and Launch Jupyter Notebook
# Run these commands in the terminal, not in a Python script:
# pip install notebook
# jupyter notebook
# ------------------------------------------------------------


# ------------------------------------------------------------
# Program 3: Install NumPy and Verify Installation
# Terminal command: pip install numpy
# ------------------------------------------------------------
import numpy as np
print(np.__version__)


# ------------------------------------------------------------
# Program 4: Install Pandas and Verify Installation
# Terminal command: pip install pandas
# ------------------------------------------------------------
import pandas as pd
print(pd.__version__)


# ------------------------------------------------------------
# Program 5: Install Matplotlib and Create a Line Plot
# Terminal command: pip install matplotlib
# ------------------------------------------------------------
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.plot(x, y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Line Plot")
plt.show()


# ------------------------------------------------------------
# Program 6: Install Seaborn and Generate a Statistical Plot
# Terminal command: pip install seaborn
# ------------------------------------------------------------
import seaborn as sns
import matplotlib.pyplot as plt

data = [10, 20, 15, 25, 30, 35, 20, 15]
sns.histplot(data, kde=True)
plt.title("Statistical Plot")
plt.show()


# ------------------------------------------------------------
# Program 7: Install Scikit-learn and Verify Its Version
# Terminal command: pip install scikit-learn
# ------------------------------------------------------------
import sklearn
print(sklearn.__version__)


# ------------------------------------------------------------
# Program 8: First Python Program in Jupyter Notebook
# ------------------------------------------------------------
message = "Hello, Python!"
print(message)


# ------------------------------------------------------------
# Program 9: Python Script Using VS Code or PyCharm
# ------------------------------------------------------------
def first_python_script():
    message = "My First Python Script"
    print(message)


if __name__ == "__main__":
    first_python_script()


# ------------------------------------------------------------
# Program 10: Create a Virtual Environment and Install Libraries
# Run these commands in the terminal, not in a Python script:
# Windows:
#   python -m venv myenv
#   myenv\Scripts\activate
#   pip install numpy pandas matplotlib seaborn scikit-learn
# macOS/Linux:
#   python3 -m venv myenv
#   source myenv/bin/activate
#   pip install numpy pandas matplotlib seaborn scikit-learn
# ------------------------------------------------------------


# ------------------------------------------------------------
# Program 11: Load a CSV Dataset Using Pandas
# Requires data.csv in the current working directory.
# ------------------------------------------------------------
df = pd.read_csv("data.csv")
print(df)


# ------------------------------------------------------------
# Program 12: Display the First Five Records
# ------------------------------------------------------------
df = pd.read_csv("data.csv")
print(df.head())


# ------------------------------------------------------------
# Program 13: Display the Last Five Records
# ------------------------------------------------------------
df = pd.read_csv("data.csv")
print(df.tail())


# ------------------------------------------------------------
# Program 14: Find Total Number of Rows and Columns
# ------------------------------------------------------------
df = pd.read_csv("data.csv")
print(df.shape)


# ------------------------------------------------------------
# Program 15: Display Names of All Columns
# ------------------------------------------------------------
df = pd.read_csv("data.csv")
print(df.columns)


# ------------------------------------------------------------
# Program 16: Check Data Types of All Columns
# ------------------------------------------------------------
df = pd.read_csv("data.csv")
print(df.dtypes)


# ------------------------------------------------------------
# Program 17: Descriptive Statistics of Numerical Features
# ------------------------------------------------------------
df = pd.read_csv("data.csv")
print(df.describe())


# ------------------------------------------------------------
# Program 18: Display Dataset Information
# ------------------------------------------------------------
df = pd.read_csv("data.csv")
df.info()


# ------------------------------------------------------------
# Program 19: Identify Missing Values
# ------------------------------------------------------------
df = pd.read_csv("data.csv")
print(df.isnull())


# ------------------------------------------------------------
# Program 20: Count Missing Values in Each Column
# ------------------------------------------------------------
df = pd.read_csv("data.csv")
print(df.isnull().sum())


# ------------------------------------------------------------
# Program 21: Display Unique Values in a Selected Column
# Requires a column named 'Name'.
# ------------------------------------------------------------
df = pd.read_csv("data.csv")
print(df["Name"].unique())


# ------------------------------------------------------------
# Program 22: Count Frequency of Unique Values in a Column
# Requires a column named 'Name'.
# ------------------------------------------------------------
df = pd.read_csv("data.csv")
print(df["Name"].value_counts())


# ------------------------------------------------------------
# Program 23: Rename One or More Columns
# Requires columns named 'Name' and 'Age'.
# ------------------------------------------------------------
df = pd.read_csv("data.csv")
df.rename(
    columns={"Name": "Student_Name", "Age": "Student_Age"},
    inplace=True
)


# ------------------------------------------------------------
# Program 24: Select Rows and Columns Using loc[]
# Requires columns named 'Name' and 'Age'.
# ------------------------------------------------------------
df = pd.read_csv("data.csv")
selected_data = df.loc[0:4, ["Name", "Age"]]
print(selected_data)


# ------------------------------------------------------------
# Program 25: Select Rows and Columns Using iloc[]
# ------------------------------------------------------------
df = pd.read_csv("data.csv")
selected_data = df.iloc[0:5, 0:2]
print(selected_data)


# ------------------------------------------------------------
# Program 26: Filter Records Based on a Condition
# Requires a numeric column named 'Age'.
# ------------------------------------------------------------
df = pd.read_csv("data.csv")
filtered_data = df[df["Age"] > 18]
print(filtered_data)


# ------------------------------------------------------------
# Program 27: Sort Dataset Using One or More Columns
# Requires a column named 'Age'.
# ------------------------------------------------------------
df = pd.read_csv("data.csv")
sorted_data = df.sort_values(by=["Age"], ascending=True)
print(sorted_data)


# ------------------------------------------------------------
# Program 28: Add a New Column to the Dataset
# Requires a numeric column named 'Age'.
# ------------------------------------------------------------
df = pd.read_csv("data.csv")
df["Age_Next_Year"] = df["Age"] + 1


# ------------------------------------------------------------
# Program 29: Delete an Existing Column
# Requires a column named 'Age'.
# ------------------------------------------------------------
df = pd.read_csv("data.csv")
df.drop(columns=["Age"], inplace=True)


# ------------------------------------------------------------
# Program 30: Remove Duplicate Records
# ------------------------------------------------------------
df = pd.read_csv("data.csv")
df.drop_duplicates(inplace=True)


# ------------------------------------------------------------
# Program 31: Save Modified Dataset as a New CSV File
# ------------------------------------------------------------
df = pd.read_csv("data.csv")
df.to_csv("modified_data.csv", index=False)


# ------------------------------------------------------------
# Program 32: Load a Dataset from Scikit-learn
# ------------------------------------------------------------
from sklearn.datasets import load_iris

iris = load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)


# ------------------------------------------------------------
# Program 33: Create a Histogram Using Matplotlib
# Requires a numeric column named 'Age'.
# ------------------------------------------------------------
df = pd.read_csv("data.csv")
plt.hist(df["Age"], bins=10)
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Histogram of Age")
plt.show()


# ------------------------------------------------------------
# Program 34: Create a Scatter Plot Between Two Variables
# Requires numeric columns named 'Age' and 'Marks'.
# ------------------------------------------------------------
df = pd.read_csv("data.csv")
plt.scatter(df["Age"], df["Marks"])
plt.xlabel("Age")
plt.ylabel("Marks")
plt.title("Age vs Marks")
plt.show()


# ------------------------------------------------------------
# Program 35: Correlation Matrix and Heatmap
# ------------------------------------------------------------
df = pd.read_csv("data.csv")
correlation_matrix = df.corr(numeric_only=True)

sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix Heatmap")
plt.show()
