import typing as t

import pandas as pd


class DataframePresenter(t.Protocol):
    def present(self, dataframe: pd.DataFrame) -> str:
        ...


class PandasDefaultDataframePresenter:
    def present(self, dataframe: pd.DataFrame) -> str:
        if dataframe.empty:
            return "No data"
        return dataframe.to_string()
