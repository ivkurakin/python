from abc import ABC, abstractmethod


class Warehouse:
    def __init__(self, space):
        self.__space = space  # инициализация общего объема склада
        self.__tech_dict = {'Computer': [{'Apple': 0}, 0], 'Notebook': [{'hp': 0, 'lenovo': 0}, 0],
                            'Printer': [{'Samsung': 0, 'Sony': 0}, 0]}  # тип техники : [{фирма : количество}, объем]

    def get_free_space(self):  # расчет свободного места
        return self.__space - self.get_occupied_space()

    def get_occupied_space(self):  # расчет занятого места
        occupied_space = 0
        for el in self.__tech_dict.keys():
            occupied_space += self.__tech_dict[el][1]
        return occupied_space

    def receive_technique(self, other):  # прием техники
        if other.check_firm(other.firm):
            request_space = Technique.get_space(other.count, other.box_space(other.firm))
            if request_space > self.get_free_space():
                return f'Можем принять только {self.get_free_space() // other.firm_list[other.firm]} {other.get_kind_tech} {other.firm}'
            else:
                self.__tech_dict[other.get_kind_tech][0][other.firm] += other.count
                self.__tech_dict[other.get_kind_tech][1] += request_space
                return f'Принято {other.count} {other.get_kind_tech} {other.firm}'
        else:
            return f"Фирму {other.firm} для {other.get_kind_tech} не берем!"

    def take_to_dep(self, dep, req_count, kind_tech, firm):  # функция готовности выдачи техники в отдел
        if kind_tech == 'Notebook':
            if Notebook.check_dep(dep):  # проверка департамента
                if Notebook.check_firm(firm):  # проверка фирмы
                    if self.__tech_dict['Notebook'][0][firm] < req_count:
                        return f"Можем отдать только {self.__tech_dict['Notebook'][0][firm]} {kind_tech} {firm}"
                    else:
                        self.__tech_dict['Notebook'][0][firm] -= req_count
                        self.__tech_dict['Notebook'][1] -= Technique.get_space(Notebook.box_space(firm), req_count)
                else:
                    return f"Фирму {firm} для {kind_tech} не берем!"
            else:
                return f"Для Вашего отдела недоступно. Обратитесь к директору!"
        elif kind_tech == 'Computer':
            if Computer.check_firm(firm):  # проверка фирмы
                if self.__tech_dict['Computer'][0][firm] < req_count:
                    return f"Можем отдать только {self.__tech_dict['Computer'][0][firm]} {kind_tech} {firm}"
                else:
                    self.__tech_dict['Computer'][0][firm] -= req_count
                    self.__tech_dict['Computer'][1] -= Technique.get_space(req_count, Computer.box_space(firm))
            else:
                return f"Фирму {firm} для {kind_tech} не берем!"
        elif kind_tech == 'Printer':
            if Printer.check_firm(firm):  # проверка фирмы
                if self.__tech_dict['Printer'][0][firm] < req_count:
                    return f"Можем отдать только {self.__tech_dict['Printer'][0][firm]} {kind_tech} {firm}"
                else:
                    self.__tech_dict['Printer'][0][firm] -= req_count
                    self.__tech_dict['Printer'][1] -= Technique.get_space(req_count, Printer.box_space(firm))
            else:
                return f"Фирму {firm} для {kind_tech} не берем!"

    @property
    def space(self):  # Функция получения площади склада (через геттер).
        return self.__space

    @space.setter
    def space(self, space):  # Функция увеличения площади склада (через сеттер).
        if space < self.__space:
            pass  # MyOWNER
        else:
            self.__space = space

    def __str__(self):  # просмотр техники
        info_str = ''
        for key in self.__tech_dict.keys():
            info_str += (f'{key} : {self.__tech_dict[key][0]}\n')
        info_str += (f'Занятое пространство: {self.get_occupied_space()}')
        return info_str


class Technique(ABC):
    @staticmethod
    def get_space(box_space, count_box):
        return box_space * count_box

    @abstractmethod
    def check_firm(self, firm):
        pass

    @property
    def get_kind_tech(self):
        return self._kind


class Printer(Technique):
    __firm_list = {'Samsung': 10, 'Sony': 10}  # фирма : объем коробки

    def __init__(self, firm, count):
        self.firm = firm
        self.count = count
        self._kind = 'Printer'

    @staticmethod
    def box_space(firm):
        return Printer.__firm_list[firm]

    @property
    def firm_list(self):
        return Printer.__firm_list

    @classmethod
    def check_firm(self, firm):
        if firm in self.__firm_list:
            return True
        else:
            return False


class Computer(Technique):
    __firm_list = {'Apple': 40}  # фирма : объем коробки

    def __init__(self, firm, count):
        self.firm = firm
        self.count = count
        self._kind = 'Computer'

    @staticmethod
    def box_space(firm):
        return Computer.__firm_list[firm]

    @property
    def firm_list(self):
        return Computer.__firm_list

    @classmethod
    def check_firm(self, firm):
        if firm in self.__firm_list:
            return True
        else:
            return False


class Notebook(Technique):
    __dep_list = [1, 3, 5]  # инициализация отделов, куда можно передавать
    __firm_list = {'hp': 15, 'lenovo': 20}  # фирма : объем коробки

    def __init__(self, firm, count):
        self.firm = firm
        self.count = count
        self._kind = 'Notebook'

    @staticmethod
    def box_space(firm):
        return Notebook.__firm_list[firm]

    @property
    def firm_list(self):
        return Notebook.__firm_list

    @classmethod
    def dep_list_add(cls, dep):
        return cls.__dep_list.append(dep)

    @classmethod
    def dep_list(cls):
        return cls.__dep_list

    @classmethod
    def check_dep(cls, dep_request):
        if dep_request in cls.__dep_list:
            return True
        else:
            return False

    @classmethod
    def check_firm(cls, firm):
        if firm in cls.__firm_list:
            return True
        else:
            return False


warehouse = Warehouse(1000)
print(f'Свободное пространство: {warehouse.get_free_space()}')

print(f'Добавляем технику всех типов и всех доступных фирм:')
notebook1 = Notebook('lenovo', 10)  # каждый объект - это поставка определенной техники и фирмы
print(warehouse.receive_technique(notebook1))
print(f'Свободное пространство: {warehouse.get_free_space()}')
notebook2 = Notebook('hp', 15)
print(warehouse.receive_technique(notebook2))
print(f'Свободное пространство: {warehouse.get_free_space()}')
computer = Computer('Apple', 8)
print(warehouse.receive_technique(computer))
print(f'Свободное пространство: {warehouse.get_free_space()}')
printer1 = Printer('Samsung', 7)
print(warehouse.receive_technique(printer1))
print(f'Свободное пространство: {warehouse.get_free_space()}')
printer2 = Printer('Sony', 15)
print(warehouse.receive_technique(printer2))
print(f'Свободное пространство: {warehouse.get_free_space()}')
print()
print(f'Для всех продуктов пытаемся добавить неподходящую фирму:')
notebook3 = Notebook('Apple', 15)
print(warehouse.receive_technique(notebook3))
computer3 = Computer('Sony', 15)
print(warehouse.receive_technique(computer3))
printer3 = Printer('hp', 15)
print(warehouse.receive_technique(printer3))
print(f'Свободное пространство: {warehouse.get_free_space()}')
print(warehouse)
print()
print(f'Попытка добавить свыше свободного пространства:')  # print(warehouse.space)
print(warehouse.receive_technique(printer1))
print(f'Свободное пространство: {warehouse.get_free_space()}')
print()
print(f'Увеличение склада:')
warehouse.space = 1500
print(f'Общее пространство склада:{warehouse.space}')
print(f'Свободное пространство: {warehouse.get_free_space()}')
print()
print(f'Дополняем склад техникой:')
notebook4 = Notebook('lenovo', 5)
computer4 = Computer('Apple', 3)
printer4 = Printer('Sony', 7)
print(warehouse.receive_technique(notebook4))
print(warehouse.receive_technique(computer4))
print(warehouse.receive_technique(printer4))
print(warehouse)
print()
print(f'Отдаем технику всех типов и всех доступных фирм в отделы: ')
warehouse.take_to_dep(1, 10, 'Notebook', 'lenovo')
warehouse.take_to_dep(3, 10, 'Notebook', 'hp')
warehouse.take_to_dep(1, 6, 'Computer', 'Apple')
warehouse.take_to_dep(11, 2, 'Printer', 'Samsung')
warehouse.take_to_dep(1, 17, 'Printer', 'Sony')
print(warehouse)
print()
print(f'Ошибочный ввод департамента: ')
print(warehouse.take_to_dep(2, 4, 'Notebook', 'lenovo'))
print()
print(f'Добавление департамента и запрос большего количества, чем имеется: ')
Notebook.dep_list_add(2)
print(warehouse.take_to_dep(2, 6, 'Notebook', 'lenovo'))
