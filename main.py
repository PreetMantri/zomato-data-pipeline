from reader import load_data
from cleaner import ZomatoCleaner

main_path = 'C:\\Users\\preet\\Desktop\\Python_prog\\zomato-data-pipeline\\zomato-dataset'
df = load_data(f"{main_path}\\zomato.csv")
cleaner = ZomatoCleaner(df)
cleaner.remove_duplicates().drop_nulls().save_clean("zomato_cleaned.csv")

