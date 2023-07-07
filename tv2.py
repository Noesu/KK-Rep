# Телевизор
# Пульт управления питанием, каналами и громкостью
# Всего настроено 3 канала
# Максимальная громкость - 5

# ИСХОДНОЕ ЗАДАНИЕ
# Создайте программу, имитирующую телевизор как объект.
# У пользователя должна быть возможность вводить номер канала,
# а также увеличивать и уменьшать громкость.
# Программа допжна следить за тем, чтобы
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
        channel_definition = channel_list[Tv.channel]
        textline = "TV is " + Tv.status
        textline += "\tChannel " + str(Tv.channel)
        textline += "\t" + channel_definition
        textline += "\tVolume " + str(Tv.volume)
        return textline

    @staticmethod
    def status_changer():  # Кнопка включения и выключения
        if Tv.status == "on":
            Tv.status = "off"  # Выключение телевизора если он включен
            print("TV switched", Tv.status)
        else:
            Tv.status = "on"  # Включение телевизора если он выключен
            print("TV switched", Tv.status)

    @staticmethod
    def channel_operation(channel_switch):  # Панель кнопок переключения каналов вверх и вниз
        if channel_switch == "up":
            if Tv.channel < 3:
                Tv.channel += 1  # Переключение канала вверх
            else:
                print("This is the last channel")  # Отбойник переключения вверх если последний канал
        elif channel_switch == "down":
            if Tv.channel > 1:
                Tv.channel -= 1  # Переключение канала вниз
            else:
                print("This is the first channel")  # Отбойник переключения вниз если первый канал

    @staticmethod
    def volume_operation(volume_switch):  # Панель кнопок переключения громкости вверх и вниз
        if volume_switch == "up":
            if Tv.volume < 5:
                Tv.volume += 1  # Добавление громкости
            else:
                print("Max volume")  # Отбойник добавления громкости если маскимум
        elif volume_switch == "down":
            if Tv.volume > 0:
                Tv.volume -= 1  # Уменьшение громкости
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
            Tv.status_changer()

        # Channel up
        elif choice == "1":
            if Tv.status == "on":
                tv.channel_operation("up")
            else:
                print("No reaction, TV os off")

        # Channel down
        elif choice == "2":
            if Tv.status == "on":
                tv.channel_operation("down")
            else:
                print("No reaction, TV os off")

        # Volume up
        elif choice == "3":
            if Tv.status == "on":
                tv.volume_operation("up")
            else:
                print("No reaction")

        # Volume down
        elif choice == "4":
            if Tv.status == "on":
                tv.volume_operation("down")
            else:
                print("No reaction")

        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")


main()
input("\n\nPress the enter key to exit.")
