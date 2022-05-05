from abc import ABC, abstractmethod
from uuid import uuid4


class XmlDataClass(ABC):
    def __init__(self):
        self.uuid = uuid4().hex

    @abstractmethod
    def to_yaml(self):
        pass
