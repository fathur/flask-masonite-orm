from masoniteorm.connections import ConnectionResolver
import os

DATABASES = {
    "default": "postgres",

    "postgres": {
        "host": os.environ.get('DB_HOST'),  # "127.0.0.1",
        "driver": "postgres",
        "database": os.environ.get('DB_NAME'),  # "underwriting",
        "user": os.environ.get('DB_USER'),  # "ops_server",
        "password": os.environ.get('DB_PASSWORD'),  # "password",
        "port": os.environ.get('DB_PORT'),  # 5432,
        "log_queries": os.environ.get('DEBUG'),  # False,
        "options": {
            #
        }
    },

}

DB = ConnectionResolver().set_connection_details(DATABASES)
