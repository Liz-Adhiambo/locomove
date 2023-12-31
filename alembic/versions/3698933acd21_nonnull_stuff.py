"""nonnull stuff

Revision ID: 3698933acd21
Revises: b08e1b81c3ad
Create Date: 2023-08-17 19:56:05.631807

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3698933acd21'
down_revision: Union[str, None] = 'b08e1b81c3ad'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('drivers', 'vehicle_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('vehicles', 'driver_id',
               existing_type=sa.UUID(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('vehicles', 'driver_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('drivers', 'vehicle_id',
               existing_type=sa.UUID(),
               nullable=False)
    # ### end Alembic commands ###
