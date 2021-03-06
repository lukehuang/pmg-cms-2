"""page-feature-flag

Revision ID: 17570e7e200b
Revises: 4b9d9e9bee64
Create Date: 2016-06-30 10:20:31.170514

"""

# revision identifiers, used by Alembic.
revision = '17570e7e200b'
down_revision = '4b9d9e9bee64'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tmp_organisation_committee')
    op.add_column('page', sa.Column('featured', sa.Boolean(), server_default=sa.text(u'false'), nullable=False))
    op.create_index(op.f('ix_page_featured'), 'page', ['featured'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_page_featured'), table_name='page')
    op.drop_column('page', 'featured')
    op.create_table('tmp_organisation_committee',
    sa.Column('domain', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('committee', sa.VARCHAR(), autoincrement=False, nullable=True)
    )
    ### end Alembic commands ###
