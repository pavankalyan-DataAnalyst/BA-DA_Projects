#!/usr/bin/env python
# coding: utf-8

# <a id='1'></a><center> <h3 style="background-color:orange; color:white" ><br>Amazon Sales Project<br></h3>

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv("Amazon Sales data.csv")


# In[3]:


df


# In[4]:


df.info()


# In[5]:


#number of unique values in our data
for i in df.columns:
  print(i,':',df[i].nunique())


# In[6]:


#checking null values in every column of our data
df.isnull().sum()


# In[7]:


df.describe(include=object).T


# In[8]:


df.describe()


# In[9]:


df1 = df.copy()


# In[10]:


df1['Order Date'] = pd.to_datetime(df1['Order Date'])
df1['Ship Date'] = pd.to_datetime(df1['Ship Date'])

df1['Year'] = df1['Order Date'].dt.year
df1['Month'] = df1['Order Date'].dt.month
df1['Quarter'] = df1['Order Date'].dt.quarter
df1['Day'] = df1['Order Date'].dt.day


# In[11]:


df1.info()


# In[12]:


df1


# In[13]:


# Checking the correlation
data_numeric = df1.select_dtypes(include=['float64', 'int64'])
plt.figure(figsize=(10, 6))
sns.heatmap(data_numeric.corr(method='pearson'),annot = True,vmin=-1, vmax=1, cmap='YlGnBu')
plt.show()


# In[14]:


data_numeric = ['Total Revenue', 'Total Cost', 'Total Profit', 'Unit Price', 'Unit Cost']
fig, axes = plt.subplots(nrows=1, ncols=len(data_numeric), figsize=(15, 5))
for i, col in enumerate(data_numeric):
    sns.boxplot(y=df1[col], ax=axes[i])
    axes[i].set_title(f'Boxplot of {col}')
plt.tight_layout()
plt.show()


# In[15]:


df_numeric = df1[data_numeric]
df_numeric


# In[16]:


#rows with outliers in the specified columns using the IQR method
outliers = pd.DataFrame(columns=df.columns)

for col in data_numeric:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    outlier_rows = df[(df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR))]
    outliers = pd.concat([outliers, outlier_rows])

# duplicate rows, if any
outliers = outliers.drop_duplicates()

print("Rows with outliers:")
print(outliers)


# In[17]:


# Key metrics
total_sales_revenue = df1['Total Revenue'].sum()
number_of_orders = df1['Order ID'].nunique()
average_order_value = df1['Total Revenue'].mean()
print("total_sales_revenue:",total_sales_revenue)
print("number_of_orders:",number_of_orders)
print("average_order_value:",average_order_value)


# In[18]:


# Sales by Region
region_sales = df1.groupby('Region')['Total Revenue'].sum()
print("region_sales:",region_sales)


# In[19]:


# Sales by Country
country_sales = df1.groupby('Country')['Total Revenue'].sum()
print("country_sales:",country_sales)


# In[20]:


# Sales by Item Type
item_type_sales = df1.groupby('Item Type')['Total Revenue'].sum()
print("item_type_sales:",item_type_sales)


# In[21]:


# Sales by Sales Channel
sales_channel_sales = df1.groupby('Sales Channel')['Total Revenue'].sum()
print("sales_channel_sales:",sales_channel_sales)


# In[22]:


# Sales by Order Priority
order_priority_sales = df1.groupby('Order Priority')['Total Revenue'].sum()
print("order_priority_sales:",order_priority_sales)


# In[23]:


# Monthly Sales Trend
monthly_sales_trend = df1.groupby(['Year', 'Month'])['Total Revenue'].sum()
print("monthly_sales_trend",monthly_sales_trend)


# In[24]:


# Yearly Sales Trend
yearly_sales_trend = (df1.groupby('Year')['Total Revenue'].sum())
print("yearly_sales_trend:",yearly_sales_trend)


# In[25]:


# Yearly Profit Trend
yearly_Profit_trend = df1.groupby('Year')['Total Profit'].sum()
print("yearly_Profit_trend:",yearly_sales_trend)


# In[26]:


# Yearly profit data
yearly_profit = {
    2010: 19186024.92,
    2011: 11129166.07,
    2012: 31898644.52,
    2013: 20330448.66,
    2014: 16630214.43,
    2015: 12427982.86,
    2016: 12372867.22,
    2017: 13373419.63
}

# total profit
total_profit = sum(yearly_profit.values())

# percentage of profit for each year
yearly_profit_percentage = {year: (profit / total_profit) * 100 for year, profit in yearly_profit.items()}

# Pie chart
plt.figure(figsize=(15, 6))
plt.pie(yearly_profit_percentage.values(), labels=yearly_profit_percentage.keys(), autopct='%1.1f%%', startangle=140)
plt.title('Yearly Profit Distribution')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()


# In[28]:


# Filter data for the year 2012
df_2012 = df1[df1['Year'] == 2012]

# joint plot
sns.jointplot(data=df_2012, x='Month', y='Total Profit', kind='scatter',)
plt.suptitle('Joint Plot of Total Profit for the Year 2012', y=1.02)
plt.show()


# In[29]:


sns.pairplot(df)


# # Top_10_countries_with_highest_profit
# ![top_10_countries_with_highest_profit.png](attachment:top_10_countries_with_highest_profit.png)

# # Total_profit_by_country__region__and_item_type
# ![total_profit_by_country__region__and_item_type.png](attachment:total_profit_by_country__region__and_item_type.png)

# # Total_profit_by_item_type_and_region
# ![total_profit_by_item_type_and_region.png](attachment:total_profit_by_item_type_and_region.png)

# # Average_profit_margin_by_item_type
# ![average_profit_margin_by_item_type.png](attachment:average_profit_margin_by_item_type.png)

# # Average_unit_price_and_unit_cost_by_item_type
# ![average_unit_price_and_unit_cost_by_item_type.png](attachment:average_unit_price_and_unit_cost_by_item_type.png)

# # Total_profit_by_region
# ![total_profit_by_region.png](attachment:total_profit_by_region.png)

# # yearly_sales_trend
# ![yearly_sales_trend.png](attachment:yearly_sales_trend.png)

# # Monthly_sales_trend
# ![monthly_sales_trend.png](attachment:monthly_sales_trend.png)

# # Monthly_profit_over_the_years
# ![monthly_profit_over_the_years.png](attachment:monthly_profit_over_the_years.png)

# # Total_profit_by_item_type
# ![total_profit_by_item_type.png](attachment:total_profit_by_item_type.png)

# # Order_priority_vs_total_revenue
# ![order_priority_vs_total_revenue.png](attachment:order_priority_vs_total_revenue.png)

# # Total_profit_by_sales_channel
# ![total_profit_by_sales_channel.png](attachment:total_profit_by_sales_channel.png)

# # Unit_price_vs__unit_cost
# ![unit_price_vs__unit_cost.png](attachment:unit_price_vs__unit_cost.png)

# # sales_channel_vs_order_priority
# ![sales_channel_vs_order_priority.png](attachment:sales_channel_vs_order_priority.png)

# # Count_vs_unit_price
# * This chart reveals the frequency distribution of unit prices, helping identify pricing patterns and potential areas for optimization to increase profits.
# ![histogram.png](attachment:histogram.png)

# # Total_Profit_vs_Sales_Channel
# * This chart displays the total profit generated by each sales channel, providing insights into the effectiveness of different distribution methods in reducing costs and increasing profits.
# ![bar_chart.png](attachment:bar_chart.png)

# # Toal_revenue_Order_date
# * This plot shows the trend of total revenue over time, allowing for analysis of the effectiveness of sales management in increasing profits.
# ![line_plot.png](attachment:line_plot.png)

# # Recomandations
# 1. Focus on the Asia region: The Asia region has the second highest total profit, indicating potential for growth. Allocate more resources and marketing efforts to tap into this market and increase profitability further.
# 
# 2. Explore opportunities in Australia and Oceania: Australia and Oceania have a decent total profit. Consider expanding operations and increasing sales efforts in this region to maximize profits.
# 
# 3. Invest in Central America and the Caribbean: Central America and the Caribbean have a relatively lower total profit compared to other regions. Look for ways to strengthen presence in this market and boost sales to increase profitability.
# 
# 4. Analyze sales strategy: The most common sales channel is offline. Evaluate the effectiveness of the current sales channels and consider diversifying or optimizing the sales strategy to reach a wider customer base and increase sales.
# 
# 5. Identify high-revenue countries: Honduras has been identified as the country with the highest revenue. Investigate the reasons behind this success and consider expanding operations or replicating successful strategies in other countries to increase overall revenue.
# 
# 6. Increase average unit price: The average unit price is $276.76. Explore opportunities to increase pricing without sacrificing demand to maximize revenue and profitability.
# 
# 7. Improve sales volume: The total units sold is 512,871. Focus on increasing sales volume by implementing targeted marketing campaigns, expanding distribution channels, and identifying potential untapped markets.
# 
