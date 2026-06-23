"""create products table

Revision ID: 0002
Revises: 0001
Create Date: 2026-06-23

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

revision = "0002"
down_revision = "0001"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "products",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("name", sa.String(128), nullable=False),
        sa.Column("slug", sa.String(128), nullable=False),
        sa.Column("status", sa.String(32), nullable=False, server_default="active"),
        sa.Column("description", sa.Text(), nullable=True),
    )
    op.create_index("ix_products_slug", "products", ["slug"], unique=True)


def downgrade() -> None:
    op.drop_index("ix_products_slug", table_name="products")
    op.drop_table("products")
