"""Initial migration.

Revision ID: 10a9f2f8e104
Revises: 
Create Date: 2024-10-16 15:05:17.150174

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10a9f2f8e104'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('finance_report',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('total_sales', sa.Float(), nullable=True),
    sa.Column('expenses', sa.Float(), nullable=True),
    sa.Column('profits', sa.Float(), nullable=True),
    sa.Column('report_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('invoice',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('status', sa.String(length=50), nullable=True),
    sa.Column('issued_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('delivery',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('invoice_id', sa.Integer(), nullable=False),
    sa.Column('delivery_status', sa.String(length=50), nullable=True),
    sa.Column('address', sa.String(length=200), nullable=False),
    sa.Column('delivery_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['invoice_id'], ['invoice.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('delivery')
    op.drop_table('invoice')
    op.drop_table('product')
    op.drop_table('finance_report')
    # ### end Alembic commands ###
