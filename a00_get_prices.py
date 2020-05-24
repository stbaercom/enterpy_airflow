import datetime
import sqlite3

import pandas as pd
import requests

def main():
    df = get_data()
    write_data(df)
    write_db(df)

def write_db(df):
    con = sqlite3.connect("data/data.db")
    df.to_sql(name='sales', con=con, if_exists='append',
              index=False, index_label=["product", "date"])

def write_data(df):
    suffix = df['date'][0]
    df.to_csv(f"data/data_{suffix}.csv", index=False)

def get_data():
    now = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    urls = {
        "price": "http://localhost:5000/price",
        "sales": "http://localhost:5000/sales",
    }
    acum = {}
    for k, v in urls.items():
        acum[k] = requests.get(v).json()
    df = pd.DataFrame.from_dict(acum)
    df['date'] = now
    df['total'] = df['price'] * df['sales']
    df = df.rename_axis("product").reset_index()
    return df

if __name__ == '__main__':
    main()


