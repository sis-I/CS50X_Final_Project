"""column type change

Revision ID: 91531c64de7e
Revises: 
Create Date: 2025-01-27 00:19:02.296425

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91531c64de7e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dictionary1')
    op.alter_column('dictionary', 'reference',
               existing_type=sa.VARCHAR(length=20),
               type_=sa.String(length=200),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('dictionary', 'reference',
               existing_type=sa.String(length=200),
               type_=sa.VARCHAR(length=20),
               existing_nullable=True)
    op.create_table('dictionary1',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('amharic', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('english', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('wordtype', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('reference', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='dictionary1_pkey1')
    )
    # ### end Alembic commands ###
