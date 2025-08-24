import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Zomato Orders Dashboard", layout="wide")

# Load Data

data = pd.read_csv("C:/Users/lenovo/Desktop/zomatoApp/venv/data.csv")


# Title and Subtitle
st.title("🍽️ Zomato Orders Dashboard")
st.subheader("Explore your Food Orders with Advanced Features")

# Sidebar - Filters and Options
st.sidebar.header("Filter Options")

# Filter by City
cities = st.sidebar.multiselect("Filter by City", data['City'].unique())

# Filter by Category
categories = st.sidebar.multiselect("Filter by Category", data['Category'].unique())

# Filter Logic
filtered_data = data

if cities:
    filtered_data = filtered_data[filtered_data['City'].isin(cities)]

if categories:
    filtered_data = filtered_data[filtered_data['Category'].isin(categories)]

# Display Filtered Data
st.write("### Filtered Orders")
st.dataframe(filtered_data)

# Summary Section
st.write("### Summary Stats")

total_orders = filtered_data['OrderID'].nunique()
total_revenue = (filtered_data['Price'] * filtered_data['Quantity']).sum()
total_items = filtered_data['Quantity'].sum()

col1, col2, col3 = st.columns(3)
col1.metric("Total Orders", total_orders)
col2.metric("Total Revenue", f"₹ {total_revenue}")
col3.metric("Total Items Sold", total_items)

# Advanced Features - Buttons
st.write("### Extra Features")

if st.button("Show Top 3 Expensive Items"):
    top_expensive = filtered_data.sort_values(by='Price', ascending=False).head(3)
    st.dataframe(top_expensive)

if st.button("Show All Unique Products"):
    st.write(filtered_data['Product'].unique())

if st.button("Show Total Quantity by Product"):
    quantity_summary = filtered_data.groupby('Product')['Quantity'].sum()
    st.write(quantity_summary)
