import pandas as pd

df = pd.read_csv("student.csv", index_col="Student_ID")
# print(df.iloc[0:5])#print first five data
print("The first five students are:\n", df.head())  # by default print first five data
print("\nThe last five students are:\n", df.tail())  # print last five data
print(
    "\nThe numbers of rows and columns are:\n", df.shape
)  # Gives numebers of rows and column
print("Names of columns are :\n", df.columns)  # gives column name
print("\nInfo of this dataframe is :\n")
print(df.info())  # Gives info of the dataframe
print(
    "\nDisplaying only Name,Math,Science,English :\n",
    df[["Name", "Math", "Science", "English"]],
)
print("\nDisplaying only Name,City,Attendance :\n", df[["Name", "City", "Attendance"]])
print(
    "\nDisplaying info of student_ID 110 :\n", df.loc[110]
)  # Displays the ddetails of student whose id is 110
print(
    "\nDisplay the first 10 students but only their name class and math :\n",
    df.loc[101:110, ["Name", "Class", "Math"]],
)
mark = df[df["Math"] >= 90]
print(
    "\nAll the student who scored more than or equal to 90 in math are :\n",
    mark[["Name", "Math", "Class"]],
)
mark1 = df[df["Science"] < 70]
print(
    "\nAll the student who scored less than 70 in science are :\n",
    mark1[["Name", "Science", "Class"]],
)
att = df[df["Attendance"] >= 90]
print(
    "\nAll the student whose attendance are more than or equal to 90  are :\n",
    att[["Name", "Attendance", "Class"]],
)
location = df[df["City"] == "Butwal"]
print(
    "\nAll the student who are from butwal are :\n",
    location[["Name", "Class"]],
)
clm = df[(df["Math"] > 80) & (df["Class"] == 12)]
print(
    "\nAll the student who are in class 12 and scored more than 80 in math are :\n",
    clm[["Name", "Math", "Class"]],
)
att1 = df[(df["Attendance"] >= 95) & (df["Gender"] == "F")]
print(
    "\nAll the student who are female and have attendance more than 95 are :\n",
    att1[["Name", "Class"]],
)
nll = df.isnull().sum()
print("\nAll the null values are :\n", nll)

a = df["Science"].mean()
b = df["English"].mean()
c = df["Attendance"].mean()
df = df.fillna(
    {"Science": a, "English": b, "Attendance": c}
)  # This will fill the gap with average value
df = df.round(2)  # This will roundup the value after decimal to 2
nll = df.isnull().sum()
print("\nAgain checking the null avlues and all the null values are :\n", nll)
print("\nThe average of Math is : \n", df["Math"].mean().__round__(2))
print("\nThe average of Science is : \n", df["Science"].mean().__round__(2))
print("\nThe average of English is : \n", df["English"].mean().__round__(2))
print("\nThe average of Attendance is :\n ", df["Attendance"].mean().__round__(2))
print("\nThe highest mark of a subject Math is :\n", df["Math"].max())
print("\nThe lowest mark of a subject Math is :\n", df["Math"].min())
print("\nThe highest mark of a subject Science is :\n", df["Science"].max())
print("\nThe lowest mark of a subject Science is :\n", df["Science"].min())
count = 0
for i in range(len(df["Name"])):
    count += 1
print("\nTotal number of students is :\n", count)
group = df.groupby("Gender")
print("\nThe average math martk scored by group of gender is :\n", group["Math"].mean())
print(
    "\nThe average math mark scored by city is :\n", df.groupby("City")["Math"].mean()
)
print(
    "\nThe average score for each subject by class is :\n",
    df.groupby("Class")[["Math", "Science", "English"]].mean().round(2),
)
ag = []
rel = []

for i in range(len(df["Name"])):
    a = df.iloc[i]["Math"]
    b = df.iloc[i]["Science"]
    c = df.iloc[i]["English"]
    avg = (a + b + c) / 3
    ag.append(avg)
df["Average"] = ag
# Average >= 80  → Excellent
# Average >= 60  → Good
# Average >= 40  → Pass
# Average < 40   → Fail
for av in ag:
    if av >= 80:
        rel.append("Excellent")
    elif av >= 60:
        rel.append("Good")
    elif av >= 40:
        rel.append("Pass")
    else:
        rel.append("Fail")

df["Result"] = rel
df = df.sort_values("Average", ascending=False)
print("\nThe top 5 students based on Average are :\n", df.head(4).round(2))
large = df["Average"].max()
high = df[df["Average"] == large]
print("\nThe student with the highest average score is :\n", high[["Name", "Average"]])
print(df)
