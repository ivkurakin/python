user_time = int(input('Введи время в секундах: '))  # Запрос времени от пользователя
hours = user_time // 3600  # расчет часа
minutes = user_time % 3600 // 60 # расчет минуты
seconds = user_time % 60  # расчет секунды
print(f"Время: {hours:02d}:{minutes:02d}:{seconds:02d}")
