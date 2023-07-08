# Телевизор
# Пульт управления питанием, каналами и громкостью
# Всего настроено 3 канала
# Максимальная громкость - 5

# ИСХОДНОЕ ЗАДАНИЕ
# Создайте программу, имитирующую телевизор как объект.
# У пользователя должна быть возможность вводить номер канала,
# а также увеличивать и уменьшать громкость.
# Программа должна следить за тем, чтобы
# номер канала и уровень громкости оставались в допустимых пределах.

channel_list = {1: "News channel",
                2: "Music channel",
                3: "Cartoon channel"}  # Список каналов


class Tv(object):  # Заголовок класса
    """Пульт управления"""
    status = "off"
    volume = 1
    channel = 1  # Задание исходных значений

    # В методе предоставления еще раззадаю значения по умолчанию,
    # правда не понимаю зачем, но иначе не работает )))
    def __init__(self, status="off", channel=1, volume=1):
        self.status = status
        self.channel = channel
        self.volume = volume

    def __str__(self):  # Формирование статусной строки
        channel_definition = channel_list[self.channel]
        textline = "TV is " + self.status
        textline += "\tChannel " + str(self.channel)
        textline += "\t" + channel_definition
        textline += "\tVolume " + str(self.volume)
        return textline

    def status_changer(self):  # Кнопка включения и выключения
        if self.status == "on":
            self.status = "off"  # Выключение телевизора если он включен
            print("TV switched", self.status)
        else:
            self.status = "on"  # Включение телевизора если он выключен
            print("TV switched", self.status)

    def channel_operation(self, channel_switch):  # Панель кнопок переключения каналов вверх и вниз
        if channel_switch == "up":
            if self.channel < 3:
                self.channel += 1  # Переключение канала вверх
            else:
                print("This is the last channel")  # Отбойник переключения вверх если последний канал
        elif channel_switch == "down":
            if self.channel > 1:
                self.channel -= 1  # Переключение канала вниз
            else:
                print("This is the first channel")  # Отбойник переключения вниз если первый канал

    def volume_operation(self, volume_switch):  # Панель кнопок переключения громкости вверх и вниз
        if volume_switch == "up":
            if self.volume < 5:
                self.volume += 1  # Добавление громкости
            else:
                print("Max volume")  # Отбойник добавления громкости если маскимум
        elif volume_switch == "down":
            if self.volume > 0:
                self.volume -= 1  # Уменьшение громкости
            else:
                print("Mute")  # Отбойник добавления громкости если минимум


def main():
    tv = Tv("off")
    while True:
        print("""
            TV Operation

            0 - Switch on/off
            1 - Channel up
            2 - Channel down
            3 - Volume up
            4 - Volume down
            """)  # Вывод меню телевизора
        print(tv)  # Вывод статуса телевизора
        choice = input("Choice: ")

        # Switch on/off
        if choice == "0":
            tv.status_changer()

        # Channel up
        elif choice == "1":
            if tv.status == "on":
                tv.channel_operation("up")
            else:
                print("No reaction, TV os off")

        # Channel down
        elif choice == "2":
            if tv.status == "on":
                tv.channel_operation("down")
            else:
                print("No reaction, TV os off")

        # Volume up
        elif choice == "3":
            if tv.status == "on":
                tv.volume_operation("up")
            else:
                print("No reaction")

        # Volume down
        elif choice == "4":
            if tv.status == "on":
                tv.volume_operation("down")
            else:
                print("No reaction")

        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")


main()
input("\n\nPress the enter key to exit.")
