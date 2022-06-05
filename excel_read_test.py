import pandas as pd

if __name__ == "__main__":
    df = pd.read_excel(r".\test.xlsx", header=0)
    print(df.test_col)
