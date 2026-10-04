
import pandas as pd
import pytest

from transformation.fact_superstore import calculate_total_sales, calculate_total_profit, calculate_profit_margin, filter_profitable_orders, filter_loss_orders


def test_calculate_total_sales():
    data = {"Sales": [261.96, 731.94, 14.62, 957.5775, 22.368]}
    df = pd.DataFrame(data)
    result = calculate_total_sales(df)
    assert pytest.approx(result) == pytest.approx(1988.466)


def test_calculate_total_profit():
    data = {"Profit": [41.9136, 219.582, 6.8714, -383.031, 2.5164]}
    df = pd.DataFrame(data)
    result = calculate_total_profit(df)
    assert pytest.approx(result) == pytest.approx(-112.148)


def test_calculate_profit_margin():
    data = {
        "Sales": [261.96, 731.94, 14.62, 957.5775, 22.368],
        "Profit": [41.9136, 219.582, 6.8714, -383.031, 2.5164]}
    df = pd.DataFrame(data)
    result = calculate_profit_margin(df)
    expected = round((-112.147 / 1988.466), 3)
    assert pytest.approx(result) == pytest.approx(expected)


def test_filter_profitable_orders():
    data = {"Profit": [41.9136, 219.582, 6.8714, -383.031, 2.5164]}
    df = pd.DataFrame(data)
    result = filter_profitable_orders(df)
    assert len(result) == 4


def test_filter_loss_orders():
    data = {"Profit": [41.9136, 219.582, 6.8714, -383.031, 2.5164]}
    df = pd.DataFrame(data)
    result = filter_loss_orders(df)
    assert len(result) == 1
    assert result.iloc[0]["Profit"] == pytest.approx(-383.031)
