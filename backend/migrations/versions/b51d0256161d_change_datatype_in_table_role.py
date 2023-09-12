"""change datatype in table Role

Revision ID: b51d0256161d
Revises: b7e2b4ce8006
Create Date: 2023-09-12 18:54:06.505850

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'b51d0256161d'
down_revision: Union[str, None] = 'b7e2b4ce8006'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Roles', sa.Column('role_name', sa.String(), nullable=False))
    op.drop_column('Roles', 'permission')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Roles', sa.Column('permission', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True))
    op.drop_column('Roles', 'role_name')
    # ### end Alembic commands ###