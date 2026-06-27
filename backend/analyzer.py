import pandas as pd
df= pd.read_csv("/Users/jiyaarora/Downloads/SampleSuperstore.csv")
print(df.shape)

def total_sales(df):
    return df["Sales"].sum()
def top_category(df):
    category_sales=df.groupby('Category')['Sales'].sum()
    return category_sales.idxmax()
def top_region(df):
    regions= df.groupby('Region')['Sales'].sum()
    return regions.idxmax()
def  total_profit(df):
    return df['Profit'].sum()
def most_profit_region(df):
    profregion=df.groupby('Region')['Profit'].sum()
    return profregion.idxmax()
def generate_insights(df):    
    insights={
        "total_sales":round(total_sales(df),2),
        "top_category" : top_category(df),
        "top_region":top_region(df),
        "total_profit": round(total_profit(df),2),
        "most_profitable region": most_profit_region(df)
    }
    return insights
print(generate_insights(df))