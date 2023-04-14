import typing as t

import pandas as pd

from simple_excel_viewer.dataframe_service import DataframeService
from simple_excel_viewer.exceptions import InvalidFileFormat


class DataframeLoader(t.Protocol):
    def load(self, path: str) -> pd.DataFrame:
        ...


class DataframePresenter(t.Protocol):
    def present(self, dataframe: pd.DataFrame) -> str:
        ...


class App:
    def __init__(
        self,
        loader: DataframeLoader,
        presenter: DataframePresenter,
        service: DataframeService,
    ):
        self.loader = loader
        self.presenter = presenter
        self.service = service

    def run(self, path: str, filters: dict[str, str]) -> None:
        try:
            dataframe = self.loader.load(path)
            dataframe = self.service.filter(dataframe, filters)
            print(self.presenter.present(dataframe))
        except (pd.errors.UndefinedVariableError, InvalidFileFormat) as ex:
            print(ex)
