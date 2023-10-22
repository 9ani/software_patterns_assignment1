from assignment3.FileFormatReader import FileFormatReader
from assignment3.FileFormatWriter import FileFormatWriter


class JSONToXMLAdapter(FileFormatReader, FileFormatWriter):
    def __init__(self, json_reader, json_writer):
        self.json_reader = json_reader
        self.json_writer = json_writer

    def read(self, file_path):
        json_data = self.json_reader.read(file_path)
        xml_data = json_data
        return xml_data

    def write(self, data, file_path):
        json_data = data
        self.json_writer.write(json_data, file_path)
