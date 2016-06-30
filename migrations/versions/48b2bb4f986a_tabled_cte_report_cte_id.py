"""tabled-cte-report-cte-id

Revision ID: 48b2bb4f986a
Revises: 8939e1ee328
Create Date: 2016-06-30 12:21:07.236513

"""

# revision identifiers, used by Alembic.
revision = '48b2bb4f986a'
down_revision = '8939e1ee328'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tabled_committee_report', 'committee_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.create_index(op.f('ix_tabled_committee_report_committee_id'), 'tabled_committee_report', ['committee_id'], unique=False)
    op.drop_constraint(u'tabled_committee_report_committee_id_fkey', 'tabled_committee_report', type_='foreignkey')
    op.create_foreign_key(op.f('fk_tabled_committee_report_committee_id_committee'), 'tabled_committee_report', 'committee', ['committee_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_tabled_committee_report_committee_id_committee'), 'tabled_committee_report', type_='foreignkey')
    op.create_foreign_key(u'tabled_committee_report_committee_id_fkey', 'tabled_committee_report', 'committee', ['committee_id'], ['id'], ondelete=u'SET NULL')
    op.drop_index(op.f('ix_tabled_committee_report_committee_id'), table_name='tabled_committee_report')
    op.alter_column('tabled_committee_report', 'committee_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    ### end Alembic commands ###
