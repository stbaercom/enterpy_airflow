import sqlite3
import pandas as pd

import importlib

def read_db(fn):
    con = sqlite3.connect(fn)
    df = pd.read_sql("select * from sales;", con)
    return df

def calc(df):
    df2 = pd.pivot_table(df,index=["product"], values=["total","sales"],aggfunc="sum")
    df2['avg'] = df2['total'] / df2['sales']
    df2 = df2.rename_axis("product").reset_index()
    return df2

def write_db(df,fn):
    con = sqlite3.connect(fn)
    df.to_sql(name='report', con=con, if_exists='replace',
              index=False, index_label=["product", "date"])

def main():
    fn = "data/data.db"
    df = read_db(fn)
    df2 = calc(df)
    write_db(df2,"data/report.db")

if __name__ == '__main__':
    main()



