# Design_Pattern_Assignment

## Weather Monitoring System
The Weather Monitoring System is a Python application that implements the Observer design pattern to monitor weather conditions and notify multiple display devices about changes in the weather. It establishes a one-to-many relationship between the weather station (subject) and the display devices (observers).

### Design Pattern: Observer
The Observer design pattern is used to establish a dependency between objects, such that when the state of one object (subject) changes, all its dependents (observers) are automatically notified and updated.

In the Weather Monitoring System, the Observer pattern is implemented as follows:

- Subject: The WeatherStation class acts as the subject or the weather station. It maintains a list of registered observers (observers) and provides methods to register and unregister observers. It also defines a method to notify all registered observers when new weather data is available.

- Observers: The DisplayDevice class is the abstract base class for observers or display devices. It defines an abstract method update(weather_data) that concrete observers must implement. This method is called by the subject to update the observer with the latest weather data.

- Concrete Observers: The MobileAppDisplay, WebInterfaceDisplay, and DesktopApplicationDisplay classes are concrete observers or display devices. They inherit from the DisplayDevice base class and implement the update method to handle the received weather data. Each observer is responsible for updating its own user interface and displaying the weather information.

### Usage
- The WeatherStation class provides methods to register and unregister observers, allowing for the addition and removal of display devices without modifying the existing code.

- The DisplayDevice abstract base class defines the update method that must be implemented by concrete observers. To add a new display device, create a new subclass of DisplayDevice and implement the update method with the desired functionality.

- The WeatherStation class automatically notifies all registered observers when new weather data is available. The observers receive the weather data through the update method and can update their user interfaces accordingly.

- To start monitoring the weather, create an instance of the WeatherStation class and register the desired display devices using the register_observer method. Call the start_monitoring method to initiate the continuous weather monitoring process.


## Vehicle Manufacturing System
The Vehicle Manufacturing System is a Python application that utilizes the Factory Method design pattern to create different types of vehicles based on user input. The system allows users to specify the type of vehicle they want to manufacture (car, motorcycle, or truck) and provides the corresponding factory to create the desired vehicle object.

### Design Pattern: Factory Method
The Factory Method design pattern is used in this system to encapsulate the vehicle creation logic and ensure the correct type of vehicle is created based on user input. It provides an interface for creating objects, but defers the decision of which object to create to the subclasses. In this way, the Vehicle Factory acts as an abstract creator, and each specific vehicle factory subclass (CarFactory, MotorcycleFactory, TruckFactory) implements the factory method create_vehicle() to create the corresponding vehicle object.

By using the Factory Method pattern, the system achieves the following benefits:

 - Decouples the client code from the specific vehicle classes, allowing for flexibility and extensibility in adding new vehicle types.
- Provides a way to create objects without exposing the instantiation logic to the client.
- Ensures that the correct type of vehicle object is created based on user input, without the need for conditional statements or switch cases.

### Classes and Usage

The system consists of the following classes:

- Vehicle (Abstract Class): Represents the abstract product, defining the interface for all vehicle objects. It declares the abstract method get_details() which is implemented by concrete vehicle subclasses.

- Concrete Products (Car, Motorcycle, Truck): Represents the concrete vehicle subclasses that implement the Vehicle interface. Each subclass defines its specific attributes such as the number of wheels, maximum speed, and seating capacity. They also implement the get_details() method to provide details about the vehicle.

- Vehicle Factory (Abstract Class): Represents the abstract creator that declares the factory method create_vehicle(). It acts as an interface for creating vehicle objects.

- Concrete Creators (CarFactory, MotorcycleFactory, TruckFactory): Represent the concrete vehicle factory subclasses that extend the VehicleFactory class and implement the create_vehicle() method. Each factory creates a specific type of vehicle object based on user input.
