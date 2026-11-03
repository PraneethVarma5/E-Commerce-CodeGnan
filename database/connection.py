
import mysql.connector as SQLC


def DatabaseConnction():
    try:
        db_config = SQLC.connect(
            host="localhost",
            user="root",
            password="Praneeth@005",
            database="ecommerce"
        )

        return db_config

    except SQLC.Error as e:
        raise RuntimeError(
            f"MySQL connection failed: {e}"
        ) from e
