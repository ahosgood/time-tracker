"""add_event_comment

Revision ID: 55b4d6070aa0
Revises: 13384866a8a2
Create Date: 2020-12-03 08:44:09.199511

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "55b4d6070aa0"
down_revision = "13384866a8a2"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("event", sa.Column("comment", sa.String(length=64), nullable=True))
    op.drop_constraint("tag_user_id_name_key", "tag", type_="unique")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint("tag_user_id_name_key", "tag", ["user_id", "name"])
    op.drop_column("event", "comment")
    # ### end Alembic commands ###
