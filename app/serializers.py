import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod
from app.models import Book


class Serializer(ABC):

    @abstractmethod
    def serialize(self, book: Book):
        pass


class JsonSerializer(Serializer):
    def __init__(self, serialize_type: str):
        self.serialize_type = serialize_type

    def serialize(self, book: Book):
        if self.serialize_type == "json":
            return json.dumps({"title": book.title, "content": book.content})
        else:
            raise ValueError(f"Unknown serialize type: {self.serialize_type}")


class XmlSerializer(Serializer):
    def __init__(self, serialize_type: str):
        self.serialize_type = serialize_type

    def serialize(self, book: Book):
        if self.serialize_type == "xml":
            root = ET.Element("book")
            title = ET.SubElement(root, "title")
            title.text = book.title
            content = ET.SubElement(root, "content")
            content.text = book.content
            return ET.tostring(root, encoding="unicode")
        else:
            raise ValueError(f"Unknown serialize type: {self.serialize_type}")
