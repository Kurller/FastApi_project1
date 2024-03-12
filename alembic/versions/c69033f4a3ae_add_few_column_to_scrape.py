"""add few column to scrape

Revision ID: c69033f4a3ae
Revises: d8220d7cfe2a
Create Date: 2024-03-11 13:29:49.702503

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c69033f4a3ae'
down_revision: Union[str, None] = 'd8220d7cfe2a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('scrape',sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('scrape_user_fk',source_table='scrape',referent_table='user',
                          local_cols=['owner_id'],remote_cols=['id'],ondelete='CASCADE')
    pass


def downgrade():
    op.drop_constraint('scrape_user_fk',table_name='scrape')
    op.drop_column('scrape','owner_id')
    pass