"""empty message

Revision ID: a528eec66603
Revises: abe9d313d838
Create Date: 2024-04-18 17:58:44.689028

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a528eec66603'
down_revision: Union[str, None] = 'abe9d313d838'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('eseh',sa.Column('id',sa.Integer(),nullable=False,primary_key=True))
    pass


def downgrade() -> None:
    op.drop_table("eseh")
    pass
