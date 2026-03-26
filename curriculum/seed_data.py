CURRICULUM = {
    "categories": [
        {
            "name": "Data Base",
            "slug": "data-base",
            "description": "Intro to databases and the alx_book_store MySQL project.",
            "order": 1,
            "topics": [
                {
                    "title": "Intro to MySQL and alx_book_store",
                    "slug": "intro-to-mysql-alx-book-store",
                    "description": "Hands-on MySQL project: designing and using the alx_book_store database.",
                    "order": 1,
                    "objectives": [
                        "What’s a database",
                        "What’s a relational database",
                        "What does SQL stand for",
                        "What’s MySQL",
                        "How to create a database in MySQL",
                        "What does DDL and DML stand for",
                        "How to CREATE or ALTER a table",
                        "How to SELECT data from a table",
                        "How to INSERT, UPDATE or DELETE data",
                        "What are subqueries",
                        "How to use MySQL functions",
                    ],
                    "tasks": [
                        {
                            "title": "0. A Magical Database for Your Dream Online Bookstore Adventure!",
                            "instructions": (
                                "Imagine you’re tasked with designing a MySQL database for an online bookstore. "
                                "The database should store information about books, authors, customers, orders, and order details.\n\n"
                                "Database Name: alx_book_store\n\n"
                                "Books: book_id (PK), title VARCHAR(130), author_id (FK to Authors), price DOUBLE, publication_date DATE\n"
                                "Authors: author_id (PK), author_name VARCHAR(215)\n"
                                "Customers: customer_id (PK), customer_name VARCHAR(215), email VARCHAR(215), address TEXT\n"
                                "Orders: order_id (PK), customer_id (FK to Customers), order_date DATE\n"
                                "Order_Details: orderdetailid (PK), order_id (FK to Orders), book_id (FK to Books), quantity DOUBLE\n\n"
                                "NOTE:\n"
                                "- The file extension should be alx_book_store.sql\n"
                                "- All SQL keywords should be in uppercase\n\n"
                                "Repo: Intro_to_DB\n"
                                "File: alx_book_store.sql\n"
                            ),
                            "order": 0,
                            "is_mandatory": True,
                            "checkers": [
                                "Checks for files exists and not empty",
                                "Checks for Implementation of Database alx_book_store",
                                "Check for creation and implementation of Authors",
                                "Check for creation and implementation of Books Table",
                                "Check for creation and implementation of Customers Table",
                                "Check for creation and implementation of Orders Table",
                                "Check for creation and implementation of Order_Details Table",
                            ],
                        },
                        {
                            "title": "1. Let's Build Your Database: Your Gateway to Data Adventure!",
                            "instructions": (
                                "Write a simple Python script that creates the database alx_book_store in your MySQL server.\n\n"
                                "Requirements:\n"
                                "- Name of python script should be MySQLServer.py\n"
                                "- If the database alx_book_store already exists, your script should not fail\n"
                                "- You are not allowed to use the SELECT or SHOW statements\n"
                                "- Print a message such as: Database 'alx_book_store' created successfully! when created\n"
                                "- Print an error message when failing to connect to the DB\n"
                                "- Handle opening and closing the DB in your script\n\n"
                                "Repo: Intro_to_DB\n"
                                "File: MySQLServer.py\n"
                            ),
                            "order": 1,
                            "is_mandatory": True,
                            "checkers": [
                                "Checks for files exists and not empty",
                                "Check if the script contains the import statement for mysql.connector",
                                "Check if the script contains the CREATE DATABASE statement for alx_book_store",
                                "Check if the script contains the code to establish a connection to the MySQL server",
                                "Check if the script contains the code to handle exceptions",
                                "Checks if the student did not use the SELECT or SHOW statements",
                            ],
                        },
                        {
                            "title": "2. Create Your Magical Tables",
                            "instructions": (
                                "Write a script that creates all the tables (books, authors, customers, orders, order_details) "
                                "in alx_book_store in your MySQL server.\n\n"
                                "Requirements:\n"
                                "- Name of the file should be task_2.sql\n"
                                "- All SQL keywords should be in uppercase\n\n"
                                "Repo: Intro_to_DB\n"
                                "File: task_2.sql\n"
                            ),
                            "order": 2,
                            "is_mandatory": True,
                            "checkers": [
                                "Check for creation and implementation of table Authors",
                                "Check for creation and implementation of Books Table",
                                "Check for creation and implementation of Customers Table",
                                "Check for creation and implementation of Orders Table",
                                "Check for creation and implementation of Order_Details Table",
                                "Check for the task_2.sql file and if its not empty",
                            ],
                        },
                        {
                            "title": "3. List all the tables created",
                            "instructions": (
                                "Write a script that lists all the tables in alx_book_store in your MySQL server.\n\n"
                                "Requirements:\n"
                                "- Name of the file should be task_3.sql\n"
                                "- The database name will be passed as argument of mysql command\n\n"
                                "Repo: Intro_to_DB\n"
                                "File: task_3.sql\n"
                            ),
                            "order": 3,
                            "is_mandatory": True,
                            "checkers": [
                                "Checks for listing all tables",
                                "Check if task_3.sql file is available",
                                "Checks if task_3.sql is not empty",
                                "Checks if the student used the correct database alx_book_store",
                            ],
                        },
                        {
                            "title": "4. Full description",
                            "instructions": (
                                "Write a script that prints the full description of the table books from the database alx_book_store.\n\n"
                                "Requirements:\n"
                                "- The database name will be passed as an argument of the mysql command\n"
                                "- You are not allowed to use the DESCRIBE or EXPLAIN statements\n"
                                "- The name of the file should be task_4.sql\n"
                                "- All SQL keywords should be in uppercase\n\n"
                                "Repo: Intro_to_DB\n"
                                "File: task_4.sql\n"
                            ),
                            "order": 4,
                            "is_mandatory": True,
                            "checkers": [
                                "Tests if the student didn’t use the DESCRIBE keyword",
                                "Checks for the description of the table books",
                                "Checks if the student didn’t use the ANALYZE keyword",
                                "Checks if the file task_4.sql exists",
                                "Checks if the task_4.sql is not empty",
                            ],
                        },
                        {
                            "title": "5. Populating Your Database with Your Very First Data",
                            "instructions": (
                                "Write a script that inserts a single row in the table customers (database alx_book_store).\n\n"
                                "Single data insertion:\n"
                                "- customer_id = 1\n"
                                "- customer_name = Cole Baidoo\n"
                                "- email = cbaidoo@sandtech.com\n"
                                "- address = 123 Happiness Ave.\n\n"
                                "Requirements:\n"
                                "- The database name will be passed as an argument of the mysql command\n"
                                "- Name of the file should be task_5.sql\n"
                                "- All SQL keywords should be in uppercase\n\n"
                                "Repo: Intro_to_DB\n"
                                "File: task_5.sql\n"
                            ),
                            "order": 5,
                            "is_mandatory": True,
                            "checkers": [
                                "Checks for the insertion of data in the customer table",
                                "Checks if task_5.sql is available",
                                "Checks if task_5.sql file is not empty",
                                "Checks for the insertion of the correct values in the customers table",
                            ],
                        },
                        {
                            "title": "6. Populating Your Database with More Data",
                            "instructions": (
                                "Write a script that inserts multiple rows in the table customers (database alx_book_store).\n\n"
                                "Data insertion:\n"
                                "- customer_id = 2, customer_name = Blessing Malik, email = bmalik@sandtech.com, address = 124 Happiness Ave.\n"
                                "- customer_id = 3, customer_name = Obed Ehoneah, email = eobed@sandtech.com, address = 125 Happiness Ave.\n"
                                "- customer_id = 4, customer_name = Nehemial Kamolu, email = nkamolu@sandtech.com, address = 126 Happiness Ave.\n\n"
                                "Requirements:\n"
                                "- The database name will be passed as an argument of the mysql command\n"
                                "- Name of the file should be task_6.sql\n\n"
                                "Repo: Intro_to_DB\n"
                                "File: task_6.sql\n"
                            ),
                            "order": 6,
                            "is_mandatory": True,
                            "checkers": [
                                "Checks for the insertion of the customer with customer_id=2",
                                "Checks for the insertion of the customer with customer_id=3",
                                "Checks for the insertion of the data with customer_id=4",
                                "Checks if task_6.sql file is available",
                                "Checks if task_6.sql file is not empty",
                            ],
                        },
                    ],
                },
            ],
        },
    ]
}