from abc import ABC, abstractmethod


class XmlDataClass(ABC):
    @abstractmethod
    def to_yaml(self):
        pass
