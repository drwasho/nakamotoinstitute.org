"""empty message

Revision ID: 341e59e9c366
Revises: None
Create Date: 2014-03-08 15:49:00.471409

"""

# revision identifiers, used by Alembic.
revision = '341e59e9c366'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('text', sa.String(), nullable=True),
    sa.Column('source', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('doctype',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('author',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('doc',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('date', sa.String(), nullable=True),
    sa.Column('slug', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('email',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject', sa.String(), nullable=True),
    sa.Column('sent_from', sa.String(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('text', sa.String(), nullable=True),
    sa.Column('source', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('format',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('formats',
    sa.Column('doc_id', sa.Integer(), nullable=True),
    sa.Column('format_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['doc_id'], ['doc.id'], ),
    sa.ForeignKeyConstraint(['format_id'], ['format.id'], )
    )
    op.create_table('authors',
    sa.Column('doc_id', sa.Integer(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['author.id'], ),
    sa.ForeignKeyConstraint(['doc_id'], ['doc.id'], )
    )
    op.create_table('categories',
    sa.Column('doc_id', sa.Integer(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['doc_id'], ['doc.id'], )
    )
    op.create_table('doctypes',
    sa.Column('doc_id', sa.Integer(), nullable=True),
    sa.Column('format_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['doc_id'], ['doc.id'], ),
    sa.ForeignKeyConstraint(['format_id'], ['doctype.id'], )
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('doctypes')
    op.drop_table('categories')
    op.drop_table('authors')
    op.drop_table('formats')
    op.drop_table('format')
    op.drop_table('email')
    op.drop_table('doc')
    op.drop_table('category')
    op.drop_table('author')
    op.drop_table('doctype')
    op.drop_table('post')
    ### end Alembic commands ###
