def print_info(name, surname, year, city, email, phone):
    """Выводит информацию о пользователе.

    Именованные параметры:
    name -- имя
    surname -- фамилия
    year -- год рождения
    city  -- город проживания
    email -- эл. почта
    phone -- номер телефона
    """
    print(name, surname, year, city, email, phone)


print_info(name='Alex',surname='Alexeev', year=1991, city='Moscow',
           email='alex@mail.ru', phone=738247283)
print_info(name='Ivan',surname='Ivanov', year=1993, city='SPB',
           email='iv@mail.ru', phone=2351635712)
