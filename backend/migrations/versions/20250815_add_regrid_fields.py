"""Add Regrid enrichment fields to land_parcels

Revision ID: add_regrid_fields_001
Revises: b31a3aa2a25b
Create Date: 2025-08-15 00:00:00
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'add_regrid_fields_001'
down_revision = 'b31a3aa2a25b'  # <- change if your last revision id differs
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('land_parcels', sa.Column('latitude', sa.Float(), nullable=True))
    op.add_column('land_parcels', sa.Column('longitude', sa.Float(), nullable=True))
    op.add_column('land_parcels', sa.Column('apn', sa.String(), nullable=True))
    op.add_column('land_parcels', sa.Column('parcel_id', sa.String(), nullable=True))
    op.add_column('land_parcels', sa.Column('acreage', sa.Float(), nullable=True))
    op.add_column('land_parcels', sa.Column('zoning_code', sa.String(), nullable=True))
    op.add_column('land_parcels', sa.Column('zoning_desc', sa.String(), nullable=True))
    op.add_column('land_parcels', sa.Column('owner_type', sa.String(), nullable=True))
    op.add_column('land_parcels', sa.Column('mailing_address', sa.String(), nullable=True))
    op.add_column('land_parcels', sa.Column('last_sale_date', sa.Date(), nullable=True))
    op.add_column('land_parcels', sa.Column('last_sale_price', sa.Numeric(14, 2), nullable=True))
    op.add_column('land_parcels', sa.Column('assessed_value', sa.Numeric(14, 2), nullable=True))
    op.add_column('land_parcels', sa.Column('geometry', postgresql.JSONB(astext_type=sa.Text()), nullable=True))

def downgrade():
    op.drop_column('land_parcels', 'geometry')
    op.drop_column('land_parcels', 'assessed_value')
    op.drop_column('land_parcels', 'last_sale_price')
    op.drop_column('land_parcels', 'last_sale_date')
    op.drop_column('land_parcels', 'mailing_address')
    op.drop_column('land_parcels', 'owner_type')
    op.drop_column('land_parcels', 'zoning_desc')
    op.drop_column('land_parcels', 'zoning_code')
    op.drop_column('land_parcels', 'acreage')
    op.drop_column('land_parcels', 'parcel_id')
    op.drop_column('land_parcels', 'apn')
    op.drop_column('land_parcels', 'longitude')
    op.drop_column('land_parcels', 'latitude')
