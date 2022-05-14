"""'transactions_table'

Revision ID: 761dc7b650f1
Revises: 22499cd1db72
Create Date: 2022-05-14 20:09:19.257811

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision = '761dc7b650f1'
down_revision = '22499cd1db72'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'transactions',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('monero_transaction_id', sa.String(length=255), nullable=False),
        sa.Column('completed', sa.Boolean(), nullable=False, server_default='false'),
        sa.Column('amount', sa.Integer),
        sa.Column('account_id', sa.Integer, sa.ForeignKey('accounts.id')),
        sa.Column('created_at', sa.DateTime(), nullable=False, server_default=func.now()),
        sa.Column('updated_at', sa.DateTime(), nullable=False, server_default=func.now()),

    )
    op.alter_column(
        'accounts',
        'created_at',
        server_default=func.now(),
    )
    op.alter_column(
        'accounts',
        'updated_at',
        server_default=func.now(),
    )


def downgrade():
    op.drop_table('transactions')
