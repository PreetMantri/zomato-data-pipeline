import pandas as pd
class ZomatoCleaner:
    def __init__ (self, df):
        self.df = df

    def remove_duplicates(self):
        self.df = self.df.drop_duplicates()
        return self
    
    def drop_nulls(self):
        self.df = self.df.dropna()
        return self
    
    def save_clean(self, output_path):
        self.df.to_csv(output_path, index = False)
        print(f"Cleaned data saved to {output_path}")
