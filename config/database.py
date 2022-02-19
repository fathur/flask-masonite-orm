from masoniteorm.connections import ConnectionResolver

DATABASES = {
  "default": "postgres",

  "postgres": {
    "host": "127.0.0.1",
    "driver": "postgres",
    "database": "underwriting",
    "user": "postgres",
    "password": "password",
    "port": 5432,
    "log_queries": False,
    "options": {
      #
    }
  },

}

DB = ConnectionResolver().set_connection_details(DATABASES)
