import pandas as pd
import numpy as np


if __name__ == "__main__":
    df = pd.DataFrame()
    df["test_col"] = [1, 2, 3, 4, 5]
    print(df)
    df.to_excel("test.xlsx")
