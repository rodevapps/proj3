from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Builder(ABC):
    @property
    @abstractmethod
    def house(self) -> None:
        pass

    @abstractmethod
    def add_door(self) -> None:
        pass

    @abstractmethod
    def add_window(self) -> None:
        pass

    @abstractmethod
    def add_garage(self) -> None:
        pass


class HouseBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._house = Product1()

    @property
    def house(self) -> Product1:
        product = self._house
        self.reset()
        return product

    def add_door(self) -> None:
        self._house.add("PartA1")

    def add_window(self) -> None:
        self._house.add("PartB1")

    def add_garage(self) -> None:
        self._house.add("PartC1")


class Product1():
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="\n")


class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_minimal_house(self) -> None:
        self.builder.add_door()
        self.builder.add_window()

    def build_full_featured_house(self) -> None:
        self.builder.add_door()
        self.builder.add_window()
        self.builder.add_garage()


if __name__ == "__main__":
    director = Director()
    builder = HouseBuilder()
    director.builder = builder

    print("Standard basic product: ")
    director.build_minimal_house()
    builder.house.list_parts()

    print("Standard full featured product: ")
    director.build_full_featured_house()
    builder.house.list_parts()

    print("Custom product: ")
    builder.add_door()
    builder.add_window()
    builder.add_garage()
    builder.house.list_parts()
