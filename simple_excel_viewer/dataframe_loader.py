import pandas as pd

from simple_excel_viewer.exceptions import InvalidFileFormat


class ExcelDataframeLoader:
    def load(self, path: str) -> pd.DataFrame:
        try:
            dataframe = pd.read_excel(path)
        except ValueError as ex:
            raise InvalidFileFormat(f"Cannot parse excel file with {path=}") from ex
        return dataframe
