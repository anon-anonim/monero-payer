"""accounts_table

Revision ID: 22499cd1db72
Revises: 
Create Date: 2022-04-25 21:53:44.174781

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22499cd1db72'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'accounts',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('address', sa.String(length=255), nullable=False, unique=True),
        sa.Column('in_use', sa.Boolean(), nullable=False, server_default='false'),
        sa.Column('last_issued_at', sa.DateTime(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False, server_default='now()'),
        sa.Column('updated_at', sa.DateTime(), nullable=False, server_default='now()'),
    )
    pass


def downgrade():
    op.drop_table('accounts')
