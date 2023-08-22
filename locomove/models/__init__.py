from sqlalchemy.orm import configure_mappers

from locomove.models.user import *
from locomove.models.client import *
from locomove.models.driver import *
from locomove.models.mover import *
from locomove.models.vehicle import *

configure_mappers()
