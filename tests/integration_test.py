import pandas as pd
from transformation.fact_superstore import calculate_total_sales, calculate_total_profit


def test_dataset_is_not_empty():
    df = pd.read_csv(r"src\Fact_Superstore.csv", encoding="latin1")
    assert len(df) > 0


def test_required_columns_exist():
    df = pd.read_csv(r"src\Fact_Superstore.csv", encoding="latin1")
    required_columns = ["Order ID", "Order Date", "Ship Date",
                        "Customer ID", "Sales", "Quantity", "Discount", "Profit"]

    for column in required_columns:
        assert column in df.columns


def test_customer_id_not_null():
    df = pd.read_csv(r"src\Fact_Superstore.csv", encoding="latin1")
    assert df["Customer ID"].notna().all()


def test_order_id_not_null():
    df = pd.read_csv(r"src\Fact_Superstore.csv", encoding="latin1")
    assert df["Order ID"].notna().all()


def test_row_id_unique():
    df = pd.read_csv(r"src\Fact_Superstore.csv", encoding="latin1")
    assert df["Row ID"].is_unique


def test_sales_not_negative():
    df = pd.read_csv(r"src\Fact_Superstore.csv", encoding="latin1")
    assert (df["Sales"] >= 0).all()


def test_quantity_positive():
    df = pd.read_csv(r"src\Fact_Superstore.csv", encoding="latin1")
    assert (df["Quantity"] > 0).all()


def test_discount_valid():
    df = pd.read_csv(r"src\Fact_Superstore.csv", encoding="latin1")
    assert (df["Discount"] >= 0).all()
    assert (df["Discount"] <= 1).all()


def test_profit_is_numeric():
    df = pd.read_csv(r"src\Fact_Superstore.csv", encoding="latin1")
    assert df["Profit"].dtype.kind in "fi"


def test_calculate_sales_from_real_dataset():
    df = pd.read_csv(r"src\Fact_Superstore.csv", encoding="latin1")
    result = calculate_total_sales(df)
    assert result > 0


def test_calculate_profit_from_real_dataset():
    df = pd.read_csv(r"src\Fact_Superstore.csv", encoding="latin1")
    result = calculate_total_profit(df)
    assert result is not None
