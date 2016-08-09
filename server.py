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
        self.devices, res =  self.actions[action_name].run(self.devices, args)
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


HOME = Home()
HOME.add_device(AirConditioner("electra"))
HOME.add_device(Lamp("bulb"))

HOME.add_action("list_devices", ListDevices())
HOME.add_action("switch", Switch())

print HOME.run("list_devices")
HOME.run("switch", ["bulb", "on"])
HOME.run("switch", ["electra", "on"])
print HOME.run("list_devices")
HOME.run("switch", ["electra", "off"])
print HOME.run("list_devices")
