# Sales Dataset Analysis

This project explores a sales dataset to uncover trends, performance metrics, and customer behavior. The goal is to clean the data, perform exploratory analysis, and visualize key insights that can support business decisions.

# Dataset Overview

The dataset contains sales transactions including:
- Date of sale
- Product category
- Quantity sold
- Unit price
- Total revenue
- Region
  
The data was imported from Excel and analyzed using Python (Pandas, Matplotlib) in Google Colab.

# Data Cleaning & Preprocessing

Steps performed:
- Removed missing values in `Total Revenue` and `Unit Price`
- Converted `Date` column to datetime format
- Standardized column names to lowercase
- Verified data types and corrected inconsistencies

# Exploratory Analysis

Key metrics explored:
- Total sales per region
- Top-selling product categories
- Monthly revenue trends
- Average unit price per category

Used `groupby()`, `describe()`, and filtering to extract insights.

# Visualizations

Included:
- Bar chart of top 5 product categories by revenue
- Line chart of monthly sales trends
- Pie chart of sales distribution by region

Visualizations created using Matplotlib and Seaborn.

# Insights & Conclusion

- Region X generated the highest revenue consistently
- Product Category Y was the top performer across all months
- Sales peaked in Q4, suggesting seasonal demand
- Average unit price varied significantly by category

This analysis can help inform inventory planning and marketing strategies. It demonstrates the power of Python and visualization tools in uncovering business insights from raw data.
