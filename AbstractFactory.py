from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def create_house(self) -> AbstractHouse:
        pass

    @abstractmethod
    def create_car(self) -> AbstractCar:
        pass

    @abstractmethod
    def create_plane(self) -> AbstractPlane:
        pass


class AbstractHouse(ABC):
    @abstractmethod
    def build(self) -> str:
        pass

class AbstractCar(ABC):
    @abstractmethod
    def run(self) -> str:
        pass

class AbstractPlane(ABC):
    @abstractmethod
    def fly(self) -> str:
        pass


class ConcreteFactory1(AbstractFactory):
    def create_house(self) -> AbstractHouse:
        return ConcreteMiniHouse()

    def create_car(self) -> AbstractCar:
        return ConcreteMiniCar()

    def create_plane(self) -> AbstractPlane:
        return ConcreteMiniPlane()

class ConcreteFactory2(AbstractFactory):
    def create_house(self) -> AbstractHouse:
        return ConcreteMediumHouse()

    def create_car(self) -> AbstractCar:
        return ConcreteMediumCar()

    def create_plane(self) -> AbstractPlane:
        return ConcreteMediumPlane()

class ConcreteFactory3(AbstractFactory):
    def create_house(self) -> AbstractHouse:
        return ConcreteBigHouse()

    def create_car(self) -> AbstractCar:
        return ConcreteBigCar()

    def create_plane(self) -> AbstractPlane:
        return ConcreteBigPlane()


class ConcreteMiniHouse(AbstractHouse):
    def build(self) -> str:
        return "Mini house is building..."

class ConcreteMediumHouse(AbstractHouse):
    def build(self) -> str:
        return "Medium house is building..."

class ConcreteBigHouse(AbstractHouse):
    def build(self) -> str:
        return "Big house is building..."

class ConcreteMiniCar(AbstractCar):
    def run(self) -> str:
        return "Mini car is running..."

class ConcreteMediumCar(AbstractCar):
    def run(self) -> str:
        return "Medium car is running..."

class ConcreteBigCar(AbstractCar):
    def run(self) -> str:
        return "Big car is running..."

class ConcreteMiniPlane(AbstractPlane):
    def fly(self) -> str:
        return "Mini plane is flying..."

class ConcreteMediumPlane(AbstractPlane):
    def fly(self) -> str:
        return "Medium plane is flying..."

class ConcreteBigPlane(AbstractPlane):
    def fly(self) -> str:
        return "Big plane is flying..."


def client_code(factory: AbstractFactory) -> None:
    house = factory.create_house()
    car = factory.create_car()
    plane = factory.create_plane()

    print(house.build())
    print(car.run())
    print(plane.fly())


if __name__ == "__main__":
    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteFactory1())

    print("Client: Testing the same client code with the second factory type:")
    client_code(ConcreteFactory2())

    print("Client: Testing the same client code with the third factory type:")
    client_code(ConcreteFactory3())
