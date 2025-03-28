"""change title in News model

Revision ID: a0759e297410
Revises: b45897b9aacd
Create Date: 2025-03-17 16:39:56.046526

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "a0759e297410"
down_revision: Union[str, None] = "b45897b9aacd"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("news", sa.Column("published_at", sa.DateTime(), nullable=False))
    op.drop_column("news", "created_at")
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "news",
        sa.Column(
            "created_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=False
        ),
    )
    op.drop_column("news", "published_at")
    # ### end Alembic commands ###
