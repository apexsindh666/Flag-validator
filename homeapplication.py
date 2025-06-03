from abc import ABC, abstractmethod


class SmartDevice(ABC):
    def __init__(self, name):
        self._name = name
        self.__is_on = False 

    @abstractmethod
    def operate(self):
        pass

    def show_status(self):
        status = "ON" if self.__is_on else "OFF"
        print(f"{self._name} is {status}.")

    def _turn_on(self):
        self.__is_on = True

    def _turn_off(self):
        self.__is_on = False

    def _is_device_on(self):
        return self.__is_on



class SmartLight(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self.__brightness = 0 

    def operate(self):
        self._turn_on()
        self.__brightness = 70
        print(f"{self._name} turned ON with brightness {self.__brightness}%.")

    def get_brightness(self):
        return self.__brightness

    def set_brightness(self, value):
        if 0 <= value <= 100:
            self.__brightness = value
        else:
            print("Brightness must be between 0 and 100.")


class SmartFan(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self.__speed = 'Off'

    def operate(self):
        self._turn_on()
        self.__speed = "Medium"
        print(f"{self._name} turned ON at {self.__speed} speed.")

    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        if speed in ["Low", "Medium", "High"]:
            self.__speed = speed
        else:
            print("Speed must be 'Low', 'Medium', or 'High'.")



class SmartAC(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self.__temperature = 0

    def operate(self):
        self._turn_on()
        self.__temperature = 24
        print(f"{self._name} turned ON with temperature set to {self.__temperature}°C.")

    def get_temperature(self):
        return self.__temperature

    def set_temperature(self, temp):
        if 16 <= temp <= 30:
            self.__temperature = temp
        else:
            print("Temperature must be between 16 and 30°C.")



light = SmartLight("Living Room Light")
fan = SmartFan("Bedroom Fan")
ac = SmartAC("Office AC")


light.operate()
light.show_status()

fan.operate()
fan.show_status()

ac.operate()
ac.show_status()

print("\nAttempting to directly modify private attributes:")
try:
    light.__brightness = 100
except AttributeError as e:
    print("Error:", e)

try:
    fan.__speed = "High"
except AttributeError as e:
    print("Error:", e)

try:
    ac.__temperature = 20
except AttributeError as e:
    print("Error:", e)


print("\nUpdating device settings using setters:")
light.set_brightness(85)
print("Updated Brightness:", light.get_brightness())

fan.set_speed("High")
print("Updated Speed:", fan.get_speed())

ac.set_temperature(22)
print("Updated Temperature:", ac.get_temperature())
