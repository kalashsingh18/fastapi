"""create post table

Revision ID: abe9d313d838
Revises: 
Create Date: 2024-04-17 04:52:33.832751

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'abe9d313d838'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('esehi',sa.Column('id',sa.Integer(),nullable=False,primary_key=True))
    pass


def downgrade() -> None:
    op.drop_table("esehi")
    pass
