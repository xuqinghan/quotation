import os

INSTANCE_FOLDER_PATH = os.path.join('/tmp', 'instance')
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + INSTANCE_FOLDER_PATH\
                          + '/db.sqlite'
