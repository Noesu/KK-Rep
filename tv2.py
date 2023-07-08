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

from enum import Enum, IntEnum
from typing import Optional


MIN_VOLUME_LEVEL = 0
MAX_VOLUME_LEVEL = 5

MIN_CHANNEL_NUMBER = 1
MAX_CHANNEL_NUMBER = 3


class TVPowerStatus(str, Enum):
    POWER_ON = "ON"
    POWER_OFF = "OFF"


class TVButton(str, Enum):
    CHANNEL_UP = "CHANNEL_UP"
    CHANNEL_DOWN = "CHANNEL_DOWN"

    VOLUME_UP = "VOLUME_UP"
    VOLUME_DOWN = "VOLUME_DOWN"


class TVMenuOption(IntEnum):
    SWITCH_POWER = 0
    CHANNEL_UP = 1
    CHANNEL_DOWN = 2
    VOLUME_UP = 3
    VOLUME_DOWN = 4

    @classmethod
    def from_user_input(cls, user_input: str) -> Optional["TVMenuOption"]:
        try:
            return TVMenuOption(int(user_input))
        except ValueError:
            return None


class TVChannelNumber(IntEnum):
    NEWS = 1
    MUSIC = 2
    CARTOON = 3


CHANNEL_NUMBER_TO_NAME = {
    TVChannelNumber.NEWS: "News channel",
    TVChannelNumber.MUSIC: "Music channel",
    TVChannelNumber.CARTOON: "Cartoon channel",
}


class TVRemote:
    """Пульт управления ТВ"""

    def __init__(
        self,
        power_status: TVPowerStatus,
        channel_number: TVChannelNumber,
        volume: int,
    ):
        self.power_status = power_status
        self.channel_number = channel_number
        self.volume = volume

    @property
    def menu(self) -> str:
        return (
            """
            TV Operation

            0 - Switch on/off
            1 - Channel up
            2 - Channel down
            3 - Volume up
            4 - Volume down
            """
        )

    @property
    def state(self) -> str:
        return (
            f"TV is {self.power_status}\t "
            f"Channel {self.channel_number}\t "
            f"{CHANNEL_NUMBER_TO_NAME[self.channel_number]}\t "
            f"Volume {self.volume}"
        )

    def switch_power(self) -> None:
        if self.power_status == TVPowerStatus.POWER_ON:
            self.power_status = TVPowerStatus.POWER_OFF
        else:
            self.power_status = TVPowerStatus.POWER_ON

        print(f"TV switched {self.power_status}")

    def switch_channel(self, button: TVButton):
        if button == TVButton.CHANNEL_UP:
            if self.channel_number < MAX_CHANNEL_NUMBER:
                self.channel_number += 1
            else:
                print("This is the last channel")

        elif button == TVButton.CHANNEL_DOWN:
            if self.channel_number > MIN_CHANNEL_NUMBER:
                self.channel_number -= 1
            else:
                print("This is the first channel")

    def switch_volume(self, button: TVButton):
        if button == TVButton.VOLUME_UP:
            if self.volume < MAX_VOLUME_LEVEL:
                self.volume += 1
            else:
                print("Max volume")

        elif button == TVButton.VOLUME_DOWN:
            if self.volume > MIN_VOLUME_LEVEL:
                self.volume -= 1
            else:
                print("Mute")


def main():
    tv_remote = TVRemote(
        power_status=TVPowerStatus.POWER_OFF,
        channel_number=TVChannelNumber.NEWS,
        volume=MIN_VOLUME_LEVEL + 1,
    )

    running = True
    while running:
        print(tv_remote.menu)
        print(tv_remote.state)

        user_input = input("Choice: ")

        menu_option = TVMenuOption.from_user_input(user_input)
        if menu_option is None:
            print(f"\nSorry, but '{user_input}' isn't a valid menu option.")
            continue

        # Switch on/off
        if menu_option == TVMenuOption.SWITCH_POWER:
            tv_remote.switch_power()

        elif menu_option in TVMenuOption:
            if tv_remote.power_status == TVPowerStatus.POWER_OFF:
                print("No reaction, TV is off")
                continue

        # Channel up
        if menu_option == TVMenuOption.CHANNEL_UP:

            tv_remote.switch_channel(button=TVButton.CHANNEL_UP)

        # Channel down
        elif menu_option == TVMenuOption.CHANNEL_DOWN:
            tv_remote.switch_channel(button=TVButton.CHANNEL_DOWN)

        # Volume up
        elif menu_option == TVMenuOption.VOLUME_UP:
            tv_remote.switch_volume(button=TVButton.VOLUME_UP)

        # Volume down
        elif menu_option == TVMenuOption.VOLUME_DOWN:
            tv_remote.switch_volume(button=TVButton.VOLUME_DOWN)

    input("\n\nPress the enter key to exit.")


if __name__ == '__main__':
    main()
