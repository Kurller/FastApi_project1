"""create scrape table

Revision ID: 9a9ba130be9e
Revises: 
Create Date: 2024-03-11 13:22:37.386446

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9a9ba130be9e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    op.create_table('scrape',sa.Column('id',sa.Integer(),nullable=False,primary_key=True),
                    sa.Column('companyNames',sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_table('scrape')
    pass