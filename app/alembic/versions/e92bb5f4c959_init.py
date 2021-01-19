"""init

Revision ID: e92bb5f4c959
Revises: 
Create Date: 2021-01-19 10:40:39.780897

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e92bb5f4c959'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user_list',
        sa.Column('email', sa.String, primary_key=True),
        sa.Column('username', sa.String, unique=True, nullable=False),
        sa.Column('password', sa.String, nullable=False)
    )


def downgrade():
    op.drop_table('user_list')
