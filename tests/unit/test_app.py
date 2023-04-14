from unittest.mock import Mock

from simple_excel_viewer import App, InvalidFileFormat


class TestApp:
    def setup(self):
        self.loader_mock = Mock()
        self.presenter_mock = Mock()
        self.service_mock = Mock()
        self.sut = App(self.loader_mock, self.presenter_mock, self.service_mock)

    def test_run(self, capsys):
        # arrange
        path = "test-path-to-file"
        filters = {"key_1": "value_1"}
        loaded_dataframe_mock = Mock()
        filtered_dataframe_mock = Mock()
        presented_dataframe_mock = "test-present"
        self.loader_mock.load = Mock(return_value=loaded_dataframe_mock)
        self.service_mock.filter = Mock(return_value=filtered_dataframe_mock)
        self.presenter_mock.present = Mock(return_value=presented_dataframe_mock)
        # act
        self.sut.run(path, filters)
        # assert
        self.loader_mock.load.assert_called_once_with(path)
        self.service_mock.filter.assert_called_once_with(loaded_dataframe_mock, filters)
        self.presenter_mock.present.assert_called_once_with(filtered_dataframe_mock)
        assert capsys.readouterr().out == f"{presented_dataframe_mock}\n"

    def test_run_raises_exception(self, capsys):
        # arrange
        path = "test-path-to-file"
        filters = {"key_1": "value_1"}
        error_message = "invalid file"
        self.loader_mock.load = Mock(side_effect=InvalidFileFormat(error_message))
        # act
        self.sut.run(path, filters)
        # assert
        self.loader_mock.load.assert_called_once_with(path)
        assert capsys.readouterr().out == f"{error_message}\n"
