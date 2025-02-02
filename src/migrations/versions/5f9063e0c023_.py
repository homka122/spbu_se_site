"""empty message

Revision ID: 5f9063e0c023
Revises: 925985497ccc
Create Date: 2022-05-20 01:04:21.444079

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f9063e0c023'
down_revision = '925985497ccc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('promo_code',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=512), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_promo_code'))
    )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('summer_school', schema=None) as batch_op:
        batch_op.alter_column('requirements',
               existing_type=sa.VARCHAR(length=1024),
               nullable=True)
        batch_op.alter_column('advisors',
               existing_type=sa.VARCHAR(length=1024),
               nullable=True)
        batch_op.alter_column('tech',
               existing_type=sa.VARCHAR(length=1024),
               nullable=True)
        batch_op.alter_column('description',
               existing_type=sa.VARCHAR(length=2048),
               nullable=True)
        batch_op.alter_column('project_name',
               existing_type=sa.VARCHAR(length=1024),
               nullable=True)

    with op.batch_alter_table('staff', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_staff_official_email'), type_='unique')

    with op.batch_alter_table('post_vote', schema=None) as batch_op:
        batch_op.alter_column('post_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    op.drop_table('promo_code')
    # ### end Alembic commands ###
