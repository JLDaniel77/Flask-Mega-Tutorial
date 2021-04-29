"""followers

Revision ID: 790cc3c78389
Revises: cd5a79039073
Create Date: 2021-04-29 16:05:36.460580

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '790cc3c78389'
down_revision = 'cd5a79039073'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###