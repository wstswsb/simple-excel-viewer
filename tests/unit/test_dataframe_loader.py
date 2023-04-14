from unittest.mock import Mock, patch

import pytest

from simple_excel_viewer import ExcelDataframeLoader, InvalidFileFormat


class TestDataframeLoader:
    def setup(self):
        self.sut = ExcelDataframeLoader()

    @patch("simple_excel_viewer.dataframe_loader.pd")
    def test_load_returns_dataframe(self, pandas_mock: Mock):
        # arrange
        path = "test-path-to-file"
        expected_result = Mock()
        pandas_mock.read_excel = Mock(return_value=expected_result)
        # act
        result = self.sut.load(path)
        # assert
        pandas_mock.read_excel.assert_called_once_with(path)
        assert result == expected_result

    @patch("simple_excel_viewer.dataframe_loader.pd")
    def test_load_raises_exception(self, pandas_mock: Mock):
        # arrange
        path = "test-path-to-file"
        pandas_mock.read_excel = Mock(side_effect=ValueError())
        # act
        with pytest.raises(InvalidFileFormat) as ex:
            self.sut.load(path)
        # assert
        pandas_mock.read_excel.assert_called_once_with(path)
        assert ex.value.args[0] == f"Cannot parse excel file with {path=}"
