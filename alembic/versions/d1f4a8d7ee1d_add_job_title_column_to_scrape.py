"""add job_title column to scrape

Revision ID: d1f4a8d7ee1d
Revises: 9a9ba130be9e
Create Date: 2024-03-11 13:25:19.271803

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd1f4a8d7ee1d'
down_revision: Union[str, None] = '9a9ba130be9e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('scrape',sa.Column('job_titles',sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_column('scrape','job_titles')
    pass