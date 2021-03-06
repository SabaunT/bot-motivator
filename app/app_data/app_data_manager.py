import os
import pickle


class FileDataOperator:
    def __init__(self, file_name: str):
        self._file: str = os.path.join(os.path.dirname(__file__), file_name)

    def save_data(self, data):
        with open(self._file, 'wb') as cur_f:
            pickle.dump(data, cur_f)

    def data_load(self):
        with open(self._file, 'rb') as cur_f:
            pickled_data: dict = pickle.load(cur_f)
        return pickled_data


class AppFileDataManager(FileDataOperator):
    """
    Base data manager
    """
    def __init__(self):
        super().__init__('app_db')


class TestFileDataManager(FileDataOperator):
    """
    Data manger for tests
    """
    def __init__(self):
        super().__init__('test_db')


if __name__ == '__main__':
    # todo temporary
    with open(os.path.join(os.path.dirname(__file__), 'app_db'), 'wb') as f:
        pickle.dump({}, f)
