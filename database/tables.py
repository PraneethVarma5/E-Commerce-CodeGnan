
# from database.connection import DatabaseConnction


# def createTables():
#     try:
#         db_config = DatabaseConnction()
#         cursor = db_config.cursor()

#         users_table_query = """create table if not exists users(
#             userid bigint auto_increment primary key,
#             username varchar(50) not null,
#             email varchar(50) not null unique,
#             hashpassword varchar(255) not null,
#             role enum('admin','user') default 'admin',
#             gender enum('male', 'female'),
#             phone varchar(15),
#             dateofbirth date,
#             profilename varchar(255), 
#             profilepath varchar(255), 
#             is_active boolean default true,
#             created_at timestamp default current_timestamp,
#             updated_at timestamp default current_timestamp on update current_timestamp
#         );"""

#         products_table_query = """create table if not exists products(
#             productid bigint auto_increment primary key,
#             productname varchar(100) not null,
#             description text,
#             category varchar(50),
#             quantity int unsigned default 0,
#             buyprice float(15,2) default 0.0,
#             saleprice float(15,2) default 0.0,
#             imgname varchar(100),
#             storedpath varchar(255),
#             is_active boolean default true,
#             created_at timestamp default current_timestamp,
#             updated_at timestamp default current_timestamp on update current_timestamp
#         );"""

#         orders_table_query = """create table if not exists orders(
#             orderid bigint auto_increment primary key,
#             userid bigint,
#             status enum('shipped', 'delivered', 'cancelled', 'pending') default 'pending',
#             address varchar(255),
#             created_at timestamp default current_timestamp,
#             foreign key (userid) references users(userid)
#         );"""

#         orderdetails_table_query = """create table if not exists order_details(
#             orderid bigint, 
#             productid bigint,
#             quantity int unsigned default 1,
#             price float(15,2) default 0.0,
#             subtotal float(20,2) generated always as (quantity * price),
#             foreign key(orderid) references orders(orderid),
#             foreign key(productid) references products(productid)
#         );"""

#         payments_table_query = """create table if not exists payments(
#             paymentid bigint auto_increment primary key,
#             userid bigint,
#             orderid bigint,
#             method enum('cash', 'upi', 'netbanking'),
#             amount float(20,2) default 0.0,
#             created_at timestamp default current_timestamp,
#             foreign key(userid) references users(userid),
#             foreign key(orderid) references orders(orderid)
#         );"""

#         cart_table_query = """create table if not exists cart(
#             cartid bigint auto_increment primary key,
#             userid bigint,
#             productid bigint,
#             quantity int default 1,
#             foreign key(userid) references users(userid),
#             foreign key(productid) references products(productid)
#         );"""

#         tables = [
#             users_table_query,
#             products_table_query,
#             orders_table_query,
#             orderdetails_table_query,
#             payments_table_query,
#             cart_table_query
#         ]

#         for table_query in tables:
#             cursor.execute(table_query)

#         return "Tables Created"

#     except Exception as e:
#         return f"Somthing wrong in database/tables.py:{e}"



from database.connection import DatabaseConnction


def createTables():
    db_config = None
    cursor = None

    try:
        db_config = DatabaseConnction()
        cursor = db_config.cursor()

        users_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            userid BIGINT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL,
            email VARCHAR(50) NOT NULL UNIQUE,
            hashpassword VARCHAR(255) NOT NULL,
            role ENUM('admin', 'user') DEFAULT 'admin',
            gender ENUM('male', 'female'),
            phone VARCHAR(15),
            dateofbirth DATE,
            profilename VARCHAR(255),
            profilepath VARCHAR(255),
            is_active BOOLEAN DEFAULT TRUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                ON UPDATE CURRENT_TIMESTAMP
        )
        """

        products_table_query = """
        CREATE TABLE IF NOT EXISTS products (
            productid BIGINT AUTO_INCREMENT PRIMARY KEY,
            productname VARCHAR(100) NOT NULL,
            description TEXT,
            category VARCHAR(50),
            quantity INT UNSIGNED DEFAULT 0,
            buyprice FLOAT(15,2) DEFAULT 0.0,
            saleprice FLOAT(15,2) DEFAULT 0.0,
            imgname VARCHAR(100),
            storedpath VARCHAR(255),
            is_active BOOLEAN DEFAULT TRUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                ON UPDATE CURRENT_TIMESTAMP
        )
        """

        orders_table_query = """
        CREATE TABLE IF NOT EXISTS orders (
            orderid BIGINT AUTO_INCREMENT PRIMARY KEY,
            userid BIGINT,
            status ENUM(
                'shipped', 'delivered', 'cancelled', 'pending'
            ) DEFAULT 'pending',
            address VARCHAR(255),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (userid) REFERENCES users(userid)
        )
        """

        orderdetails_table_query = """
        CREATE TABLE IF NOT EXISTS order_details (
            orderid BIGINT,
            productid BIGINT,
            quantity INT UNSIGNED DEFAULT 1,
            price FLOAT(15,2) DEFAULT 0.0,
            subtotal FLOAT(20,2)
                GENERATED ALWAYS AS (quantity * price),
            FOREIGN KEY (orderid) REFERENCES orders(orderid),
            FOREIGN KEY (productid) REFERENCES products(productid)
        )
        """

        payments_table_query = """
        CREATE TABLE IF NOT EXISTS payments (
            paymentid BIGINT AUTO_INCREMENT PRIMARY KEY,
            userid BIGINT,
            orderid BIGINT,
            method ENUM('cash', 'upi', 'netbanking'),
            amount FLOAT(20,2) DEFAULT 0.0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (userid) REFERENCES users(userid),
            FOREIGN KEY (orderid) REFERENCES orders(orderid)
        )
        """

        cart_table_query = """
        CREATE TABLE IF NOT EXISTS cart (
            cartid BIGINT AUTO_INCREMENT PRIMARY KEY,
            userid BIGINT,
            productid BIGINT,
            quantity INT DEFAULT 1,
            FOREIGN KEY (userid) REFERENCES users(userid),
            FOREIGN KEY (productid) REFERENCES products(productid)
        )
        """

        tables = [
            users_table_query,
            products_table_query,
            orders_table_query,
            orderdetails_table_query,
            payments_table_query,
            cart_table_query,
        ]

        for table_query in tables:
            cursor.execute(table_query)

        db_config.commit()
        return "Tables Created"

    except Exception as e:
        if db_config is not None:
            try:
                db_config.rollback()
            except Exception:
                pass

        return f"Error in database/tables.py: {e}"

    finally:
        if cursor is not None:
            cursor.close()

        if db_config is not None and db_config.is_connected():
            db_config.close()
