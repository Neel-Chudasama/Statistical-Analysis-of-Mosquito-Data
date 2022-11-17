# import core ds libs
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def basic_eda(df, df_name):
    """
    getting some basic information about each dataframe
    shape of dataframe i.e. number of rows and columns
    total number of rows with null values
    total number of duplicates
    data types of columns

    Args:
        df (dataframe): dataframe containing the data for analysis
        df_name (string): name of the dataframe
    """
    print(df_name.upper())
    print()
    print(f"Rows: {df.shape[0]} \t Columns: {df.shape[1]}")
    print()
    
    print(f"Total null rows: {df.isnull().sum().sum()}")
    print(f"Percentage null rows: {round(df.isnull().sum().sum() / df.shape[0] * 100, 2)}%")
    print()
    
    print(f"Total duplicate rows: {df[df.duplicated(keep=False)].shape[0]}")
    print(f"Percentage dupe rows: {round(df[df.duplicated(keep=False)].shape[0] / df.shape[0] * 100, 2)}%")
    print()
    
    print(df.dtypes)
    print("-----\n")


def eda(df):
    """
    getting some basic information about each dataframe
    shape of dataframe i.e. number of rows and columns
    total number of rows with null values
    total number of duplicates
    data types of columns

    Args:
        df (dataframe): dataframe containing the data for analysis
        df_name (string): name of the dataframe
    """
    print()
    print(f"Rows: {df.shape[0]} \t Columns: {df.shape[1]}")
    print()
    
    print(f"Total null rows: {df.isnull().sum().sum()}")
    print(f"Percentage null rows: {round(df.isnull().sum().sum() / df.shape[0] * 100, 2)}%")
    print()
    
    print(f"Total duplicate rows: {df[df.duplicated(keep=False)].shape[0]}")
    print(f"Percentage dupe rows: {round(df[df.duplicated(keep=False)].shape[0] / df.shape[0] * 100, 2)}%")
    print()
    
    print(df.dtypes)
    print("-----\n")
    
    print()
    print("The head of the dataframe is: ")
    display(df.head(5))
    
    print()
    print("The tail of the dataframe is:")
    display(df.tail(5))
    
    print()
    print("Description of the numerical columns is as follows")
    display(df.describe())
    
def plot_dist_by_dim(data, column, dim):
    """
    Plots the given column against the registration station in the data.
    The function assumes data is a dataframe, column is string (existing column in data),
    and data has a registered column too.
    """
    total_count = data.groupby([column, dim])[column].count()
    pct_contact_type = total_count/data.groupby(column)[column].count()
    pct_contact_type = pct_contact_type.unstack()
    print(pct_contact_type.sort_values([1]))
    
    plt.rcParams['figure.dpi'] = 360
    plt.rcParams['figure.figsize'] = (5, 5)
    # set the font name for a font family
#     plt.rcParams.update({'font.sans-serif':'Helvetica'})
    sns.set(style="whitegrid")
    pct_contact_type.sort_values([1]).plot(kind="bar", stacked=True, color=['#003f5c', '#ffa600', '#bc5090'])
    sns.despine(left=True)
    plt.title(f"{column} group distribution", size=10, color='#4f4e4e', fontweight="bold")
    plt.xlabel('')
    plt.xticks(size=8, color='#4f4e4e', rotation=90)
    plt.yticks(size=8, color='#4f4e4e')
    plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
    plt.show()

# def eda(df):
#     print("1) Are there missing values:")
#     if df.isnull().any().unique().shape[0] == 2:
#         if df.isnull().any().unique()[0] == False and df.isnull().any().unique()[1] == False:
#             print('No\n')
#         else:
#             print("Yes|Percentage of missing values in each column:\n",df.isnull().sum()/df.shape[0],'\n')
#     elif df.isnull().any().unique().shape[0] == 1:
#         if df.isnull().any().unique() == False:
#             print('No\n')
#         else:
#             print("Yes|Percentage of missing values in each column:\n",df.isnull().sum()/df.shape[0],'\n')

#     print("2) Which are the data types:\n")
#     print(df.dtypes,'\n')
#     print("3) Dataframe shape:",df.shape)
#     print("4) Unique values per columm")
#     for col in df.columns.tolist():
#         print (col,":",df[col].nunique())  
#     print("5) Removing duplicates")
#     print('Initial shape:',df.shape)
#     df.groupby(df.columns.tolist()).size().reset_index().rename(columns={0:'count'}).sort_values('count',ascending=False).head()
#     df.drop_duplicates(inplace=True)
#     print('Shape after removing duplicates:',df.shape)
#     return