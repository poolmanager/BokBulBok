import random, sys, os
from typing import Literal
from pynput.keyboard import Key, Listener

class games:
    def __init__(self, game: Literal["뽑기", "복불복"]):
        self.game = game

    def BokBulBokMixin(self, input: list) -> list:
        out = []
        
        for _ in range(len(input)):
            _random = random.choice(input)
            input.remove(_random)
            out.append(_random)

        return out

    def BokBulBokSortNumber(self, number: int) -> list:
        out = []
        
        for i in range(number):
            out.append(i)

        return out

    def BokBulBokFilter(self, number: int, options: list):
        if len(options) <= 1:
            raise ValueError

        if number <= 1:
            raise ValueError

        if number != len(options):
            raise IndexError

    def BokBulBok(self, number: int, options: list) -> str:
        self.BokBulBokFilter(number, options)
        
        _number = self.BokBulBokSortNumber(number)
        _mixed = self.BokBulBokMixin(options)

        _out = []

        for i in range(len(_mixed)):
            _out.append("{0}: {1}".format(_number[i], _mixed[i]))

        return "\n".join(_out)

option = 0
menus = ["뽑기", "복불복"]
options = {
    "0": "뽑기",
    "1": "복불복"
}
option_changed = False

def on_press(key):
    global option, menus, options
    if key == Key.up:
        option += 1

        if option > 1:
            option = 0

        print(
            f"""
            뽑기
            복불복
            """
            .center(round(os.get_terminal_size().columns * os.get_terminal_size().lines))
            .replace(menus[option], f"> {menus[option]}"),
            end="\r"
        )

    if key == Key.down:
        option -= 1

        if option < 0:
            option = 1

        print(
            f"""
            뽑기
            복불복
            """
            .center(round(os.get_terminal_size().columns * os.get_terminal_size().lines))
            .replace(menus[option], f"> {menus[option]}"),
            end="\r"
        )

    if key == Key.enter:
        if options[str(option)] == "복불복":
            print("")

with Listener(
    on_press=on_press
) as listener:
    listener.join()
