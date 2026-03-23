import pandas as pd

class ZomatoTransformer:
    def __init__(self,df):
        self.df = df

    def rename_columns(self):
        self.df.columns = self.df.columns.str.strip().str.lower().str.replace(' ','_')
        return self
    
    def clean_rate_columns(self):
        self.df['rate'] = self.df['rate'].astype(str).str.replace('/5','').str.strip()
        self.df['rate'] = pd.to_numeric(self.df['rate'], errors = 'coerce')
        return self
    
    def clean_cost_column(self):
        self.df['approx_cost(for_two_people)'] = (
            self.df['approx_cost(for_two_people)']
            .astype(str).str.replace(',','').str.strip()
        )
        self.df['approx_cost(for_two_people)'] = pd.to_numeric(
            self.df['approx_cost(for_two_people)'], errors = 'coerce'
        )
        return self
    
    def add_price_category(self):
        def categorize(cost):
            if pd.isna(cost): return 'Unknown'
            elif cost < 300: return 'Budget'
            elif cost < 700: return 'Mid-range'
            else: return 'Premium'
        
        self.df['price_category'] = self.df['approx_cost(for_two_people)'].apply(categorize)
        return self
    
    def save_as_parquet(self, output_path):
        self.df.to_parquet(output_path, index=False)
        print(f"Saved parquet file to: {output_path}")
        return self
