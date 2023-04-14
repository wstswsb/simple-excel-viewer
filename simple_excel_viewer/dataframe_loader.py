import typing as t

import pandas as pd
from exceptions import InvalidFileFormat


class DataframeLoader(t.Protocol):
    def load(self, path: str) -> pd.DataFrame:
        ...


class ExcelDataframeLoader:
    def load(self, path: str) -> pd.DataFrame:
        try:
            dataframe = pd.read_excel(path)
        except ValueError as ex:
            raise InvalidFileFormat(f"Cannot parse excel file with {path=}") from ex
        return dataframe
