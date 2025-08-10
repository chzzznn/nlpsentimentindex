import pandas as pd
from statsmodels.formula.api import ols

def rolling_corr(df: pd.DataFrame, window: int = 7) -> pd.Series:
    return df["sentiment"].rolling(window).corr(df["log_return"]).rename("rolling_corr")

def lag_regression(df: pd.DataFrame):
    tmp = df.copy()
    tmp["ret_t1"] = tmp["log_return"].shift(-1)
    model = ols("ret_t1 ~ sentiment", data=tmp.dropna()).fit()
    return model
