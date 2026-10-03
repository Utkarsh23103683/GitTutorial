import pandas as pd
import numpy as np
df = pd.read_csv(
    r"C:\Users\utkar\Downloads\Utkarsh Gupta\ineuron\Interview Preparation\Gitnew\src\dim_passengers.csv")


def clean_name(df):
    df["first name"] = df["name"].str.split(" ").str[0]
    df["last name"] = df["name"].str.split(" ").str[1:].str.join(" ")
    df["full name"] = df["first name"] + " " + df["last name"]
    df.drop(columns=["name"], inplace=True)
    return df


def clean_gender(df):
    df["gender"] = df["gender"].str.lower().replace(
        {"male": "M", "female": "F"})
    return df


if __name__ == "__main__":
    df = clean_name(df)
    df = clean_gender(df)
    df = df[["passenger_id", "first name", "last name",
             "full name", "gender", "nationality"]]
    print(df.head())
