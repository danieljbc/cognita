from backend.modules.parsers.multimodalparser import MultiModalParser
from backend.modules.parsers.parser import register_parser
from backend.modules.parsers.unstructured_io import UnstructuredIoParser
from backend.modules.parsers.sourcecodeparser import SourceCodeParser

# The order of registry defines the order of precedence
register_parser("SourceCodeParser", SourceCodeParser)
register_parser("MultiModalParser", MultiModalParser)
register_parser("UnstructuredIoParser", UnstructuredIoParser)
