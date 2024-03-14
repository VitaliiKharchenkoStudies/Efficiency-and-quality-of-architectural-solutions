import os
from DataGenerator import *
import time


class DataProcessor:
    def __init__(self):
        self.data = []

    def process_data(self):
        self._read_data_from_file()
        processed_data = self._process_data()
        self._write_processed_data_to_file(processed_data)

    def _read_data_from_file(self):
        with open('data.txt', 'r') as file:
            for line in file:
                self.data.append(line.strip())

    def _process_data(self):
        processed_data = []
        for item in self.data:
            if item.startswith('A'):
                processed_data.append(self._process_type_a(item))
            elif item.startswith('B'):
                processed_data.append(self._process_type_b(item))
            else:
                processed_data.append(self._process_other(item))
        return processed_data

    def _write_processed_data_to_file(self, processed_data):
        with open('processed_data.txt', 'w') as file:
            for item in processed_data:
                file.write(f"{item}\n")

    def _process_type_a(self, item):
        return item.upper()

    def _process_type_b(self, item):
        return item.lower()

    def _process_other(self, item):
        return item.capitalize()


if __name__ == '__main__':
    if not os.path.isfile('data.txt'):
        generate(1000)
    start_time = time.time()
    processor = DataProcessor()
    processor.process_data()
    end_time = time.time()
    print(f"Executing time: {end_time - start_time}")
