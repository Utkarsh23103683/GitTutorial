import pandas as pd

# df = pd.read_csv(r"src\Fact_Superstore.csv", encoding="latin1")


def calculate_total_profit(df):
    return round(df["Profit"].sum(), 3)


def calculate_total_sales(df):
    return round(df["Sales"].sum(), 3)


def calculate_profit_margin(df):
    return round((df["Profit"].sum() / df["Sales"].sum()), 3)


def filter_profitable_orders(df):
    return df[df["Profit"] > 0]


def filter_loss_orders(df):
    return df[df["Profit"] < 0]
