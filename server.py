"""Server module that will add new devices, turn them on and off etc"""

class Device(object):

    """Represents a device (such as air conditioner) in the system."""
    def __init__(self, device_id):
        self.id = device_id
        self.state = "on"

    def __str__(self):
        """Returns commaa seperated string of the device base values."""
        return "{},{}".format(self.id, self.state)

class AirConditioner(Device):
    name = "airconditioner"
    """Represents an airconditioner."""

    def __init__(self, device_id):
        super(AirConditioner, self).__init__(device_id)
        self.temperature = 20

    def __str__(self):
        return "{},{},{},{}".format(self.id, AirConditioner.name, self.state,
                                 self.temperature)
                              

    def set_value(self, temperature):
        self.temperature = temperature

class Lamp(Device):
    name = "lamp"
    """Represents an airconditioner."""
    def __str__(self):
        return "{},{},{}".format(self.id, Lamp.name, self.state)
                

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
        self.devices, res = self.actions[action_name].run(self.devices, args)
        return res

class DeviceAction(object):
    """Basic action. Each action will decide if it's working on all of the
    devices or just one of them."""
    pass

class ListDevices(DeviceAction):
    def run(self, devices, args=None):
        """Formats a string that lists all devices for the house"""
        return devices, [str(device) for device in devices.values()]

class Switch(DeviceAction):
    def run(self, devices, args=None):
        """Sets a new state for a device"""
        devices[args[0]].state = args[1]
        return devices, None

class SetValue(DeviceAction):
    def run(self, devices, args=None):
        """Sets a new value for a device"""
        devices[args[0]].set_value(args[1])
        return devices, None



HOME = Home()
HOME.add_device(Lamp("1"))
HOME.add_device(AirConditioner("2"))

HOME.add_action("list_devices", ListDevices())
HOME.add_action("switch", Switch())
HOME.add_action("set_value", SetValue())

print HOME.run("list_devices")

HOME.run("switch", ["1", "off"])
print HOME.run("list_devices")

HOME.run("switch", ["2", "off"])
print HOME.run("list_devices")

HOME.run("set_value", ["2", "30"])
print HOME.run("list_devices")
