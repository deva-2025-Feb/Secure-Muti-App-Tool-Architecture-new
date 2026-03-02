import pandas as pd
import plotly.express as px

df = pd.read_csv("iphone_sales_finance_5000_rows.csv")
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.to_period("M").astype(str)

def sales_summary():
    summary = df.groupby("Month")["Revenue"].sum().reset_index()
    return px.bar(summary, x="Month", y="Revenue", title="Monthly Sales Revenue")

def profit_trend():
    summary = df.groupby("Month")["Profit"].sum().reset_index()
    return px.line(summary, x="Month", y="Profit", title="Monthly Profit Trend")

def region_analysis():
    summary = df.groupby("Region")["Revenue"].sum().reset_index()
    return px.pie(summary, names="Region", values="Revenue", title="Revenue by Region")

def model_comparison():
    summary = df.groupby("Model")["Revenue"].sum().reset_index()
    return px.bar(summary, x="Model", y="Revenue", title="Revenue by Model")

def expense_breakdown():
    summary = df.groupby("Month")["Expenses"].sum().reset_index()
    return px.line(summary, x="Month", y="Expenses", title="Monthly Expense Trend")

def units_sold_trend():
    summary = df.groupby("Month")["Units_Sold"].sum().reset_index()
    return px.line(summary, x="Month", y="Units_Sold", title="Units Sold Trend")

TOOL_REGISTRY = {
    "sales_summary": sales_summary,
    "profit_trend": profit_trend,
    "region_analysis": region_analysis,
    "model_comparison": model_comparison,
    "expense_breakdown": expense_breakdown,
    "units_sold_trend": units_sold_trend
}