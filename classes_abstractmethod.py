from abc import abstractmethod, ABC


class Storage(ABC):
    @abstractmethod
    def add(self, name, count):
#        raise NotImplemented
        pass

    @abstractmethod
    def remove(self, name, count):
#        raise NotImplemented
        pass

    @abstractmethod
    def get_free_space(self):
#        raise NotImplemented
        pass

    @abstractmethod
    def get_items(self):
#        raise NotImplemented
        pass

    @abstractmethod
    def get_unique_items_count(self):
#        raise NotImplemented
        pass