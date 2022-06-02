"""empty message

Revision ID: b31f8ae94c28
Revises: 58fef190d428
Create Date: 2022-05-31 10:36:16.922242

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b31f8ae94c28'
down_revision = '58fef190d428'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'Show', 'Venue', ['venue_id'], ['id'])
    op.create_foreign_key(None, 'Show', 'Artist', ['artist_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Show', type_='foreignkey')
    op.drop_constraint(None, 'Show', type_='foreignkey')
    # ### end Alembic commands ###