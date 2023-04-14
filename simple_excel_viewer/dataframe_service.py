import pandas as pd


class DataframeService:
    def filter(self, dataframe: pd.DataFrame, filters: dict) -> pd.DataFrame:
        for key, value in filters.items():
            dataframe = dataframe.query(f"{key} == '{value}'")
        return dataframe
