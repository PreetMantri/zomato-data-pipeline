from reader import load_data
from cleaner import ZomatoCleaner
from transformer import ZomatoTransformer


main_path = 'data'
df = load_data(f"{main_path}\\zomato.csv")

cleaner = ZomatoCleaner(df)
cleaner.remove_duplicates().drop_nulls()
df = cleaner.df

transformer = ZomatoTransformer(df)
transformer.rename_columns()\
    .clean_rate_columns()\
    .clean_cost_column()\
    .add_price_category()\
    .save_as_parquet(f"{main_path}\\zomato_cleaned.parquet")

