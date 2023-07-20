import threading
import time

# ANSI Escape-последовательности для цветов
COLORS = {
    "RED": "\033[91m",
    "GREEN": "\033[92m",
    "BLUE": "\033[94m",
    "RESET": "\033[0m"
}

# Класс для представления таймера
class Timer:
    def __init__(self, name, duration, callback, color):
        self.name = name
        self.duration = duration
        self.callback = callback
        self.color = color
        self.is_running = False

    def start(self):
        self.is_running = True
        print(f"{self.color}Таймер '{self.name}' запущен на {self._format_time(self.duration)}.{COLORS['RESET']}")
        threading.Thread(target=self._countdown).start()

    def stop(self):
        self.is_running = False
        print(f"{self.color}Таймер '{self.name}' остановлен.{COLORS['RESET']}")

    def _countdown(self):
        start_time = time.time()
        while self.is_running:
            time.sleep(1)
            elapsed_time = time.time() - start_time
            remaining_time = self.duration - elapsed_time
            if remaining_time <= 0:
                self.is_running = False
                self.callback()
            else:
                print(f"{self.color}Таймер '{self.name}': Осталось {self._format_time(remaining_time)}.{COLORS['RESET']}")
        print(f"{self.color}Таймер '{self.name}' завершен.{COLORS['RESET']}")

    def _format_time(self, seconds):
        minutes = int(seconds // 60)
        seconds = int(seconds % 60)
        return f"{minutes:02}:{seconds:02}"

# Функция, которая будет вызвана при окончании таймера
def timer_callback():
    print(f"{COLORS['GREEN']}Время вышло! Ваше действие.{COLORS['RESET']}")

# Функция для получения времени таймера от пользователя
def get_timer_duration():
    while True:
        user_input = input("Введите время таймера в формате 'минуты:секунды': ")
        try:
            minutes, seconds = map(int, user_input.split(":"))
            if minutes >= 0 and seconds >= 0:
                return minutes * 60 + seconds
            else:
                print("Время должно быть положительным.")
        except ValueError:
            print("Некорректный формат времени. Попробуйте еще раз.")

# Создаем несколько таймеров с разными цветами
timer1 = Timer("Таймер 1", get_timer_duration(), timer_callback, COLORS["RED"])
timer2 = Timer("Таймер 2", get_timer_duration(), timer_callback, COLORS["GREEN"])
timer3 = Timer("Таймер 3", get_timer_duration(), timer_callback, COLORS["BLUE"])

# Запускаем таймеры
timer1.start()
timer2.start()
timer3.start()

# Ждем, пока все таймеры завершатся
while timer1.is_running or timer2.is_running or timer3.is_running:
    pass

print("Все таймеры завершены.")
