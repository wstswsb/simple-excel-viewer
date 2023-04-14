import typing as t

import pandas as pd


class DataframePresenter(t.Protocol):
    def present(self, dataframe: pd.DataFrame) -> str:
        ...


class StringDataframePresenter:
    def present(self, dataframe: pd.DataFrame) -> str:
        return dataframe.to_string()
