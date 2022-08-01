from typing import List, Dict, Union
from csv import writer
from statistics import mean, median

from optional_task.csv_reader import CSVReader


class UKFilmsNotes:
    def __init__(self, csv_path):
        self.__columns = ['film_name', 'note', 'rating']
        self.__csv_path = csv_path
        self.__csv_data = CSVReader(self.__csv_path, self.__columns).data

    def __clear_file(self):
        with open(self.__csv_path, "w") as file:
            writer(file).writerow(self.__columns)

    @staticmethod
    def __convert_dict_csv_item_to_list(dict_csv_item: Dict) -> List:
        list_csv_item = [dict_csv_item[key] for key in dict_csv_item.keys()]
        return list_csv_item

    @staticmethod
    def __check_row(row: List[Union[str, int]]):
        conditions = [isinstance(row, list), len(row) == 3, isinstance(row[0], str), isinstance(row[1], str),
                      isinstance(row[2], int)]
        if not all(conditions):
            return False
        return True

    def get_notes(self) -> List[Dict[str, str]]:
        notes_list = []
        for el in self.__csv_data:
            data = {key: el[key] for key in el}
            notes_list.append(data)
        return notes_list

    def print_notes(self):
        for el in self.__csv_data:
            data = {key: el[key] for key in el}
            print(data)

    def add_note(self, note: List[Union[str, int]]):
        with open(self.__csv_path, 'a', newline='') as file:
            writer_object = writer(file)
            if UKFilmsNotes.__check_row(note):
                writer_object.writerow(note)

    def remove_note(self, index: int):
        notes = self.get_notes()
        self.__clear_file()
        with open(self.__csv_path, 'a') as file:
            writer_object = writer(file)
            [writer_object.writerow(UKFilmsNotes.__convert_dict_csv_item_to_list(notes[i])) for i in range(len(notes))
             if i != index]

    def get_avg_films_rating(self) -> int:
        notes = self.get_notes()
        ratings = [int(note["rating"]) for note in notes]
        avg_rating = mean(ratings)
        return avg_rating

    def get_best_films(self) -> List[Dict[str, str]]:
        notes = self.get_notes()
        ratings = [int(note["rating"]) for note in notes]
        median_value = median(ratings)
        best_films = [notes[i] for i in range(len(ratings)) if int(notes[i]["rating"]) > median_value]
        return best_films

    def get_worst_films(self) -> List[Dict[str, str]]:
        notes = self.get_notes()
        ratings = [int(note["rating"]) for note in notes]
        median_value = median(ratings)
        worst_films = [notes[i] for i in range(len(ratings)) if int(notes[i]["rating"]) < median_value]
        return worst_films


if __name__ == '__main__':
    ukn = UKFilmsNotes("/home/kristina/PycharmProjects/bootcamp_test_task/optional_task/notes.csv")
    # ukn.add_note(["Hello", "Some note3", 5])
    # ukn.remove_note(0)
    # print(ukn.get_avg_films_rating())
    print(ukn.get_best_films())
    # print(ukn.get_worst_films())
