# задача2
time_sec = int(input("Введите время в секундах: "))
hour = time_sec // 3600
ost = time_sec % 3600
minute = ost // 60
sec = ost % 60
print(f"Время: {hour}:{minute}:{sec}")
