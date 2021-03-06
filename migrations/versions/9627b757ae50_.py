"""empty message

Revision ID: 9627b757ae50
Revises: 
Create Date: 2019-12-01 15:05:37.689234

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9627b757ae50'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('address',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('line_1', sa.String(length=255), nullable=True),
    sa.Column('line_2', sa.String(length=255), nullable=True),
    sa.Column('line_3', sa.String(length=255), nullable=True),
    sa.Column('line_4', sa.String(length=255), nullable=True),
    sa.Column('city', sa.String(length=255), nullable=True),
    sa.Column('state_code', sa.String(length=2), nullable=True),
    sa.Column('postal_code', sa.String(length=20), nullable=True),
    sa.Column('county', sa.String(length=255), nullable=True),
    sa.Column('country', sa.String(length=255), nullable=True),
    sa.Column('latitude', sa.Numeric(precision=9, scale=6), nullable=True),
    sa.Column('longitude', sa.Numeric(precision=9, scale=6), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('tenant',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('subdomain', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('subdomain')
    )
    op.create_table('deal',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('address_id', sa.Integer(), nullable=True),
    sa.Column('property_tax', sa.Integer(), nullable=True),
    sa.Column('sq_feet', sa.Integer(), nullable=True),
    sa.Column('bedrooms', sa.Integer(), nullable=True),
    sa.Column('bedrooms_str', sa.String(length=255), nullable=True),
    sa.Column('bathrooms', sa.Integer(), nullable=True),
    sa.Column('bathrooms_str', sa.String(length=255), nullable=True),
    sa.Column('after_repair_value', sa.Integer(), nullable=True),
    sa.Column('rehab_estimate', sa.Integer(), nullable=True),
    sa.Column('purchase_price', sa.Integer(), nullable=True),
    sa.Column('list_price', sa.Integer(), nullable=True),
    sa.Column('under_contract_ind', sa.Boolean(), nullable=True),
    sa.Column('tenant_id', sa.Integer(), nullable=True),
    sa.Column('updated_by_id', sa.Integer(), nullable=True),
    sa.Column('created_by_id', sa.Integer(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['address_id'], ['address.id'], ),
    sa.ForeignKeyConstraint(['created_by_id'], ['user.id'], name='fk_Deal_created_by_id', use_alter=True),
    sa.ForeignKeyConstraint(['tenant_id'], ['tenant.id'], ),
    sa.ForeignKeyConstraint(['updated_by_id'], ['user.id'], name='fk_Deal_updated_by_id', use_alter=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('settings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tenant_id', sa.Integer(), nullable=True),
    sa.Column('partnership_email_recipient', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['tenant_id'], ['tenant.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('confirmed_at', sa.DateTime(), nullable=True),
    sa.Column('api_key', sa.String(length=255), nullable=True),
    sa.Column('last_login_at', sa.DateTime(), nullable=True),
    sa.Column('current_login_at', sa.DateTime(), nullable=True),
    sa.Column('last_login_ip', sa.String(length=40), nullable=True),
    sa.Column('current_login_ip', sa.String(length=40), nullable=True),
    sa.Column('login_count', sa.Integer(), nullable=True),
    sa.Column('tenant_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['tenant_id'], ['tenant.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_api_key'), 'user', ['api_key'], unique=True)
    op.create_table('contact',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('first_name', sa.String(length=255), nullable=True),
    sa.Column('last_name', sa.String(length=255), nullable=True),
    sa.Column('phone', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('file',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('description', sa.String(length=1500), nullable=True),
    sa.Column('url', sa.String(length=500), nullable=True),
    sa.Column('deal_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['deal_id'], ['deal.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('investor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tenant_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['tenant_id'], ['tenant.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('proforma',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('proforma_type', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('description', sa.String(length=5000), nullable=True),
    sa.Column('deal_id', sa.Integer(), nullable=True),
    sa.Column('arv', sa.Integer(), nullable=True),
    sa.Column('purchase_price', sa.Integer(), nullable=True),
    sa.Column('seller_concessions', sa.Integer(), nullable=True),
    sa.Column('closing_costs', sa.Integer(), nullable=True),
    sa.Column('rehab_costs', sa.Integer(), nullable=True),
    sa.Column('initial_reserve_amount', sa.Integer(), nullable=True),
    sa.Column('lease_option_fee', sa.Integer(), nullable=True),
    sa.Column('total_finished_sq_foot', sa.Integer(), nullable=True),
    sa.Column('land_value_perc', sa.Numeric(precision=5, scale=2), nullable=True),
    sa.Column('income_tax_rate', sa.Numeric(precision=5, scale=2), nullable=True),
    sa.Column('property_appreciation_rate', sa.Numeric(precision=5, scale=2), nullable=True),
    sa.Column('vacancy_perc', sa.Numeric(precision=5, scale=2), nullable=True),
    sa.Column('sales_commission_rate', sa.Numeric(precision=5, scale=2), nullable=True),
    sa.Column('updated_by_id', sa.Integer(), nullable=True),
    sa.Column('created_by_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['created_by_id'], ['user.id'], name='fk_Proforma_created_by_id', use_alter=True),
    sa.ForeignKeyConstraint(['deal_id'], ['deal.id'], ),
    sa.ForeignKeyConstraint(['updated_by_id'], ['user.id'], name='fk_Proforma_updated_by_id', use_alter=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('roles_users',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.create_table('capital_expenditure',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('proforma_id', sa.Integer(), nullable=True),
    sa.Column('type', sa.String(length=255), nullable=True),
    sa.Column('replacement_cost', sa.Numeric(precision=12, scale=2), nullable=True),
    sa.Column('lifespan', sa.Integer(), nullable=True),
    sa.Column('updated_by_id', sa.Integer(), nullable=True),
    sa.Column('created_by_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['created_by_id'], ['user.id'], name='fk_CapitalExpenditure_created_by_id', use_alter=True),
    sa.ForeignKeyConstraint(['proforma_id'], ['proforma.id'], ),
    sa.ForeignKeyConstraint(['updated_by_id'], ['user.id'], name='fk_CapitalExpenditure_updated_by_id', use_alter=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('deal_contact',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('deal_id', sa.Integer(), nullable=True),
    sa.Column('contact_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['contact_id'], ['contact.id'], ),
    sa.ForeignKeyConstraint(['deal_id'], ['deal.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('investmentcriteria',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('investor_id', sa.Integer(), nullable=True),
    sa.Column('property_type', sa.Integer(), nullable=True),
    sa.Column('flip', sa.Integer(), nullable=True),
    sa.Column('rental', sa.Integer(), nullable=True),
    sa.Column('minimum_units', sa.Integer(), nullable=True),
    sa.Column('maximum_units', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['investor_id'], ['investor.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('line_item',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('income_proforma_id', sa.Integer(), nullable=True),
    sa.Column('expense_proforma_id', sa.Integer(), nullable=True),
    sa.Column('type', sa.String(length=255), nullable=True),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.Column('amount_type', sa.String(length=50), nullable=True),
    sa.Column('frequency', sa.Integer(), nullable=True),
    sa.Column('annual_increase_perc', sa.Numeric(precision=6, scale=2), nullable=True),
    sa.Column('updated_by_id', sa.Integer(), nullable=True),
    sa.Column('created_by_id', sa.Integer(), nullable=True),
    sa.Column('calculation', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['created_by_id'], ['user.id'], name='fk_LineItem_created_by_id', use_alter=True),
    sa.ForeignKeyConstraint(['expense_proforma_id'], ['proforma.id'], ),
    sa.ForeignKeyConstraint(['income_proforma_id'], ['proforma.id'], ),
    sa.ForeignKeyConstraint(['updated_by_id'], ['user.id'], name='fk_LineItem_updated_by_id', use_alter=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('loan',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('proforma_id', sa.Integer(), nullable=True),
    sa.Column('type', sa.Integer(), nullable=True),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.Column('interest_rate', sa.Numeric(precision=6, scale=3), nullable=True),
    sa.Column('interest_only', sa.Boolean(), nullable=True),
    sa.Column('length', sa.Integer(), nullable=True),
    sa.Column('updated_by_id', sa.Integer(), nullable=True),
    sa.Column('created_by_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['created_by_id'], ['user.id'], name='fk_Loan_created_by_id', use_alter=True),
    sa.ForeignKeyConstraint(['proforma_id'], ['proforma.id'], ),
    sa.ForeignKeyConstraint(['updated_by_id'], ['user.id'], name='fk_Loan_updated_by_id', use_alter=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('deal_contact_role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('deal_contact_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['deal_contact_id'], ['deal_contact.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('locationcriteria',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('location_type', sa.String(length=255), nullable=True),
    sa.Column('location_code', sa.String(length=2), nullable=True),
    sa.Column('criteria_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['criteria_id'], ['investmentcriteria.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('locationcriteria')
    op.drop_table('deal_contact_role')
    op.drop_table('loan')
    op.drop_table('line_item')
    op.drop_table('investmentcriteria')
    op.drop_table('deal_contact')
    op.drop_table('capital_expenditure')
    op.drop_table('roles_users')
    op.drop_table('proforma')
    op.drop_table('investor')
    op.drop_table('file')
    op.drop_table('contact')
    op.drop_index(op.f('ix_user_api_key'), table_name='user')
    op.drop_table('user')
    op.drop_table('settings')
    op.drop_table('deal')
    op.drop_table('tenant')
    op.drop_table('role')
    op.drop_table('address')
    # ### end Alembic commands ###
