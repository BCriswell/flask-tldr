"""empty message

Revision ID: 1c5c47de9e3b
Revises: 585c0b1d4748
Create Date: 2015-11-10 17:31:17.271528

"""

# revision identifiers, used by Alembic.
revision = '1c5c47de9e3b'
down_revision = '585c0b1d4748'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('summaries', sa.Column('posted_date', sa.Date(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('summaries', 'posted_date')
    ### end Alembic commands ###