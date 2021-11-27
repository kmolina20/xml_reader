import psycopg2

try:
    # credenciales = {
    #     "dbname": "dbkhv318cia3np",
    #     "user": "yyzbngfyawltmd",
    #     "password": "8faebbaa4e52a0e73132b864d021f37afc876775c1d8e6f94d1852eb7af7ae27",
    #     "host": "ec2-52-21-153-207.compute-1.amazonaws.com",
    #     "port": 5432
    # }
    credenciales = {
        "dbname": "db_metadata",
        "user": "postgres",
        "password": "root",
        "host": "localhost",
        "port": 5432
    }
    conexion = psycopg2.connect(**credenciales)
except psycopg2.Error as e:
    print("Ocurrió un error al conectar a PostgreSQL: ", e)