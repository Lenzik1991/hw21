from typing import Dict

from classes_abstractmethod import Storage


class Store(Storage):

    def __init__(self, items: dict, capacity=100):
        self.__items = items
        self.__capacity = capacity

    def add(self, name: str, count: int):
        if name in self.__items.keys():
            if self.get_free_space() >= count:
                print("Товар добавлен")
                self.__items[name] += count
                return True
            else:
                if isinstance(self, Shop):
                    print("Недостаточно места в магазине")
                else:
                    print("Недостаточно места на складе")
                return False
        else:
            if self.get_free_space() >= count:
                print("Товар добавлен")
                self.__items[name] = count
                return True
            else:
                print("Недостаточно места на складе")
                return False

    def remove(self, name, count):
        # self.__items[name] -= count
        # if self.__items[name] == 0:
        #     self.__items.pop(name)

        if self.__items[name] > count:
            print("Нужное количество есть на складе")
            self.__items[name] -= count
            return True
        else:
            print("Недостаточно товара на складе")
            return False

    def get_free_space(self):
        current_space = 0
        for value in self.__items.values():
            current_space += value
        return self.__capacity - current_space

    def get_items(self):
        return self.__items

    def get_unique_items_count(self):
        return len(self.__items.keys())

    def __str__(self):
        st = "\n"
        for key, value in self.__items.items():
            st += f"{key}: {value}\n"
        return st


class Shop(Store):
    def __init__(self, items, capacity=20):
        super().__init__(items, capacity)

    def add(self, name, count):
        if self.get_unique_items_count() >= 5:
            print("Слишком много уникальных товаров")
            return False
        else:
            super().add(name, count)


class Request:
    def __init__(self, request):
        req_list = request.lower().split(' ')
        action = req_list[0]

        self.count = int(req_list[1])
        self.name = req_list[2]
        self.departure = req_list[4]
        self.destination = req_list[6]

        # if action == "Доставить":
        #     self.__from = req_list[4]
        #     self.__to = req_list[6]
        # elif action == "Забрать":
        #     self.__from = req_list[4]
        #     self.__to = None
        # elif action == "Привезти":
        #     self.__to = req_list[4]
        #     self.__from = None


        # if self.__request.departure in storages:
        #     self.__from = storages[self.__request.departure]
        #
        # if self.__request.destination in storages:
        #     self.__from = storages[self.__request.destination]


class Courier:
    def __init__(self, request: Request, storages: Dict[str, Storage]):
        self.__request = request

        if self.__request.departure in storages:
            self.__from = storages[self.__request.departure]

        if self.__request.destination in storages:
            self.__to = storages[self.__request.destination]

    def move(self):
        self.__from.remove(name=self.__request.name, count=self.__request.count)
        print(f'Курьер забрал {self.__request.count} {self.__request.name} из {self.__request.departure}')

        self.__to.add(name=self.__request.name, count=self.__request.count)
        print(f'Курьер доставил {self.__request.count} {self.__request.name} в {self.__request.destination}')


    # def move(self):
    #     if self.__to and self.__from:
    #         if eval(self.__to).add(self.__items, self.__count):
    #             eval(self.__from).remove(self.__items, self.__count)
    #     elif self.__to:
    #         eval(self.__to).add(self.__items, self.__count)
    #     elif self.__from:
    #         eval(self.__from).remove(self.__items, self.__count)

    # def move(self, request_str):
    #    list = request_str.split()
    #    if list[self.__to] and list[self.__from]:
    #        if list[self.__to].add(list[self.__items], list[self.__count]):
    #            list[self.__from].remove(list[self.__items], list[self.__count])
    #    elif list[self.__to]:
    #        list[self.__to].add(list[self.__items], list[self.__count])
    #    elif list[self.__from]:
    #        list[self.__from].remove(list[self.__items], list[self.__count])

    # def move(self):
    #     dict = {"Склад_1": storage_1, "Склад_2": storage_2, "Магазин": shop_1}
