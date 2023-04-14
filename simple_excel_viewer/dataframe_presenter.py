import pandas as pd


class PandasDefaultDataframePresenter:
    def present(self, dataframe: pd.DataFrame) -> str:
        if dataframe.empty:
            return "No data"
        return dataframe.to_string()
