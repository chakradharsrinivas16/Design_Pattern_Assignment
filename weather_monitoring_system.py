import time
from abc import ABC, abstractmethod

class WeatherStation:
    def __init__(self):
        self.observers = []  # List to store registered observers
        self.previous_weather_data = None  # Variable to track previous weather data

    def register_observer(self, observer):
        self.observers.append(observer)  # Add an observer to the list of registered observers

    def unregister_observer(self, observer):
        self.observers.remove(observer)  # Remove an observer from the list of registered observers

    def notify_observers(self, weather_data):
        for observer in self.observers:
            observer.update(weather_data)  # Notify each observer by calling their update method with the weather data

    def get_weather_data(self):
        temperature = 25.5
        humidity = 60.0
        pressure = 1013.25
        return {'temperature': temperature, 'humidity': humidity, 'pressure': pressure}  # Simulated method to fetch weather data

    def start_monitoring(self):
        while True:  # Run indefinitely
            weather_data = self.get_weather_data()  # Get the current weather data
            if weather_data != self.previous_weather_data:  # Check if the weather data has changed
                self.notify_observers(weather_data)  # Notify the observers about the updated weather data
                self.previous_weather_data = weather_data  # Update the previous weather data

            time.sleep(5)  # Delay between iterations (5 seconds)

class DisplayDevice(ABC):
    @abstractmethod
    def update(self, weather_data):
        pass  # Abstract method to be implemented by the subclasses

class MobileAppDisplay(DisplayDevice):
    def update(self, weather_data):
        print("Hi User, here is the update on weather data")
        print("Mobile App Display:")
        print(f"Temperature: {weather_data['temperature']}")
        print(f"Humidity: {weather_data['humidity']}")
        print(f"Pressure: {weather_data['pressure']}")
        print()

class WebInterfaceDisplay(DisplayDevice):
    def update(self, weather_data):
        print("Hi User, here is the update on weather data")
        print("Web Interface Display:")
        print(f"Temperature: {weather_data['temperature']}")
        print(f"Humidity: {weather_data['humidity']}")
        print(f"Pressure: {weather_data['pressure']}")
        print()

class DesktopApplicationDisplay(DisplayDevice):
    def update(self, weather_data):
        print("Hi User, here is the update on weather data")
        print("Desktop Application Display:")
        print(f"Temperature: {weather_data['temperature']}")
        print(f"Humidity: {weather_data['humidity']}")
        print(f"Pressure: {weather_data['pressure']}")
        print()

if __name__ == '__main__':
    weather_station = WeatherStation()

    mobile_app_display = MobileAppDisplay()
    web_interface_display = WebInterfaceDisplay()
    desktop_application_display = DesktopApplicationDisplay()

    weather_station.register_observer(mobile_app_display)  # Register the mobile app display device
    weather_station.register_observer(web_interface_display)  # Register the web interface display device
    weather_station.register_observer(desktop_application_display)  # Register the desktop application display device

    weather_station.start_monitoring()  # Start monitoring the weather data
