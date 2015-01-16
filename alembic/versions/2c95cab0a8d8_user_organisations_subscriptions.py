"""User organisations & subscriptions.

Revision ID: 2c95cab0a8d8
Revises: 485814144844
Create Date: 2015-01-16 09:23:33.359196

"""

# revision identifiers, used by Alembic.
revision = '2c95cab0a8d8'
down_revision = '485814144844'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('organisation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('domain', sa.String(length=100), nullable=False),
    sa.Column('paid_subscriber', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('expiry', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_committee',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('committee_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['committee_id'], ['committee.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.create_table('organisation_committee',
    sa.Column('organisation_id', sa.Integer(), nullable=True),
    sa.Column('committee_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['committee_id'], ['committee.id'], ),
    sa.ForeignKeyConstraint(['organisation_id'], ['organisation.id'], )
    )
    op.add_column(u'user', sa.Column('organisation_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'user', 'organisation', ['organisation_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_column(u'user', 'organisation_id')
    op.drop_table('organisation_committee')
    op.drop_table('user_committee')
    op.drop_table('organisation')
    ### end Alembic commands ###
