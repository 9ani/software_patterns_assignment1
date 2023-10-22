class FileFormatConverter:
    def __init__(self, adapter):
        self.adapter = adapter

    def convert(self, input_file, output_file):
        data = self.adapter.read(input_file)
        self.adapter.write(data, output_file)
