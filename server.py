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
        self.actions = {}


    def add_device(self, device):
        """Adds a device to the house"""
        self.devices[device.id] = device

    def add_action(self, name, action):
        """Adds a new action that the house will support"""
        self.actions[name] = action

    def run(self, action_name, args=None):
        """Runs action_name on the devices of the house."""
        return self.actions[action_name].run(self.devices)

class DeviceAction(object):
    """Basic action. Each action will decide if it's working on all of the
    devices or just one of them."""
    pass

class ListDevices(DeviceAction):
    def run(self, devices, args=None):
        """Formats a string that lists all devices for the house"""
        return [str(device) for device in devices.values()]

HOME = Home()
HOME.add_device(AirConditioner("electra"))
HOME.add_device(Lamp("bulb"))

HOME.add_action("list_devices", ListDevices())
print HOME.run("list_devices")
