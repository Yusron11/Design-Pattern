from abc import ABC, abstractmethod
from typing import List, Dict
import json
import csv
from io import StringIO

class DataConverter(ABC):
    @abstractmethod
    def convert(self, data: str) -> List[Dict]:
        pass

class JsonConverter(DataConverter):
    def convert(self, data: str) -> List[Dict]:
        return json.loads(data)

class CsvConverter(DataConverter):
    def convert(self, data: str) -> List[Dict]:
        csv_reader = csv.DictReader(StringIO(data))
        return [row for row in csv_reader]

def convert_data(converter: DataConverter, data: str) -> List[Dict]:
    return converter.convert(data)

json_data = '[{"name": "Ahmad", "age": 20}, {"name": "Yusron", "age": 21}, {"name": "Alex Smith", "age": 25}]'
csv_data = 'name,age\nAhmad,20\nYusron,21\nJhon Doe,25'

json_converter = JsonConverter()
csv_converter = CsvConverter()

converted_json_data = convert_data(json_converter, json_data)
print("Converted JSON data:", converted_json_data)

converted_csv_data = convert_data(csv_converter, csv_data)
print("Converted CSV data:", converted_csv_data)
