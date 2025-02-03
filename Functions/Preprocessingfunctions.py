import pandas as pd
import datetime as datetime

def convertclock(df):
    if pd.isna(df):
        return None
    try:
        minutes,seconds=map(int,df.split(':'))
        tot_time=(minutes*60)+seconds 
        return tot_time  
    except ValueError:
        return None                 
    
    
def OutlierDetection(df):
  clean_df=df.copy()
  outliers=pd.DataFrame()
  for col in clean_df.columns:
    Q1=df[col].quantile(0.25)
    Q3=df[col].quantile(0.75)
    IQR=Q3-Q1
    lower=Q1-1.5*IQR
    upper=Q3+1.5*IQR
    mask=(df[col] >= lower) & (df[col]<=upper)
    clean_df=clean_df[mask]
  return clean_df



def boxplotter (df):
    fig, ax=plt.subplots(nrows=len(df), ncols=1, figsize=(8, len(df)))
    for ax, col in zip(df, ax):
        ax.boxplot(df[col])
        ax.set_title(f'Boxplot for {col}')
        ax.set_xlabel('Data')
        ax.set_ylabel('Values')
    plt.tight_layout()
    plt.show()
    
    
    
def ShotQualifier(row):
    if row['Shot Bins'] in ['Dunk','Layup'] and row['Openness'] in['Left Alone','Open']:
        return 'High Quality Shot'
    elif row['Shot Bins'] in ['Midrange','Three Pointer'] and row['Openness']=='Left Alone':
        return 'High Quality Shot'
    elif row['Shot Bins'] in['Midrange','Long Two','Three Pointer'] and row['Openness']=='Open':
        return 'Decent Quality Shot'
    elif row['Shot Bins'] in ['Dunk','Layup'] and row['Openness']=='Contested':
        return 'Decent Quality Shot'
    else:
        return 'Low Quality Shot'

