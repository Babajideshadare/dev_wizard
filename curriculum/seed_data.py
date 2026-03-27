CURRICULUM = {
    "categories": [

        {
            "name": "Python",
            "slug": "python",
            "description": "Intro to Python basics, arithmetic operations, and simple scripts.",
            "order": 1,  # Python can appear before Database; adjust if you like
            "topics": [
                {
                    "title": "Python",
                    "slug": "python-basics",
                    "description": "Getting started with Python syntax, arithmetic operations, and user input.",
                    "order": 1,
                    "objectives": [
                        "Define what Python is and understand its key characteristics as a high-level programming language.",
                        "Identify various application areas where Python is commonly used.",
                        "Install Python on your system and set up a development environment to start writing Python code.",
                        "Explain the importance of indentation in Python code and how it contributes to code readability.",
                        "Write basic Python code following proper syntax guidelines.",
                    ],
                    "tasks": [
                        {
                            "title": "0. Basic Arithmetic Exercise",
                            "instructions": (
                                "You are required to complete a Python script that performs basic arithmetic operations "
                                "with two predefined numbers.\n\n"
                                "Instructions:\n"
                                "- Create a file named basic_operations.py.\n"
                                "- Define two variables: number1 = 10 and number2 = 5.\n"
                                "- Perform addition, subtraction (number1 - number2), and multiplication.\n"
                                "- Print the results in the format: [operation] of [number1] and [number2] is [result].\n\n"
                                "Example execution:\n"
                                "Addition of 10 and 5 is 15\n"
                                "Subtraction of 10 and 5 is 5\n"
                                "Multiplication of 10 and 5 is 50\n\n"
                                "How to run:\n"
                                "python3 basic_operations.py\n"
                            ),
                            "order": 0,
                            "is_mandatory": True,
                            "checkers": [
                                "File basic_operations.py is present",
                                "Correct variable assignments for number1 and number2",
                                "No global variables used",
                                "Uses explicit print statements for each operation",
                                "Correctly uses arithmetic operators",
                                "Script executes without errors",
                            ],
                        },
                        {
                            "title": "1. Simple Interest Calculator",
                            "instructions": (
                                "Complete a Python script that calculates simple interest using the formula I = P * R * T.\n\n"
                                "Instructions:\n"
                                "- Create a file named simple_interest.py.\n"
                                "- Define variables: principal = 1000, rate = 0.05, time = 3.\n"
                                "- Calculate interest = principal * rate * time.\n"
                                "- Print: The simple interest is: [interest].\n\n"
                                "Expected output for these values:\n"
                                "The simple interest is: 150.0\n"
                            ),
                            "order": 1,
                            "is_mandatory": True,
                            "checkers": [
                                "Check if the required file simple_interest.py exists",
                                "Correct variable assignments for principal, rate, and time",
                                "Check for correct calculation of simple interest",
                                "Ensure no use of forbidden syntax or constructs",
                                "Check for use of correct arithmetic operators",
                                "Ensure script executes without errors",
                            ],
                        },
                        {
                            "title": "2. Calculate the Area of a Rectangle",
                            "instructions": (
                                "Write a Python script that calculates the area of a rectangle.\n\n"
                                "Instructions:\n"
                                "- Create a file named rectangle_area.py.\n"
                                "- Define variables: length = 10, width = 5.\n"
                                "- Calculate area = length * width and store in a variable named area.\n"
                                "- Print: The area of the rectangle is: [area].\n\n"
                                "Expected output:\n"
                                "The area of the rectangle is: 50\n"
                            ),
                            "order": 2,
                            "is_mandatory": True,
                            "checkers": [
                                "Check if the required file rectangle_area.py exists",
                                "Check correct variable assignments for length and width",
                                "Check for correct area calculation",
                                "Ensure no use of forbidden syntax or constructs",
                                "Check for use of correct arithmetic operators",
                                "Ensure script executes without errors",
                            ],
                        },
                        {
                            "title": "3. Convert Hours to Seconds",
                            "instructions": (
                                "Write a Python script that converts a number of hours into seconds.\n\n"
                                "Instructions:\n"
                                "- Create a file named hours_to_seconds.py.\n"
                                "- Define a variable hours = 2.\n"
                                "- Calculate seconds = hours * 3600.\n"
                                "- Print: [hours] hour(s) is [seconds] seconds.\n\n"
                                "Expected output:\n"
                                "2 hour(s) is 7200 seconds.\n"
                            ),
                            "order": 3,
                            "is_mandatory": True,
                            "checkers": [
                                "Check if the required file hours_to_seconds.py exists",
                                "Check correct variable assignment for hours",
                                "Check for correct calculation of seconds",
                                "Ensure no use of forbidden syntax or constructs",
                                "Check for use of correct arithmetic operators",
                                "Ensure script executes without errors",
                            ],
                        },
                        {
                            "title": "4. User Input Age Calculator",
                            "instructions": (
                                "Create a script that asks the user for their current age and calculates how old they "
                                "will be in the year 2050.\n\n"
                                "Instructions:\n"
                                "- Create a file named future_age_calculator.py.\n"
                                "- Prompt the user: 'How old are you? '.\n"
                                "- Assume the user inputs a valid integer.\n"
                                "- Assume current year is 2023; add 27 years to get age in 2050.\n"
                                "- Print: In 2050, you will be [age] years old.\n\n"
                                "Example: if user inputs 30, print: In 2050, you will be 57 years old.\n"
                            ),
                            "order": 4,
                            "is_mandatory": True,
                            "checkers": [
                                "Check if the required file future_age_calculator.py exists",
                                "Check for correct user input prompt",
                                "Ensure script executes without errors",
                            ],
                        },
                        {
                            "title": "5. Personal Finance Calculator (Advanced)",
                            "instructions": (
                                "Create a script named finance_calculator.py that calculates monthly savings and projects "
                                "savings after one year with interest.\n\n"
                                "Instructions:\n"
                                "- Prompt: 'Enter your monthly income: '.\n"
                                "- Prompt: 'Enter your total monthly expenses: '.\n"
                                "- Calculate monthly_savings = income - expenses.\n"
                                "- Assume annual interest rate = 5% (0.05).\n"
                                "- Calculate projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05).\n"
                                "- Print monthly savings and projected savings.\n\n"
                                "Example:\n"
                                "Enter your monthly income: 5000\n"
                                "Enter your total monthly expenses: 4000\n"
                                "Your monthly savings are $1000.\n"
                                "Projected savings after one year, with interest, is: $12600.\n"
                            ),
                            "order": 5,
                            "is_mandatory": False,  # advanced/optional
                            "checkers": [
                                "Check if the required file finance_calculator.py exists",
                                "Check for correct user input prompts",
                                "Check for correct calculations of monthly and annual savings",
                            ],
                        },
                    ],
                },

                {
                    "title": "Control flow and loops",
                    "slug": "control-flow-and-loops",
                    "description": "Learn how to use conditionals, match/case, and loops to control the flow of a Python program.",
                    "order": 2,
                    "objectives": [
                        "Explain the concept of control flow and its role in programming.",
                        "Utilize conditional statements (if, else, elif) to control the flow of execution in your Python code based on specific conditions.",
                        "Write practical examples demonstrating the use of conditional statements for decision-making.",
                        "Understand the concept of Match Case statements introduced in Python 3.10 as an alternative to multiple if/elif statements (optional for Python versions below 3.10).",
                        "Explain the advantages of Match Case statements for handling multiple conditions.",
                        "Implement Match Case statements using proper syntax, including matching against specific values and types (optional for Python versions below 3.10).",
                        "Apply best practices for using Match Case statements to enhance code readability and efficiency (optional for Python versions below 3.10).",
                        "Grasp the purpose and different types of loops available in Python.",
                        "Utilize for loops to iterate over sequences (lists, tuples, strings, etc.) efficiently.",
                        "Write examples demonstrating how to use for loops to iterate over various data structures.",
                        "Explain the concept of while loops and how they differ from for loops.",
                        "Implement while loops in Python to execute code repeatedly as long as a specific condition remains true.",
                        "Understand nested loops (loops within loops) and their applications in scenarios like working with multidimensional data or creating patterns.",
                    ],
                    "tasks": [
                        {
                            "title": "0. Weather Recommendation Program",
                            "instructions": (
                                "Create a Python script named weather_advice.py that asks the user about the current weather "
                                "and provides clothing recommendations using if/elif/else statements.\n\n"
                                "Instructions:\n"
                                "- Prompt the user: What's the weather like today? (sunny/rainy/cold):\n"
                                "- If 'sunny': print 'Wear a t-shirt and sunglasses.'\n"
                                "- If 'rainy': print 'Don't forget your umbrella and a raincoat.'\n"
                                "- If 'cold': print 'Make sure to wear a warm coat and a scarf.'\n"
                                "- Else: print 'Sorry, I don't have recommendations for this weather.'\n"
                            ),
                            "order": 0,
                            "is_mandatory": True,
                            "checkers": [
                                "Checks for file exists and not empty",
                                "Checks for prompting user for weather input",
                                "Check for the if statement for 'sunny' condition",
                                "Check for the elif statement for 'rainy' condition",
                                "Check for the elif statement for 'cold' condition",
                                "Check for the else statement for unexpected input",
                            ],
                        },
                        {
                            "title": "1. Simple Calculator with Match Case",
                            "instructions": (
                                "Develop a Python script named match_case_calculator.py. The script prompts the user for two numbers "
                                "and an operation (+, -, *, /), then uses a match case statement to perform the operation.\n\n"
                                "Instructions:\n"
                                "- Prompt: Enter the first number: (store in num1).\n"
                                "- Prompt: Enter the second number: (store in num2).\n"
                                "- Prompt: Choose the operation (+, -, *, /):\n"
                                "- Use match/case on the operation to perform addition, subtraction, multiplication, or division.\n"
                                "- Handle division by zero: if num2 == 0 and operation is '/', print 'Cannot divide by zero.'\n"
                                "- Otherwise, print 'The result is [result]'.\n"
                            ),
                            "order": 1,
                            "is_mandatory": True,
                            "checkers": [
                                "Checks for the file match_case_calculator.py exists and not empty",
                                "Check for the input prompt for the first number",
                                "Check for the input prompt for the second number",
                                "Check for the input prompt for the operation",
                                "Check for the match case statement for operations",
                                "Check for the output result message",
                            ],
                        },
                        {
                            "title": "2. Multiplication Table Generator",
                            "instructions": (
                                "Create a Python script named multiplication_table.py that prints the multiplication table "
                                "for a user-provided number from 1 to 10.\n\n"
                                "Instructions:\n"
                                "- Prompt: Enter a number to see its multiplication table: (store in number).\n"
                                "- Use a for loop to iterate from 1 to 10.\n"
                                "- For each i, print: number * i = result.\n\n"
                                "Example: for input 5, prints 5 * 1 = 5 ... 5 * 10 = 50.\n"
                            ),
                            "order": 2,
                            "is_mandatory": True,
                            "checkers": [
                                "Checks for file multiplication_table.py exists and not empty",
                                "Check for the input prompt for the number",
                                "Check for the for loop iterating from 1 to 10",
                                "Check for the print statement for the multiplication table",
                            ],
                        },
                        {
                            "title": "3. Drawing Patterns with Nested Loops",
                            "instructions": (
                                "Develop a Python script named pattern_drawing.py that draws a square pattern of asterisks (*) "
                                "using nested loops.\n\n"
                                "Instructions:\n"
                                "- Prompt: Enter the size of the pattern: (positive integer).\n"
                                "- Use a while loop to iterate over rows.\n"
                                "- Inside the while loop, use a for loop to print '*' side by side (use print('*', end='') ).\n"
                                "- After each row, print a newline.\n"
                                "- Continue until you form a square of the given size.\n"
                            ),
                            "order": 3,
                            "is_mandatory": True,
                            "checkers": [
                                "Checks for file pattern_drawing.py exists and not empty",
                                "Checks for user input for pattern size",
                                "Checks for existence of while loop",
                                "Checks for pattern drawing with nested loops",
                            ],
                        },
                        {
                            "title": "4. Personal Daily Reminder",
                            "instructions": (
                                "Develop a script named daily_reminder.py. The script asks for a single task, its priority, "
                                "and whether it is time-bound, then prints a customized reminder.\n\n"
                                "Instructions:\n"
                                "- Prompt: Enter your task: (store in task variable).\n"
                                "- Prompt: Priority (high/medium/low): (store in priority variable).\n"
                                "- Prompt: Is it time-bound? (yes/no): (store in time_bound variable).\n"
                                "- Use a match case statement to react based on priority.\n"
                                "- Use an if statement to modify the message if time_bound is 'yes'.\n"
                                "- Print a reminder that includes the task, its priority, and whether it requires immediate attention.\n"
                            ),
                            "order": 4,
                            "is_mandatory": True,
                            "checkers": [
                                "Checks for file daily_reminder.py exists and not empty",
                                "Checks for user prompts: task, priority, time-bound",
                                "Checks for match case statement reaction implementation",
                                "Checks for use of if statement to modify the reminder if the task is time-bound",
                                "Checks for providing a customized reminder",
                                "Checks for printing a reminder that includes task, priority, and time sensitivity",
                            ],
                        },
                    ],
                },

                  {
                    "title": "Functions, Data Structures and Modules",
                    "slug": "functions-data-structures-and-modules",
                    "description": (
                        "Learn how to define and use functions, work with core Python data structures "
                        "like lists and dictionaries, and organize code using modules."
                    ),
                    "order": 3,
                    "objectives": [
                        "Define the purpose and importance of functions in Python programming.",
                        "Construct functions using def and lambda keywords, understanding proper syntax.",
                        "Work with function parameters, argument passing mechanisms, default values, and keyword arguments.",
                        "Explain the concept of return values and utilize the return statement effectively.",
                        "Distinguish between local and global variable scope within functions.",
                        "Apply global and nonlocal keywords appropriately to manage variable scope.",
                        "Identify common Python data structures: Lists, Tuples, Sets, and Dictionaries.",
                        "Select the appropriate data structure based on the type of data and operations needed.",
                        "Perform operations on Lists (indexing, slicing, appending, etc.).",
                        "Utilize Dictionary methods, understand the immutability of Tuples, and perform Set operations.",
                        "Explain the concepts of modules and packages in Python.",
                        "Create and use custom modules, and import standard modules provided by Python.",
                        "Install and use external Python libraries using pip.",
                        "Identify some essential Python libraries and their functionalities (e.g., requests).",
                        "Comprehend the LEGB rule (Local, Enclosing, Global, Built-in) for understanding variable scope in Python.",
                        "Implement best practices for effective variable scope management.",
                        "Explain the concept of namespaces in Python and differentiate between their types.",
                        "Describe the lifecycle of a namespace and how scope resolution works in Python.",
                    ],
                    "tasks": [
                        {
                            "title": "0. Arithmetic Operations Function",
                            "instructions": (
                                "Create a module named arithmetic_operations.py that defines a function perform_operation "
                                "to perform basic arithmetic operations.\n\n"
                                "Requirements for arithmetic_operations.py:\n"
                                "- Define a function: perform_operation(num1: float, num2: float, operation: str).\n"
                                "- Supported operations: 'add', 'subtract', 'multiply', 'divide'.\n"
                                "- Execute the appropriate arithmetic operation based on the operation parameter.\n"
                                "- For division, handle division by zero gracefully (e.g., return a specific message or value).\n"
                                "- Return the result.\n\n"
                                "A main.py script (provided) will import perform_operation and:\n"
                                "- Prompt for num1 and num2 as floats.\n"
                                "- Prompt for operation.\n"
                                "- Call perform_operation and print the result.\n"
                                "You only need to implement arithmetic_operations.py; main.py is provided for testing."
                            ),
                            "order": 0,
                            "is_mandatory": True,
                            "checkers": [
                                "Checks for file arithmetic_operations.py exists and not empty",
                                "Checks for function named perform_operation with parameters num1, num2, and operation",
                                "Checks for implementation of the chosen operation",
                                "Checks for divide by zero scenario handling",
                            ],
                        },
                        {
                            "title": "1. Shopping List Manager",
                            "instructions": (
                                "Create a script named shopping_list_manager.py that manages a shopping list using a list.\n\n"
                                "Requirements:\n"
                                "- Start with an empty list named shopping_list.\n"
                                "- Implement a loop that displays a menu until the user chooses to exit.\n"
                                "- Menu options:\n"
                                "  1. Add Item: prompt for an item name and append it to shopping_list.\n"
                                "  2. Remove Item: prompt for an item name and remove it; if not found, print a message.\n"
                                "  3. View List: print each item in shopping_list.\n"
                                "  4. Exit: print 'Goodbye!' and break the loop.\n"
                                "- Handle invalid menu choices gracefully.\n\n"
                                "You are given a skeleton with display_menu() and main(); complete main() with the described logic."
                            ),
                            "order": 1,
                            "is_mandatory": True,
                            "checkers": [
                                "Checks for file shopping_list_manager.py exists and not empty",
                                "Checks for definition of the display_menu function",
                                "Checks for implementation of a list named shopping_list",
                                "Checks for calling display_menu function inside the loop",
                                "Checks for implementation of choice input as a number or string-based selection",
                            ],
                        },
                        {
                            "title": "2. Explore datetime Module",
                            "instructions": (
                                "Create a script named explore_datetime.py to practice using Python's datetime module.\n\n"
                                "Part 1: Display the current date and time\n"
                                "- Import the datetime module.\n"
                                "- Create a function display_current_datetime.\n"
                                "- Inside it, save the current date/time in a variable current_date.\n"
                                "- Format and print the current date and time, e.g. 'YYYY-MM-DD HH:MM:SS'.\n\n"
                                "Part 2: Calculate a future date\n"
                                "- Prompt the user for a number of days (integer).\n"
                                "- Create a function calculate_future_date.\n"
                                "- Inside it, compute future_date by adding the given days to the current date.\n"
                                "- Print the future date in 'YYYY-MM-DD' format.\n\n"
                                "Hints:\n"
                                "- Use datetime.now() to get the current date/time.\n"
                                "- Use timedelta(days=number_of_days) to add days."
                            ),
                            "order": 2,
                            "is_mandatory": True,
                            "checkers": [
                                "Checks for file explore_datetime.py exists and not empty",
                                "Checks for import of the datetime module",
                                "Checks for display_current_datetime function definition",
                                "Checks for calculate_future_date function definition",
                                "Checks for formatting of the current date and time",
                                "Checks for returning or printing the formatted future date",
                            ],
                        },
                        {
                            "title": "3. Temperature Conversion Tool",
                            "instructions": (
                                "Create a script named temp_conversion_tool.py that converts temperatures between Celsius and Fahrenheit,\n"
                                "demonstrating the use of global variables for conversion factors.\n\n"
                                "Requirements:\n"
                                "- Define global variables FAHRENHEIT_TO_CELSIUS_FACTOR and CELSIUS_TO_FAHRENHEIT_FACTOR at the top.\n"
                                "  (e.g. FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9, CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5).\n"
                                "- Implement convert_to_celsius(fahrenheit) using the global factor.\n"
                                "- Implement convert_to_fahrenheit(celsius) using the global factor.\n"
                                "- Prompt the user: Enter the temperature to convert: (numeric input).\n"
                                "- Prompt: Is this temperature in Celsius or Fahrenheit? (C/F):\n"
                                "- Based on the unit, call the appropriate function and print the converted temperature.\n"
                                "- If the user enters an invalid temperature (non-numeric), raise a ValueError with\n"
                                "  message: 'Invalid temperature. Please enter a numeric value.'\n"
                                "- Handle invalid unit choices gracefully.\n"
                            ),
                            "order": 3,
                            "is_mandatory": True,
                            "checkers": [
                                "Checks for file temp_conversion_tool.py exists and not empty",
                                "Checks for definition of global conversion factors",
                                "Checks for implementation of convert_to_celsius and convert_to_fahrenheit functions",
                                "Checks for user interaction (temperature and unit prompts)",
                                "Checks for implementation of ValueError for invalid temperature input",
                            ],
                        },
                    ],
                },
            ],
        },
        
        
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