from csv import DictReader
from pathlib import Path


class CSVReader:
    def __init__(self, csv_path: str, required_columns: list):
        self.__check_file_path(csv_path)
        self.__check_is_file_empty(csv_path)
        self.required_columns = required_columns
        self.data = self.__read_file(csv_path)

    @staticmethod
    def __check_file_path(csv_path: str) -> None:
        _csv_path = Path(csv_path)
        assert _csv_path.exists(), "File with path does not exists: {}".format(csv_path)

    @staticmethod
    def __check_is_file_empty(csv_path: str):
        assert Path(csv_path).stat().st_size > 0, "File is empty"

    def __read_file(self, csv_path: str) -> dict:
        with open(csv_path, "r") as f:
            for row in DictReader(f):
                data = {key: row[key] for key in row}

                self.check_columns(data.keys(), self.required_columns)

                yield data

    @staticmethod
    def check_columns(existing_columns, columns: list) -> None:
        for required_col in columns:
            assert required_col in existing_columns, "Column is required: {}".format(required_col)

        for existing_col in existing_columns:
            assert existing_col in columns, "Column is redundant: {}".format(existing_col)


if __name__ == "__main__":
    csv_path = "/home/kristina/PycharmProjects/bootcamp_test_task/optional_task/notes.csv"
    c = CSVReader(csv_path, ['film_name', 'note', 'rating'])

    for el in c.data:
        data = {key: el[key] for key in el}
        print(data)
