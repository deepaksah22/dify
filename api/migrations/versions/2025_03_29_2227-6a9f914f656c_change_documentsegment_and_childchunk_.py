"""change documentsegment and childchunk indexes

Revision ID: 6a9f914f656c
Revises: d20049ed0af6
Create Date: 2025-03-29 22:27:24.789481

"""
from alembic import op
import models as models
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a9f914f656c'
down_revision = 'd20049ed0af6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('child_chunks', schema=None) as batch_op:
        batch_op.create_index('child_chunks_node_idx', ['index_node_id', 'dataset_id'], unique=False)
        batch_op.create_index('child_chunks_segment_idx', ['segment_id'], unique=False)

    with op.batch_alter_table('document_segments', schema=None) as batch_op:
        batch_op.drop_index('document_segment_dataset_node_idx')
        batch_op.create_index('document_segment_node_dataset_idx', ['index_node_id', 'dataset_id'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('document_segments', schema=None) as batch_op:
        batch_op.drop_index('document_segment_node_dataset_idx')
        batch_op.create_index('document_segment_dataset_node_idx', ['dataset_id', 'index_node_id'], unique=False)

    with op.batch_alter_table('child_chunks', schema=None) as batch_op:
        batch_op.drop_index('child_chunks_segment_idx')
        batch_op.drop_index('child_chunks_node_idx')

    # ### end Alembic commands ###
