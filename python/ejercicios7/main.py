from dog import Animal
from wheel import Wheel

fido = Animal("fido", "red", 2020, True)
fido.get_info()

wheel = Wheel("red", 11)
print(wheel.get_velocity())