"""Server module that will add new devices, turn them on and off etc"""

class Device(object):

    """Represents a device (such as air conditioner) in the system."""
    def __init__(self, device_id):
        self.id = device_id
        self.state = "off"

    def __str__(self):
        """Returns commaa seperated string of the device base values."""
        return "{},{}".format(self.id, self.state)

class AirConditioner(Device):
    """Represents an airconditioner."""

    def __init__(self, device_id):
        super(AirConditioner, self).__init__(device_id)
        self.temperature = 0

    def __str__(self):
        return "{},{}".format(super(AirConditioner, self).__str__(),
                              str(self.temperature))

    def increase_temperature(self, degrees):
        """Increases temperature"""
        self.temperature += degrees

    def decrease_temperature(self, degrees):
        """Increases temperature"""
        self.temperature -= degrees


class Lamp(Device):
    """Represents an airconditioner."""

class Home(object):
    """Represents a home that has a lot of devices"""
    def __init__(self):
        self.devices = {}

    def add(self, device):
        """Adds a device to the house"""
        self.devices[device.id] = device

    def list_devices(self):
        """Formats a string that lists all devices for the house"""
        return [str(device) for device in self.devices.values()]

HOME = Home()
HOME.add(AirConditioner("electra"))
HOME.add(Lamp("bulb"))
print HOME.list_devices()
