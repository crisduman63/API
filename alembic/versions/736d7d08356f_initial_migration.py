"""initial migration

Revision ID: 736d7d08356f
Revises: c283e541ff5b
Create Date: 2024-12-21 05:04:20.058362

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '736d7d08356f'
down_revision: Union[str, None] = 'c283e541ff5b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
