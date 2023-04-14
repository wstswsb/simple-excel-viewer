from unittest.mock import Mock

from simple_excel_viewer import PandasDefaultDataframePresenter


class TestPresenter:
    def setup(self):
        self.sut = PandasDefaultDataframePresenter()

    def test_present_with_empty_dataframe(self):
        # arrange
        dataframe_mock = Mock(empty=True)
        # act
        result = self.sut.present(dataframe_mock)
        # assert
        assert result == "No data"

    def test_present_with_not_empty_dataframe(self):
        # arrange
        expected_result = "Presented dataframe"
        dataframe_mock = Mock(empty=False)
        dataframe_mock.to_string = Mock(return_value=expected_result)
        # act
        result = self.sut.present(dataframe_mock)
        # assert
        assert result == expected_result
