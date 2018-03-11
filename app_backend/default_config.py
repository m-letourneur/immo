import os
basedir = os.path.abspath(os.path.dirname(__file__))
# Path to root
immodir = '/'.join(basedir.split('/')[:-1])

# Migration files location
SQLALCHEMY_MIGRATE_REPO = os.path.join(immodir, 'database/migrations')
# Location of the sqlite database in the repository
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
    os.path.join(immodir, 'database/immodb.db')
# Remove a lot of overhead messages
SQLALCHEMY_TRACK_MODIFICATIONS = False
