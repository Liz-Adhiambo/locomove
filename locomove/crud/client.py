from typing import List
from locomove.models.client import Client
from locomove.schemas.client import Client as ClientSchema
from locomove.db import get_db


def get_clients() -> List[ClientSchema]:
    db = next(get_db())
    clients = db.query(Client).all()
    return clients

def get_client(id: str) -> ClientSchema:
    db = next(get_db())
    client = db.query(Client).filter(Client.id == id).first()
    return client


