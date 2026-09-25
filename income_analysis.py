import pandas as pd

df = pd.read_csv(r"C:\Users\ZBook G3\Downloads\income-analysis\data\row\data.csv")

print(df)


print(df.head())
print(df.tail())

print(df.shape)
print(df.columns)
print(df.shape[0])

df.info()

print(df.dtypes)

summary = pd.DataFrame({
    "Data_Type": df.dtypes,
    "Missing_Values": df.isnull().sum(),
    "Missing_Ratio": df.isnull().mean() * 100,
    "Unique_Values": df.nunique()
})

print(summary)

print(df.describe())

print(df.describe(include="object"))

object_columns = df.select_dtypes(include="object").columns

print(object_columns)

for column in object_columns:
    print(column)
    print(df[column].unique())
    print(df[column].value_counts())

print(df.isnull().mean() * 100)

print(df.duplicated().sum())

df = df.drop_duplicates()

df.columns = df.columns.str.strip()

object_columns = df.select_dtypes(include="object").columns

for column in object_columns:
    if df[column].isnull().sum() > 0:
        df[column] = df[column].fillna(df[column].mode()[0])

print(df.isnull().sum())

print(df.groupby("Education_Level")["Income"].mean())

print(df.groupby("Occupation")["Income"].mean())

print(df.groupby("Location")["Income"].mean())

print(df.groupby("Marital_Status")["Income"].mean())

print(df.groupby("Employment_Status")["Income"].mean())

print(df.groupby("Homeownership_Status")["Income"].mean())

print(df.groupby("Type_of_Housing")["Income"].mean())

print(df.groupby("Gender")["Income"].mean())

print(df.groupby("Primary_Mode_of_Transportation")["Income"].mean())

numeric_columns = [
    "Age",
    "Number_of_Dependents",
    "Work_Experience",
    "Household_Size",
    "Income"
]

for column in numeric_columns:
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    Lower_Bound = Q1 - 1.5 * IQR
    Upper_Bound = Q3 + 1.5 * IQR

    outliers = df[
        (df[column] < Lower_Bound) |
        (df[column] > Upper_Bound)
    ]

    print(column)
    print("Q1:", Q1)
    print("Q3:", Q3)
    print("IQR:", IQR)
    print("Lower Bound:", Lower_Bound)
    print("Upper Bound:", Upper_Bound)
    print("Number of Outliers:", len(outliers))

df["Gender"] = df["Gender"].map({
    "Female": 0,
    "Male": 1
})

print(df["Gender"].head())

object_columns = df.select_dtypes(include="object").columns

df = pd.get_dummies(
    df,
    columns=object_columns
)

print(df.head())

print(df.shape)

print(df.select_dtypes(include="object").columns)

df.to_csv(
    r"C:\Users\ZBook G3\Downloads\income-analysis\data\processed\cleaned_data.csv",
    index=False
)