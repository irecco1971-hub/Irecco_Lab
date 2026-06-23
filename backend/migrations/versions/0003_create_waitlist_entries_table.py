"""create waitlist_entries table

Revision ID: 0003
Revises: 0002
Create Date: 2026-06-23

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

revision = "0003"
down_revision = "0002"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "waitlist_entries",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column(
            "product_id",
            UUID(as_uuid=True),
            sa.ForeignKey("products.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("email", sa.String(255), nullable=False),
        sa.Column("status", sa.String(32), nullable=False, server_default="pending"),
    )
    op.create_index("ix_waitlist_product_email", "waitlist_entries", ["product_id", "email"], unique=True)


def downgrade() -> None:
    op.drop_index("ix_waitlist_product_email", table_name="waitlist_entries")
    op.drop_table("waitlist_entries")
