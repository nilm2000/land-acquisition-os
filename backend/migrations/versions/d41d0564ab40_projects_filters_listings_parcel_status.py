"""projects/filters/listings + parcel status

Revision ID: 7c9a_proj_filter
Revises: b31a3aa2a25b
Create Date: 2025-08-15
"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '7c9a_proj_filter'
down_revision: Union[str, None] = 'b31a3aa2a25b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # --- projects ---
    op.create_table(
        'projects',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(length=200), nullable=False, unique=True),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    )

    # --- filters ---
    op.create_table(
        'filters',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('project_id', sa.Integer(), sa.ForeignKey('projects.id', ondelete='CASCADE'), index=True, nullable=False),
        sa.Column('name', sa.String(length=200), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False, server_default=sa.text('true')),
        sa.Column('polygon_geojson', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column('rules', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    )

    # --- land_parcels additions ---
    status_enum = sa.Enum('unqualified', 'qualified', 'disqualified', 'snoozed', name='parcelstatus')
    status_enum.create(op.get_bind(), checkfirst=True)

    op.add_column('land_parcels', sa.Column('latitude', sa.Float(), nullable=True))
    op.add_column('land_parcels', sa.Column('longitude', sa.Float(), nullable=True))
    op.add_column('land_parcels', sa.Column('status', status_enum, nullable=False, server_default='unqualified'))
    op.add_column('land_parcels', sa.Column('disqualify_reason', sa.Text(), nullable=True))
    op.add_column('land_parcels', sa.Column('snooze_until', sa.Date(), nullable=True))

    op.add_column('land_parcels', sa.Column('county_fips', sa.String(length=10), nullable=True))
    op.add_column('land_parcels', sa.Column('apn', sa.String(length=100), nullable=True))
    op.add_column('land_parcels', sa.Column('zoning_code', sa.String(length=100), nullable=True))
    op.add_column('land_parcels', sa.Column('acreage_gis', sa.Float(), nullable=True))
    op.add_column('land_parcels', sa.Column('last_sale_date', sa.Date(), nullable=True))
    op.add_column('land_parcels', sa.Column('last_sale_price', sa.Float(), nullable=True))
    op.add_column('land_parcels', sa.Column('price_current', sa.Float(), nullable=True))
    op.add_column('land_parcels', sa.Column('days_on_market', sa.Integer(), nullable=True))

    op.create_index('ix_land_parcels_county_fips', 'land_parcels', ['county_fips'])
    op.create_index('ix_land_parcels_apn', 'land_parcels', ['apn'])

    # --- listings ---
    op.create_table(
        'listings',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('parcel_id', sa.Integer(), sa.ForeignKey('land_parcels.id', ondelete='CASCADE'), nullable=False, index=True),
        sa.Column('source', sa.String(length=50), nullable=False),
        sa.Column('url', sa.Text(), nullable=False),
        sa.Column('price', sa.Float(), nullable=True),
        sa.Column('first_seen', sa.Date(), nullable=True),
        sa.Column('last_seen', sa.Date(), nullable=True),
        sa.Column('remarks', sa.Text(), nullable=True),
    )


def downgrade() -> None:
    op.drop_table('listings')
    op.drop_index('ix_land_parcels_apn', table_name='land_parcels')
    op.drop_index('ix_land_parcels_county_fips', table_name='land_parcels')

    op.drop_column('land_parcels', 'days_on_market')
    op.drop_column('land_parcels', 'price_current')
    op.drop_column('land_parcels', 'last_sale_price')
    op.drop_column('land_parcels', 'last_sale_date')
    op.drop_column('land_parcels', 'acreage_gis')
    op.drop_column('land_parcels', 'zoning_code')
    op.drop_column('land_parcels', 'apn')
    op.drop_column('land_parcels', 'county_fips')
    op.drop_column('land_parcels', 'snooze_until')
    op.drop_column('land_parcels', 'disqualify_reason')
    op.drop_column('land_parcels', 'status')
    op.drop_column('land_parcels', 'longitude')
    op.drop_column('land_parcels', 'latitude')

    op.drop_table('filters')
    op.drop_table('projects')

    status_enum = sa.Enum(name='parcelstatus')
    status_enum.drop(op.get_bind(), checkfirst=True)
