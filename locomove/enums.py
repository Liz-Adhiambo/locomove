import enum

class Enum(str, enum.Enum):
    pass

class Role(str, enum.Enum):
    CLIENT = "client"
    DRIVER = "driver"
    MOVER = "mover"


    def __str__(self):
        return str(self.value)

