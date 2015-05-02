from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
tasks = Table('tasks', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('input', VARCHAR(length=1024)),
    Column('output', VARCHAR(length=1024)),
    Column('time_started', DATETIME),
    Column('user_id', INTEGER),
)

task = Table('task', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('input', String(length=1024)),
    Column('output', String(length=1024)),
    Column('time_started', DateTime),
    Column('user_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['tasks'].drop()
    post_meta.tables['task'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['tasks'].create()
    post_meta.tables['task'].drop()
