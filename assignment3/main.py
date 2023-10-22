from FileFormatReader import JSONFileReader
from FileFormatWriter import JSONFileWriter
from FileFormatAdapter import JSONToXMLAdapter
from FileFormatConverter import FileFormatConverter

json_reader = JSONFileReader()
json_writer = JSONFileWriter()

json_to_xml_adapter = JSONToXMLAdapter(json_reader, json_writer)

converter = FileFormatConverter(json_to_xml_adapter)

converter.convert("data.json", "data.xml")