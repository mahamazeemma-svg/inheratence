class vehicle:
    def __init__(self,name,maxspeed,milage):
        self.name=name
        self.maxspeed=maxspeed
        self.milage=milage

class bus(vehicle):
    pass

school_bus = bus("volvo",180,12)
print("name:",school_bus.name)
print("maxspeed:",school_bus.maxspeed)
print("milage:",school_bus.milage)