from unittest.mock import Mock, call

from simple_excel_viewer import DataframeService


class TestDataframeService:
    def setup(self):
        self.sut = DataframeService()

    def test_filter(self):
        # arrange
        filters = {f"key_{i}": f"value_{i}" for i in range(3)}
        dataframe_mock = Mock()
        dataframe_mock.query = Mock(return_value=dataframe_mock)
        # act
        result = self.sut.filter(dataframe_mock, filters)
        # assert
        dataframe_mock.query.assert_has_calls(
            [
                call("key_0 == 'value_0'"),
                call("key_1 == 'value_1'"),
                call("key_2 == 'value_2'"),
            ]
        )
        assert result == dataframe_mock
