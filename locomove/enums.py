import enum

class Enum(str, enum.Enum):
    pass

class Role(Enum):
    CLIENT = "client"
    DRIVER = "driver"
    MOVER = "mover"

