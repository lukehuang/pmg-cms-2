"""content_body_summary

Revision ID: 21fb154d61b5
Revises: a91338ba772
Create Date: 2015-02-06 12:15:21.256299

"""

# revision identifiers, used by Alembic.
revision = '21fb154d61b5'
down_revision = 'a91338ba772'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('content', sa.Column('body', sa.Text(), nullable=True))
    op.add_column('content', sa.Column('summary', sa.Text(), nullable=True))
    op.execute("update content set body = rt.body, summary = rt.summary from rich_text rt where rich_text_id = rt.id")
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('content', 'summary')
    op.drop_column('content', 'body')
    ### end Alembic commands ###
