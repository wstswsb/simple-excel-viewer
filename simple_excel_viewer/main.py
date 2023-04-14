import pandas as pd
from dataframe_loader import ExcelDataframeLoader
from dataframe_presenter import StringDataframePresenter
from dataframe_service import DataframeService
from exceptions import InvalidFileFormat

loader = ExcelDataframeLoader()
service = DataframeService()
presenter = StringDataframePresenter()


def main(path: str, filters: dict) -> None:
    try:
        dataframe = loader.load(path)
        dataframe = service.filter(dataframe, filters)
        print(presenter.present(dataframe))
    except (pd.errors.UndefinedVariableError, InvalidFileFormat) as ex:
        print(ex)
