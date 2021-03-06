"""event_tweaks

Revision ID: e88bc62b6e4
Revises: 4d3c2b4ceacb
Create Date: 2015-03-17 14:04:09.394924

"""

# revision identifiers, used by Alembic.
revision = 'e88bc62b6e4'
down_revision = '4d3c2b4ceacb'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('event_files', 'event_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('event_files', 'file_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('event_files', u'type')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('event_files', sa.Column(u'type', postgresql.ENUM(u'related', name=u'event_file_type_enum'), autoincrement=False, nullable=False))
    op.alter_column('event_files', 'file_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('event_files', 'event_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    ### end Alembic commands ###
