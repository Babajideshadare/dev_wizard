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

                  {
                    "title": "Programming Paradigms & Exception handling",
                    "slug": "programming-paradigms-and-exception-handling",
                    "description": (
                        "Understand core OOP concepts, how to handle exceptions robustly, and how to "
                        "write basic unit tests using Python's unittest module."
                    ),
                    "order": 4,
                    "objectives": [
                        "Explain the core concepts of OOP: classes, objects, encapsulation, and abstraction.",
                        "Discuss the significance of OOP in software development and its advantages over other programming paradigms.",
                        "Define classes and create objects in Python.",
                        "Understand the difference between class attributes, instance methods, and the role of the self keyword within classes.",
                        "Differentiate between syntax errors and exceptions in Python.",
                        "Identify common Python exceptions and understand their causes.",
                        "Utilize try, except, else, and finally blocks to handle exceptions effectively.",
                        "Raise exceptions using the raise keyword and create custom exceptions for specific errors in your code.",
                        "Explain the importance of testing in software development.",
                        "Describe different types of testing, with a focus on unit testing.",
                        "Write basic unit tests using Python’s unittest module to verify the functionality of your code.",
                        "Structure test cases effectively and understand how test runners work.",
                    ],
                    "tasks": [
                        {
                            "title": "0. Create a Simple Bank Account Class",
                            "instructions": (
                                "Create a BankAccount class and a CLI interface to perform basic banking operations.\n\n"
                                "bank_account.py:\n"
                                "- Define class BankAccount.\n"
                                "- __init__(self, initial_balance=0): initialize an account_balance attribute.\n"
                                "- Implement deposit(amount): add amount to account_balance.\n"
                                "- Implement withdraw(amount): if sufficient funds, subtract and return True; otherwise return False.\n"
                                "- Implement display_balance(): print current balance in a user-friendly format.\n\n"
                                "main-0.py:\n"
                                "- Uses command line arguments to interact with BankAccount.\n"
                                "- Example skeleton uses: python main-0.py <command>:<amount> with commands deposit, withdraw, display.\n"
                                "- You must ensure BankAccount behaves correctly for deposits, withdrawals, and balance display.\n"
                            ),
                            "order": 0,
                            "is_mandatory": True,
                            "checkers": [
                                "Checks files bank_account.py and main-0.py exist and are not empty",
                                "Checks for implementation of class BankAccount",
                                "Checks for initialization of BankAccount with an account_balance",
                                "Checks for deposit and withdraw methods",
                                "Checks for implementation of display_balance method",
                                "Checks for correct output when depositing",
                                "Checks for correct output when withdrawing with sufficient funds",
                                "Checks for correct output when withdrawing more than the balance",
                                "Checks for correct output when displaying balance",
                            ],
                        },
                        {
                            "title": "1. Robust Division Calculator with Command Line Arguments",
                            "instructions": (
                                "Create robust_division_calculator.py and main.py to perform safe division with error handling.\n\n"
                                "robust_division_calculator.py:\n"
                                "- Define function safe_divide(numerator, denominator).\n"
                                "- Attempt to convert numerator and denominator to floats.\n"
                                "- Use try/except to handle:\n"
                                "  * ValueError when inputs are non-numeric: return 'Error: Please enter numeric values only.'\n"
                                "  * ZeroDivisionError when denominator is zero: return 'Error: Cannot divide by zero.'\n"
                                "- On success, return a message: 'The result of the division is X'.\n\n"
                                "main.py:\n"
                                "- Imports safe_divide.\n"
                                "- Expects exactly two command line arguments: numerator and denominator.\n"
                                "- Calls safe_divide and prints the returned message.\n"
                            ),
                            "order": 1,
                            "is_mandatory": True,
                            "checkers": [
                                "Checks if robust_division_calculator.py and main.py exist and are not empty",
                                "Checks for definition of safe_divide function",
                                "Checks for try/except blocks implementation",
                                "Checks for conversion of inputs into floats",
                                "Checks for ZeroDivisionError handling",
                                "Checks for ValueError handling for non-numeric inputs",
                                "Checks for correct output message for normal division",
                                "Checks for correct output message for division by zero",
                                "Checks for correct output message for non-numeric values",
                            ],
                        },
                        {
                            "title": "2. Writing Unit Tests for a Simple Calculator Class",
                            "instructions": (
                                "Write unit tests for the provided SimpleCalculator class in simple_calculator.py.\n\n"
                                "Provided: simple_calculator.py with class SimpleCalculator supporting add, subtract, multiply, divide.\n"
                                "Your task: create test_simple_calculator.py and write unittest-based tests.\n\n"
                                "Guidelines:\n"
                                "- Import unittest and SimpleCalculator.\n"
                                "- Define class TestSimpleCalculator(unittest.TestCase).\n"
                                "- Implement setUp() to create self.calc = SimpleCalculator().\n"
                                "- Write test methods:\n"
                                "  * test_addition\n"
                                "  * test_subtraction\n"
                                "  * test_multiply\n"
                                "  * test_divide (including division by zero, expecting None).\n"
                                "- Use assertions like self.assertEqual to verify results.\n"
                                "- Run tests with: python -m unittest test_simple_calculator.py.\n"
                            ),
                            "order": 2,
                            "is_mandatory": True,
                            "checkers": [
                                "Checks that test_simple_calculator.py exists and is not empty",
                                "Checks for necessary imports: unittest and SimpleCalculator",
                                "Checks for definition of a TestSimpleCalculator test class",
                                "Checks for test_addition test cases",
                                "Checks for test_subtraction test cases",
                                "Checks for test_multiply test cases",
                                "Checks for test_divide test cases (including division by zero)",
                            ],
                        },
                        {
                            "title": "3. Implementing Basic OOP for a Library Management System",
                            "instructions": (
                                "Implement a simple library management system using OOP in library_management.py.\n\n"
                                "Requirements:\n"
                                "- Implement class Book with public attributes title and author, and a private attribute _is_checked_out.\n"
                                "- Book should provide methods to check a book out and return it (updating _is_checked_out).\n"
                                "- Implement class Library with a private list _books to store Book instances.\n"
                                "- Library methods:\n"
                                "  * add_book(book): add a Book instance to the collection.\n"
                                "  * check_out_book(title): mark the book with the given title as checked out (if available).\n"
                                "  * return_book(title): mark the book with the given title as returned.\n"
                                "  * list_available_books(): print available books in 'Title by Author' format.\n\n"
                                "Provided main.py sets up a small library, checks out and returns a book, and prints the available books."
                            ),
                            "order": 3,
                            "is_mandatory": True,
                            "checkers": [
                                "Checks that library_management.py exists and is not empty",
                                "Checks for successful creation of classes Library and Book",
                                "Checks for initialization of the library's internal collection",
                                "Checks for methods in Book class to check out and return a book",
                                "Checks for methods in Library class: add_book, check_out_book, return_book",
                                "Checks for list_available_books method in Library",
                            ],
                        },
                    ],
                },

                {
                    "title": "More about OOP",
                    "slug": "more-about-oop",
                    "description": (
                        "Explore advanced OOP concepts in Python, including magic methods, inheritance vs composition, "
                        "polymorphism, and class vs static methods."
                    ),
                    "order": 5,
                    "objectives": [
                        "Describe the functionalities of constructors (__init__), destructors (__del__), and common magic methods (e.g., __str__, __repr__) in Python classes.",
                        "Implement inheritance to create new classes that inherit properties and methods from existing classes.",
                        "Utilize composition as an alternative to inheritance for building complex objects.",
                        "Explain the concepts of single, multiple, and multilevel inheritance in Python.",
                        "Understand the method resolution order (MRO) in Python and how it affects method calls in inheritance hierarchies.",
                        "Implement polymorphism and method overriding to create flexible and reusable code.",
                        "Explain and use Python’s duck typing to achieve polymorphic behavior.",
                        "Distinguish between class methods and static methods based on their usage and purpose.",
                        "Apply @classmethod and @staticmethod decorators appropriately in your Python classes.",
                    ],
                    "tasks": [
                        {
                            "title": "0. Dive into Python Magic Methods",
                            "instructions": (
                                "Create a script named book_class.py and define a Book class that demonstrates key magic methods.\n\n"
                                "Requirements for Book class in book_class.py:\n"
                                "- Attributes: title (str), author (str), year (int).\n"
                                "- __init__(self, title, author, year): initialize the attributes.\n"
                                "- __del__(self): print 'Deleting <title>' when the object is deleted.\n"
                                "- __str__(self): return '<title> by <author>, published in <year>'.\n"
                                "- __repr__(self): return a recreatable representation like: "
                                "Book('1984', 'George Orwell', 1949).\n\n"
                                "Provided main.py imports Book, instantiates it, prints it with str() and repr(), "
                                "and then deletes it to trigger __del__."
                            ),
                            "order": 0,
                            "is_mandatory": True,
                            "checkers": [
                                "Checks book_class.py and main.py files exist and are not empty",
                                "Checks for successful creation of class Book",
                                "Checks for proper initialization of Book attributes",
                                "Checks for implementation of magic methods __init__, __del__, __str__, and __repr__",
                                "Checks for correct string and repr output",
                            ],
                        },
                        {
                            "title": "1. Mastering Inheritance and Composition in Python",
                            "instructions": (
                                "Develop library_system.py and a main.py to demonstrate inheritance and composition.\n\n"
                                "library_system.py:\n"
                                "- Base class Book with attributes title and author; __init__(self, title, author).\n"
                                "- Derived class EBook(Book) with additional attribute file_size (int) and its own __init__ "
                                "that calls super().__init__(title, author).\n"
                                "- Derived class PrintBook(Book) with additional attribute page_count (int) and its own __init__.\n"
                                "- Library class using composition:\n"
                                "  * Attribute books: a list to store Book/EBook/PrintBook instances.\n"
                                "  * add_book(self, book): add a book instance to the list.\n"
                                "  * list_books(self): print details of each book, e.g.:\n"
                                "    - Book: Pride and Prejudice by Jane Austen\n"
                                "    - EBook: Snow Crash by Neal Stephenson, File Size: 500KB\n"
                                "    - PrintBook: The Catcher in the Rye by J.D. Salinger, Page Count: 234\n\n"
                                "main.py imports Book, EBook, PrintBook, Library, creates instances, adds them to Library, "
                                "and calls list_books()."
                            ),
                            "order": 1,
                            "is_mandatory": True,
                            "checkers": [
                                "Checks library_system.py and main.py files exist and are not empty",
                                "Checks for implementation of base class Book and derived classes EBook and PrintBook",
                                "Checks for correct initialization of Book and derived classes",
                                "Checks for implementation of EBook-specific attribute file_size",
                                "Checks for implementation of PrintBook-specific attribute page_count",
                                "Checks for implementation of Library class and its methods add_book and list_books",
                                "Checks for correct output when listing books",
                            ],
                        },
                        {
                            "title": "2. Exploring Polymorphism and Method Overriding",
                            "instructions": (
                                "Create polymorphism_demo.py to demonstrate polymorphism with a Shape hierarchy.\n\n"
                                "polymorphism_demo.py:\n"
                                "- Base class Shape with method area(self) that raises NotImplementedError.\n"
                                "- Derived class Rectangle(Shape): attributes length and width; override area() to return length * width.\n"
                                "- Derived class Circle(Shape): attribute radius; override area() to return math.pi * radius ** 2.\n\n"
                                "Provided main.py imports Shape, Rectangle, Circle and:\n"
                                "- Creates shapes = [Rectangle(10, 5), Circle(7)].\n"
                                "- Loops over shapes and prints: The area of the <ClassName> is: <area>.\n"
                                "This should show polymorphic behavior via overridden area() methods."
                            ),
                            "order": 2,
                            "is_mandatory": True,
                            "checkers": [
                                "Checks polymorphism_demo.py and main.py files exist and are not empty",
                                "Checks for import of math module",
                                "Checks for implementation and initialization of Shape, Rectangle, and Circle classes",
                                "Checks for overriding of area method in Rectangle and Circle",
                                "Checks for correct area output for Rectangle and Circle",
                            ],
                        },
                        {
                            "title": "3. Distinguishing Between Class Methods and Static Methods",
                            "instructions": (
                                "Create class_static_methods_demo.py with a Calculator class demonstrating @staticmethod and @classmethod.\n\n"
                                "Calculator class:\n"
                                "- Class attribute calculation_type = 'Arithmetic Operations'.\n"
                                "- @staticmethod add(a, b): return a + b.\n"
                                "- @classmethod multiply(cls, a, b):\n"
                                "  * Print 'Calculation type: <cls.calculation_type>'.\n"
                                "  * Return the product a * b.\n\n"
                                "Provided main.py imports Calculator and:\n"
                                "- Calls Calculator.add(10, 5) and prints: The sum is: 15\n"
                                "- Calls Calculator.multiply(10, 5) and prints:\n"
                                "  Calculation type: Arithmetic Operations\n"
                                "  The product is: 50\n"
                            ),
                            "order": 3,
                            "is_mandatory": True,
                            "checkers": [
                                "Checks class_static_methods_demo.py and main.py files exist and are not empty",
                                "Checks for implementation of Calculator class",
                                "Checks for implementation of static method add",
                                "Checks for implementation of class method multiply using cls and calculation_type",
                                "Checks for correct output of sum and product including the calculation_type message",
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

        {
            "name": "Django",
            "slug": "django",
            "description": "Introduction to Django: environment setup, models, and admin interface.",
            "order": 3,
            "topics": [
                {
                    "title": "Introduction to Django",
                    "slug": "introduction-to-django",
                    "description": "Set up a Django project, create models, perform CRUD with the ORM, and use the Django admin.",
                    "order": 1,
                    "objectives": [
                        "Install Django and create a new Django project.",
                        "Familiarize yourself with the project’s default structure and run the development server.",
                        "Create a Django app.",
                        "Define Django models with specified attributes.",
                        "Perform and document CRUD operations using Django’s ORM via the Django shell.",
                        "Register your models with the Django admin.",
                        "Customize the admin interface to enhance the management and visibility of your data.",
                    ],
                    "tasks": [
                        {
                            "title": "0. Introduction to Django Development Environment Setup",
                            "instructions": (
                                "Install Django and create a new Django project named LibraryProject.\n\n"
                                "Steps:\n"
                                "- Ensure Python is installed.\n"
                                "- Install Django with: pip install django.\n"
                                "- Create a project: django-admin startproject LibraryProject.\n"
                                "- Navigate into LibraryProject.\n"
                                "- Create a README.md file inside LibraryProject and describe the project.\n"
                                "- Run the dev server: python manage.py runserver.\n"
                                "- Open http://127.0.0.1:8000/ and confirm the Django welcome page.\n"
                                "- Explore manage.py, settings.py, and urls.py to understand their roles."
                            ),
                            "order": 0,
                            "is_mandatory": True,
                            "checkers": [
                                "Checks for a non-empty README.md file within the LibraryProject directory",
                                "Check for the existence of manage.py file in the right location",
                                "Checks for the existence of settings-related file (settings.py) in the right location",
                                "Checks the content of the settings.py file",
                            ],
                        },
                        {
                            "title": "1. Implementing and Interacting with Django Models",
                            "instructions": (
                                "Within LibraryProject, create an app named bookshelf and define a Book model.\n\n"
                                "Steps:\n"
                                "- In the project directory, run: python manage.py startapp bookshelf.\n"
                                "- In bookshelf/models.py, define a Book model with fields:\n"
                                "  * title = CharField(max_length=200)\n"
                                "  * author = CharField(max_length=100)\n"
                                "  * publication_year = IntegerField()\n"
                                "- Add 'bookshelf' to INSTALLED_APPS in settings.py.\n"
                                "- Run: python manage.py makemigrations bookshelf\n"
                                "- Run: python manage.py migrate\n"
                                "- Open Django shell: python manage.py shell and perform CRUD:\n"
                                "  * Create a Book: title='1984', author='George Orwell', publication_year=1949.\n"
                                "  * Retrieve and display it.\n"
                                "  * Update the title to 'Nineteen Eighty-Four'.\n"
                                "  * Delete the book.\n"
                                "- Document each operation and its output in separate files: create.md, retrieve.md, update.md, delete.md.\n"
                                "- Optionally, summarize all operations in CRUD_operations.md."
                            ),
                            "order": 1,
                            "is_mandatory": True,
                            "checkers": [
                                "Check if Book model is defined in bookshelf/models.py",
                                "Check if Book model has required fields: title, author, publication_year",
                                "Check that create.md exists and contains create commands and output",
                                "Check that retrieve.md exists and contains retrieve commands and output",
                                "Check that update.md exists and contains update commands and output",
                                "Check that delete.md exists and contains delete commands and output",
                            ],
                        },
                        {
                            "title": "2. Utilizing the Django Admin Interface",
                            "instructions": (
                                "Register the Book model in the Django admin and customize its list display.\n\n"
                                "Steps:\n"
                                "- In bookshelf/admin.py, import Book and register it with admin.\n"
                                "- Configure a ModelAdmin so that the list view displays: title, author, publication_year.\n"
                                "- Add list_filter for publication_year or author to filter books.\n"
                                "- Add search_fields for title and author to allow searching.\n"
                                "- Run the server, log into /admin/, and verify that Book entries are visible and manageable."
                            ),
                            "order": 2,
                            "is_mandatory": True,
                            "checkers": [
                                "Check for bookshelf/admin.py file existence",
                                "Check for Book model registration in the admin",
                                "Check for list_filter configuration on the Book admin",
                                "Check for search_fields configuration on the Book admin",
                            ],
                        },
                    ],
                },

                {
                    "title": "Django Models and Views",
                    "slug": "django-models-and-views",
                    "description": (
                        "Work with advanced Django model relationships, build views and URL configurations, "
                        "and implement authentication, role-based access control, and custom permissions."
                    ),
                    "order": 2,
                    "objectives": [
                        "Master Django’s ORM capabilities by creating models that demonstrate ForeignKey, ManyToMany, and OneToOne relationships.",
                        "Effectively model complex data relationships in a Django project.",
                        "Gain proficiency in creating function-based and class-based views in Django.",
                        "Configure URL patterns to handle web requests effectively, routing them to the appropriate views.",
                        "Set up user login, logout, and registration functionalities using Django’s built-in authentication system.",
                        "Develop views and templates to demonstrate user session and permission management.",
                        "Extend the Django User model to include user roles and create views that restrict access based on these roles.",
                        "Utilize Django signals to automatically create a UserProfile when a new user is registered.",
                        "Add custom permissions to the Book model to control actions such as adding, editing, and deleting entries based on user roles.",
                        "Enforce these permissions in views, ensuring only authorized users can perform specific actions.",
                    ],
                    "tasks": [
                        {
                            "title": "0. Implementing Advanced Model Relationships in Django",
                            "instructions": (
                                "Create a new app relationship_app in your Django project and define models using "
                                "ForeignKey, ManyToMany, and OneToOne fields.\n\n"
                                "Models in relationship_app/models.py:\n"
                                "- Author: name (CharField)\n"
                                "- Book: title (CharField), author (ForeignKey to Author)\n"
                                "- Library: name (CharField), books (ManyToManyField to Book)\n"
                                "- Librarian: name (CharField), library (OneToOneField to Library)\n\n"
                                "Run migrations for relationship_app, then create a script query_samples.py in the "
                                "relationship_app directory that demonstrates queries to:\n"
                                "- Query all books by a specific author.\n"
                                "- List all books in a library.\n"
                                "- Retrieve the librarian for a library.\n"
                            ),
                            "order": 0,
                            "is_mandatory": True,
                            "checkers": [
                                "Checks for implementation of Author model",
                                "Checks for implementation of Book model",
                                "Checks for implementation of Library model with ManyToMany to Book",
                                "Checks for implementation of Librarian model with OneToOne to Library",
                                "Checks for existence of query_samples.py file",
                                "Checks for 'Query all books by a specific author' query",
                                "Checks for 'List all books in a library' query",
                                "Checks for 'Retrieve the librarian for a library' query",
                            ],
                        },
                        {
                            "title": "1. Django Views and URL Configuration",
                            "instructions": (
                                "In relationship_app, add views and URLs to display information about books and libraries.\n\n"
                                "Views in relationship_app/views.py:\n"
                                "- Function-based view to list all books (titles and authors) from the database.\n"
                                "  * Optionally render list_books.html template with context variable 'books'.\n"
                                "- Class-based view (ListView or DetailView) to display details for a specific library, "
                                "including all its books.\n"
                                "  * Optionally render library_detail.html template.\n\n"
                                "URLs:\n"
                                "- Create relationship_app/urls.py and define URL patterns for:\n"
                                "  * The function-based book list view.\n"
                                "  * The class-based library detail view (e.g. path('library/<int:pk>/', ...)).\n\n"
                                "Templates (optional but recommended):\n"
                                "- list_books.html: loops over 'books' and shows title and author.\n"
                                "- library_detail.html: shows a particular library and its related books."
                            ),
                            "order": 1,
                            "is_mandatory": True,
                            "checkers": [
                                "Checks for function-based view that renders a list of book titles and their authors",
                                "Checks for class-based view in relationship_app/views.py that displays library details with its books",
                                "Checks for use of Django's ListView or DetailView for the class-based view",
                                "Checks that relationship_app/urls.py routes to both the function-based and class-based views",
                                "Checks for implementation of list_books.html and library_detail.html templates (or equivalent)",
                            ],
                        },
                        {
                            "title": "2. Implementing User Authentication in Django",
                            "instructions": (
                                "Enhance relationship_app by adding login, logout, and registration functionality using "
                                "Django's built-in auth system.\n\n"
                                "Steps:\n"
                                "- Create views or use Django's built-in auth views for:\n"
                                "  * User login\n"
                                "  * User logout\n"
                                "  * User registration (using UserCreationForm)\n"
                                "- Create templates in relationship_app/templates/relationship_app/:\n"
                                "  * login.html\n"
                                "  * logout.html\n"
                                "  * register.html\n"
                                "- Configure URL patterns in relationship_app/urls.py to link to these views.\n"
                                "- Test that users can register, log in, and log out, and that sessions work correctly."
                            ),
                            "order": 2,
                            "is_mandatory": True,
                            "checkers": [
                                "Checks that views for login, logout, and registration are implemented using Django's built-in auth tools",
                                "Checks that URL patterns in relationship_app/urls.py link to the authentication views",
                                "Checks that provided templates (login.html, logout.html, register.html) are implemented",
                                "Checks that users can successfully register, log in, and log out",
                            ],
                        },
                        {
                            "title": "3. Implement Role-Based Access Control in Django",
                            "instructions": (
                                "Implement role-based access control by extending the User model with a UserProfile and "
                                "restricting views based on roles.\n\n"
                                "UserProfile model:\n"
                                "- user: OneToOneField to Django's User.\n"
                                "- role: CharField with choices: 'Admin', 'Librarian', 'Member'.\n"
                                "- Use Django signals (post_save) to automatically create a UserProfile when a User is created.\n\n"
                                "Role-based views:\n"
                                "- Implement three role-specific views:\n"
                                "  * admin_view (for Admin users only)\n"
                                "  * librarian_view (for Librarian users only)\n"
                                "  * member_view (for Member users only)\n"
                                "- Use @user_passes_test to ensure only users with the appropriate role can access each view.\n\n"
                                "URLs and templates:\n"
                                "- Define URLs for each role-based view.\n"
                                "- Create templates:\n"
                                "  * admin_view.html\n"
                                "  * librarian_view.html\n"
                                "  * member_view.html\n"
                                "to show content tailored to each role."
                            ),
                            "order": 3,
                            "is_mandatory": True,
                            "checkers": [
                                "Checks for creation of a UserProfile model with OneToOneField to User and role field",
                                "Checks for use of Django signals to auto-create UserProfile on user registration",
                                "Checks for admin_view restricted to Admin role",
                                "Checks for librarian_view restricted to Librarian role",
                                "Checks for member_view restricted to Member role",
                                "Checks for use of @user_passes_test decorator to enforce role-based access",
                            ],
                        },
                        {
                            "title": "4. Implementing Custom Permissions in Django",
                            "instructions": (
                                "Extend the Book model in relationship_app with custom permissions and enforce them in views.\n\n"
                                "Step 1: Book model Meta permissions:\n"
                                "- Inside the Book model, define a nested Meta class.\n"
                                "- In Meta, specify a permissions tuple including:\n"
                                "  * ('can_add_book', 'Can add book')\n"
                                "  * ('can_change_book', 'Can change book')\n"
                                "  * ('can_delete_book', 'Can delete book')\n\n"
                                "Step 2: Permission-protected views:\n"
                                "- Create or update views to handle adding, editing, and deleting Book instances.\n"
                                "- Decorate these views with @permission_required using the custom permissions above.\n\n"
                                "Step 3: URLs:\n"
                                "- Define URL patterns for add, edit, and delete book views in urls.py.\n"
                                "- Ensure that only users with the proper permissions can access these views."
                            ),
                            "order": 4,
                            "is_mandatory": True,
                            "checkers": [
                                "Checks that a nested Meta class is defined inside the Book model",
                                "Checks that Meta.permissions includes can_add_book, can_change_book, and can_delete_book",
                                "Checks that views for add, edit, delete books use @permission_required with the custom permissions",
                                "Checks that urls.py defines paths for the secured book actions",
                            ],
                        },
                    ],
                },

                 {
                    "title": "Advanced Features and Security",
                    "slug": "advanced-features-and-security",
                    "description": (
                        "Implement a custom user model, manage permissions and groups, and apply security best practices "
                        "including HTTPS and secure redirects in a Django project."
                    ),
                    "order": 3,
                    "objectives": [
                        "Customize Django’s user model to include additional fields and functionality.",
                        "Configure settings and integrate the custom user model into the Django admin.",
                        "Implement and manage permissions and groups to control access to various parts of your application.",
                        "Develop views that enforce these permissions and document the setup process.",
                        "Configure Django settings to prevent security vulnerabilities and ensure data privacy.",
                        "Protect views and templates against common security threats such as CSRF, XSS, and SQL injection.",
                        "Configure Django to handle secure HTTPS connections and enforce HTTPS redirects.",
                        "Adjust settings for secure cookies and implement secure headers to protect against various attacks.",
                    ],
                    "tasks": [
                        {
                            "title": "0. Implementing a Custom User Model in Django",
                            "instructions": (
                                "Replace Django's default user model with a custom user model that includes additional fields.\n\n"
                                "Steps:\n"
                                "- Duplicate your existing django-models project to a new project named advanced_features_and_security.\n"
                                "- Create a custom user model extending AbstractUser with extra fields:\n"
                                "  * date_of_birth (DateField)\n"
                                "  * profile_photo (ImageField)\n"
                                "- In settings.py, set AUTH_USER_MODEL to point to your custom user model.\n"
                                "- Implement a custom user manager with create_user and create_superuser handling the new fields.\n"
                                "- Update admin.py with a custom ModelAdmin to manage the custom user model and display the new fields.\n"
                                "- Update any ForeignKey or references to User in other models to use the new custom user model.\n"
                            ),
                            "order": 0,
                            "is_mandatory": True,
                            "checkers": [
                                "Check for models.py file existence and custom user model definition",
                                "Check for custom user manager definition (create_user and create_superuser)",
                                "Check for custom user admin registration in admin.py",
                                "Check for settings.py configuration of AUTH_USER_MODEL",
                            ],
                        },
                        {
                            "title": "1. Managing Permissions and Groups in Django",
                            "instructions": (
                                "Implement detailed access control using groups and permissions.\n\n"
                                "Steps:\n"
                                "- In one of your models (e.g., Book), add custom permissions in Meta.permissions:\n"
                                "  * can_view, can_create, can_edit, can_delete\n"
                                "- In Django admin, create groups such as Editors, Viewers, and Admins.\n"
                                "- Assign appropriate permissions to each group (e.g., Editors have can_create and can_edit).\n"
                                "- In views.py, protect views that create, edit, or delete instances using @permission_required decorators.\n"
                                "- Example: @permission_required('app_name.can_edit', raise_exception=True) for an edit view.\n"
                                "- Create or update a README.md or comments explaining which permissions and groups exist, "
                                "how they are set up, and how they are used.\n"
                            ),
                            "order": 1,
                            "is_mandatory": True,
                            "checkers": [
                                "Check for models.py file existence and custom permissions definition (can_view, can_create, can_edit, can_delete)",
                                "Check for views.py file existence and use of permission decorators on protected views",
                                "Check for README.md file existence and content documenting permissions and groups setup",
                            ],
                        },
                        {
                            "title": "2. Implementing Security Best Practices in Django",
                            "instructions": (
                                "Configure security-related settings and code to protect against common web vulnerabilities.\n\n"
                                "Steps:\n"
                                "- In settings.py, configure secure settings (for production):\n"
                                "  * DEBUG = False\n"
                                "  * SECURE_BROWSER_XSS_FILTER = True\n"
                                "  * X_FRAME_OPTIONS = 'DENY'\n"
                                "  * SECURE_CONTENT_TYPE_NOSNIFF = True\n"
                                "  * CSRF_COOKIE_SECURE = True\n"
                                "  * SESSION_COOKIE_SECURE = True\n"
                                "- Ensure all form templates include {% csrf_token %}.\n"
                                "- In views, avoid raw SQL string concatenation; use Django ORM and forms/validation to prevent SQL injection.\n"
                                "- Optionally implement a Content Security Policy (CSP) via middleware or custom headers.\n"
                                "- Document the security measures applied with comments in settings.py, views, or a small security README.\n"
                            ),
                            "order": 2,
                            "is_mandatory": True,
                            "checkers": [
                                "Check if settings.py contains the necessary security configurations (DEBUG, X_FRAME_OPTIONS, SECURE_* flags)",
                                "Check if forms.py contains the definition of ExampleForm (if used for secure input handling)",
                                "Check if views.py imports and uses ExampleForm correctly",
                                "Check if form_example.html template file exists",
                                "Check if book_list.html template file exists",
                            ],
                        },
                        {
                            "title": "3. Implementing HTTPS and Secure Redirects in Django",
                            "instructions": (
                                "Configure Django and your deployment environment to enforce HTTPS and secure headers.\n\n"
                                "Steps:\n"
                                "- In settings.py, set:\n"
                                "  * SECURE_SSL_REDIRECT = True\n"
                                "  * SECURE_HSTS_SECONDS = 31536000 (e.g., one year)\n"
                                "  * SECURE_HSTS_INCLUDE_SUBDOMAINS = True\n"
                                "  * SECURE_HSTS_PRELOAD = True\n"
                                "  * SESSION_COOKIE_SECURE = True\n"
                                "  * CSRF_COOKIE_SECURE = True\n"
                                "  * X_FRAME_OPTIONS = 'DENY'\n"
                                "  * SECURE_CONTENT_TYPE_NOSNIFF = True\n"
                                "  * SECURE_BROWSER_XSS_FILTER = True\n"
                                "- Ensure your deployment (e.g., Nginx/Apache) is configured with SSL/TLS certificates.\n"
                                "- Document the HTTPS configuration and security headers in your deployment notes or README.\n"
                            ),
                            "order": 3,
                            "is_mandatory": True,
                            "checkers": [
                                "Checks that SECURE_SSL_REDIRECT is set to True",
                                "Checks that SECURE_HSTS_SECONDS is set to a suitable value (e.g. 31536000)",
                                "Checks that SECURE_HSTS_INCLUDE_SUBDOMAINS and SECURE_HSTS_PRELOAD are set to True",
                                "Checks that SESSION_COOKIE_SECURE is set to True",
                                "Checks that CSRF_COOKIE_SECURE is set to True",
                                "Checks for secure headers implementation (X_FRAME_OPTIONS, SECURE_CONTENT_TYPE_NOSNIFF, SECURE_BROWSER_XSS_FILTER)",
                            ],
                        },
                    ],
                },

                  {
                    "title": "Django: Building a Complete Django Application",
                    "slug": "django-building-complete-application",
                    "description": (
                        "Build a full-featured Django blog application with authentication, post management, "
                        "comments, tagging, and search functionality."
                    ),
                    "order": 4,
                    "objectives": [
                        "Initialize and configure a new Django project tailored for a blogging platform.",
                        "Establish the initial models and prepare the base templates.",
                        "Develop a comprehensive user authentication system, including registration, login, logout, and profile management.",
                        "Enable CRUD (Create, Read, Update, Delete) operations for blog posts.",
                        "Allow authenticated users to manage their content dynamically.",
                        "Implement a comment system to enhance interactivity, allowing users to leave and manage comments on blog posts.",
                        "Add tagging and search functionalities to improve content organization and discoverability.",
                    ],
                    "tasks": [
                        {
                            "title": "0. Initial Setup and Project Configuration for a Django Blog",
                            "instructions": (
                                "Set up a new Django project named django_blog and a blog app, and configure the initial Post model.\n\n"
                                "Steps:\n"
                                "- Install Django with pip install django if not already installed.\n"
                                "- Create project: django-admin startproject django_blog.\n"
                                "- cd into django_blog and create app: python manage.py startapp blog.\n"
                                "- Add 'blog' to INSTALLED_APPS in django_blog/settings.py.\n"
                                "- (Optional) Configure DATABASES in settings.py if using PostgreSQL or another DB instead of SQLite.\n"
                                "- In blog/models.py, define Post model with fields:\n"
                                "  * title = models.CharField(max_length=200)\n"
                                "  * content = models.TextField()\n"
                                "  * published_date = models.DateTimeField(auto_now_add=True)\n"
                                "  * author = models.ForeignKey(User, on_delete=models.CASCADE)\n"
                                "- Run: python manage.py makemigrations blog; python manage.py migrate.\n"
                                "- Set up static files and templates directories inside the blog app; configure STATIC_URL, TEMPLATES, and STATICFILES_DIRS as needed.\n"
                                "- Place provided HTML/CSS/JS into the appropriate static and template directories.\n"
                                "- Run: python manage.py runserver and verify http://127.0.0.1:8000/ loads.\n"
                            ),
                            "order": 0,
                            "is_mandatory": True,
                            "checkers": [
                                "Checks if blog app is installed (app created)",
                                "Checks if 'blog' app is added to INSTALLED_APPS in django_blog/settings.py",
                                "Checks for implementation of Post model in blog/models.py",
                                "Checks for database configuration and migrations applied",
                            ],
                        },
                        {
                            "title": "1. Implementing the Blog's User Authentication System",
                            "instructions": (
                                "Add user authentication to django_blog: registration, login, logout, and profile management.\n\n"
                                "Steps:\n"
                                "- Use Django's built-in auth views/forms for login and logout.\n"
                                "- Create custom registration and profile views, extending UserCreationForm to include email (and optionally other fields).\n"
                                "- Create templates for:\n"
                                "  * login\n"
                                "  * registration\n"
                                "  * logout\n"
                                "  * user profile (view/edit)\n"
                                "- Configure URLs in blog/urls.py for /login, /logout, /register, and /profile.\n"
                                "- Implement profile management to allow authenticated users to view and update their details (e.g. email, profile picture, bio if added).\n"
                                "- Ensure all forms use {% csrf_token %} and rely on Django's password hashing.\n"
                                "- Document how the authentication system works and how to test each feature.\n"
                            ),
                            "order": 1,
                            "is_mandatory": True,
                            "checkers": [
                                "Checks for implementation of authentication views (login, logout, register, profile)",
                                "Checks for templates for login, registration, logout, and profile pages",
                                "Checks for URL patterns in blog/urls.py for /login, /logout, /register, and /profile",
                                "Checks that CSRF tokens are used in authentication forms",
                                "Checks for documentation of the authentication system",
                            ],
                        },
                        {
                            "title": "2. Creating Blog Post Management Features",
                            "instructions": (
                                "Implement full CRUD for the Post model using class-based views, forms, and templates.\n\n"
                                "Steps:\n"
                                "- Use Django's class-based views to implement:\n"
                                "  * ListView: list all posts\n"
                                "  * DetailView: show a single post\n"
                                "  * CreateView: allow authenticated users to create posts\n"
                                "  * UpdateView: allow authors to edit their posts\n"
                                "  * DeleteView: allow authors to delete their posts\n"
                                "- Create a PostForm (ModelForm) to handle creation/updating of posts; author should be set to the logged-in user.\n"
                                "- Create templates for:\n"
                                "  * Listing posts (titles + snippet)\n"
                                "  * Viewing a single post\n"
                                "  * Creating a post\n"
                                "  * Editing a post\n"
                                "  * Deleting a post\n"
                                "- Configure URLs in blog/urls.py:\n"
                                "  * /posts/ (list)\n"
                                "  * /posts/new/\n"
                                "  * /posts/<int:pk>/\n"
                                "  * /posts/<int:pk>/edit/\n"
                                "  * /posts/<int:pk>/delete/\n"
                                "- Use LoginRequiredMixin so only authenticated users can create posts.\n"
                                "- Use UserPassesTestMixin (or equivalent logic) to ensure only the author can edit/delete their posts.\n"
                                "- Test navigation and permissions thoroughly.\n"
                            ),
                            "order": 2,
                            "is_mandatory": True,
                            "checkers": [
                                "Checks for implementation of CRUD operations for Post using class-based views",
                                "Checks for updated URLs for listing, viewing, creating, editing, and deleting blog posts",
                                "Checks for new templates for listing, viewing, creating, editing, and deleting blog posts",
                                "Checks for use of LoginRequiredMixin and UserPassesTestMixin to ensure only authors can edit or delete posts",
                            ],
                        },
                        {
                            "title": "3. Adding Comment Functionality to Blog Posts",
                            "instructions": (
                                "Add a Comment system to posts, including model, forms, views, templates, and URLs.\n\n"
                                "Steps:\n"
                                "- In blog/models.py, define Comment model with fields:\n"
                                "  * post (ForeignKey to Post)\n"
                                "  * author (ForeignKey to User)\n"
                                "  * content (TextField)\n"
                                "  * created_at (DateTimeField)\n"
                                "  * updated_at (DateTimeField)\n"
                                "- Run migrations.\n"
                                "- Create a CommentForm (ModelForm) to create/update comments.\n"
                                "- Implement views for comment CRUD:\n"
                                "  * Display comments under each post (often integrated into the post detail view).\n"
                                "  * Allow authenticated users to add comments on the post detail page.\n"
                                "  * Allow comment authors to edit and delete their own comments.\n"
                                "- Create templates (or integrate into post detail template) for displaying, adding, editing, and deleting comments.\n"
                                "- Configure URLs, e.g. /posts/<int:post_id>/comments/new/, /comments/<int:pk>/edit/, /comments/<int:pk>/delete/.\n"
                                "- Ensure only the comment author can edit/delete their comment.\n"
                            ),
                            "order": 3,
                            "is_mandatory": True,
                            "checkers": [
                                "Checks for implementation of Comment model",
                                "Checks for CRUD operations for Comment (create, list under a post, edit, delete)",
                                "Checks for CommentForm (ModelForm) for comment creation and updating",
                                "Checks for logically structured URLs for comment actions (e.g., /posts/<int:post_id>/comments/new/)",
                            ],
                        },
                        {
                            "title": "4. Implementing Advanced Features: Tagging and Search Functionality",
                            "instructions": (
                                "Add tagging and search features to organize and discover blog posts.\n\n"
                                "Steps:\n"
                                "- Tagging:\n"
                                "  * Implement a Tag model with a name field, or use a package like django-taggit.\n"
                                "  * Create a many-to-many relationship between Tag and Post.\n"
                                "  * Run migrations.\n"
                                "- Forms:\n"
                                "  * Update PostForm to allow adding/editing tags.\n"
                                "  * Support creating new tags from the form.\n"
                                "- Search:\n"
                                "  * Implement a search view that filters posts by title, content, or tags (using Q objects).\n"
                                "  * Add a search bar in templates and a search results page.\n"
                                "- Templates & URLs:\n"
                                "  * Display associated tags on post templates.\n"
                                "  * Each tag should link to a page showing posts with that tag (e.g., /tags/<tag_name>/).\n"
                                "  * Add URL patterns for tag-filtered views and search results (e.g., /search/).\n"
                                "- Test tagging and search thoroughly, and document how to use them.\n"
                            ),
                            "order": 4,
                            "is_mandatory": True,
                            "checkers": [
                                "Checks for integrating tagging functionality (Tag model or equivalent) with Post",
                                "Checks for modifications to Post creation/update forms to include tags",
                                "Checks for implementation of search functionality using title/content/tags",
                                "Checks for URL configuration for viewing posts by tag and for search results",
                            ],
                        },
                    ],
                }, 
            ],
        },

         {
            "name": "API",
            "slug": "api",
            "description": "Building RESTful APIs with Django REST Framework.",
            "order": 4,
            "topics": [
                {
                    "title": "Building APIs with Django REST Framework",
                    "slug": "building-apis-with-drf",
                    "description": (
                        "Set up a Django project with Django REST Framework, build basic API endpoints, "
                        "implement CRUD with ViewSets and routers, and secure APIs with authentication and permissions."
                    ),
                    "order": 1,
                    "objectives": [
                        "Create a new Django project and configure it to use Django REST Framework.",
                        "Set up a basic environment for API development, including creating models and running migrations.",
                        "Develop a simple API endpoint to retrieve data using serializers and views in DRF.",
                        "Understand the core components of DRF, including serializers and generic views.",
                        "Use DRF’s ViewSets and Routers to simplify the implementation of CRUD operations.",
                        "Manage standard database operations through RESTful APIs effectively.",
                        "Secure API endpoints by implementing authentication schemes and permission settings.",
                        "Ensure only authorized users can access and modify data through the API.",
                    ],
                    "tasks": [
                        {
                            "title": "0. Setting Up a New Django Project with Django REST Framework",
                            "instructions": (
                                "Create a new Django project dedicated to API development and configure Django REST Framework.\n\n"
                                "Steps:\n"
                                "- If needed, install Django: pip install django.\n"
                                "- Create a new project named api_project: django-admin startproject api_project.\n"
                                "- Install DRF: pip install djangorestframework.\n"
                                "- In api_project/settings.py, add 'rest_framework' to INSTALLED_APPS.\n"
                                "- From the api_project directory, create an app named api: python manage.py startapp api.\n"
                                "- Add 'api' to INSTALLED_APPS.\n"
                                "- In api/models.py, define a Book model with fields title (CharField) and author (CharField).\n"
                                "- Run migrations: python manage.py makemigrations; python manage.py migrate.\n"
                                "- Start the dev server: python manage.py runserver and confirm the site loads on http://127.0.0.1:8000/.\n"
                            ),
                            "order": 0,
                            "is_mandatory": True,
                            "checkers": [
                                "Checks if 'api' and 'rest_framework' are added in INSTALLED_APPS",
                                "Checks for the Book model implementation in api/models.py",
                                "Checks for the installation and registration of the 'api' application",
                            ],
                        },
                        {
                            "title": "1. Building Your First API Endpoint with Django REST Framework",
                            "instructions": (
                                "Create a simple API endpoint to list all Book instances using DRF serializers and generic views.\n\n"
                                "Steps:\n"
                                "- In api/serializers.py, define BookSerializer extending serializers.ModelSerializer including all Book fields.\n"
                                "- In api/views.py, define BookList view extending generics.ListAPIView:\n"
                                "  * queryset = Book.objects.all()\n"
                                "  * serializer_class = BookSerializer\n"
                                "- In api/urls.py, create a URL pattern mapping 'books/' to BookList.as_view(), named 'book-list'.\n"
                                "- In api_project/urls.py, include the api app URLs with path('api/', include('api.urls')).\n"
                                "- Test the endpoint at /api/books/ and ensure it returns JSON list of books.\n"
                            ),
                            "order": 1,
                            "is_mandatory": True,
                            "checkers": [
                                "Checks that api/serializers.py file exists",
                                "Checks for definition of BookSerializer extending serializers.ModelSerializer with all Book fields",
                                "Checks that BookList view in api/views.py extends generics.ListAPIView",
                                "Checks that api/urls.py defines a URL pattern routing to BookList",
                                "Checks that path() is used to map 'books/' to the view",
                            ],
                        },
                        {
                            "title": "2. Implementing CRUD Operations with ViewSets and Routers in DRF",
                            "instructions": (
                                "Replace or extend the simple list view with a ViewSet to provide full CRUD operations for Book.\n\n"
                                "Steps:\n"
                                "- In api/views.py, add a BookViewSet class extending viewsets.ModelViewSet:\n"
                                "  * queryset = Book.objects.all()\n"
                                "  * serializer_class = BookSerializer\n"
                                "- In api/urls.py, import DefaultRouter from rest_framework.routers.\n"
                                "- Create a router instance and register the BookViewSet with:\n"
                                "  router.register(r'books_all', BookViewSet, basename='book_all')\n"
                                "- Include router.urls in urlpatterns, alongside the existing 'books/' path:\n"
                                "  urlpatterns = [\n"
                                "      path('books/', BookList.as_view(), name='book-list'),\n"
                                "      path('', include(router.urls)),\n"
                                "  ]\n"
                                "- Test CRUD endpoints (GET, POST, PUT, DELETE) using /api/books_all/ and /api/books_all/<id>/.\n"
                            ),
                            "order": 2,
                            "is_mandatory": True,
                            "checkers": [
                                "Checks that api/views.py defines BookViewSet extending viewsets.ModelViewSet",
                                "Checks that BookViewSet is configured to handle CRUD operations (queryset and serializer_class)",
                                "Checks that api/urls.py imports DefaultRouter and registers BookViewSet",
                                "Checks that router URLs are included in urlpatterns",
                            ],
                        },
                        {
                            "title": "3. Implementing Authentication and Permissions in Django REST Framework",
                            "instructions": (
                                "Secure API endpoints using token authentication and DRF permission classes.\n\n"
                                "Steps:\n"
                                "- In api_project/settings.py, add 'rest_framework.authtoken' to INSTALLED_APPS.\n"
                                "- Run python manage.py migrate to create token tables.\n"
                                "- In REST_FRAMEWORK settings, include TokenAuthentication in DEFAULT_AUTHENTICATION_CLASSES.\n"
                                "- Configure a token retrieval endpoint using DRF's built-in view obtain_auth_token "
                                "(or equivalent):\n"
                                "  * e.g. path('api/token/', obtain_auth_token, name='api-token') in urls.\n"
                                "- In BookViewSet (and/or other viewsets), set permission_classes to include IsAuthenticated "
                                "or other appropriate permission classes from rest_framework.permissions.\n"
                                "- Test API calls with and without authentication tokens using a tool like Postman.\n"
                            ),
                            "order": 3,
                            "is_mandatory": True,
                            "checkers": [
                                "Checks that 'rest_framework.authtoken' is added to INSTALLED_APPS in settings.py",
                                "Checks that DEFAULT_AUTHENTICATION_CLASSES in REST_FRAMEWORK includes TokenAuthentication",
                                "Checks that a token retrieval endpoint is configured using obtain_auth_token",
                                "Checks that viewsets use DRF permission classes (e.g., IsAuthenticated)",
                            ],
                        },
                    ],
                },

                 {
                    "title": "Building and deploying a Django API",
                    "slug": "building-and-deploying-django-api",
                    "description": (
                        "Create a social media-style REST API with Django and Django REST Framework, including "
                        "authentication, posts and comments, likes and notifications, and deployment to production."
                    ),
                    "order": 2,
                    "objectives": [
                        "Create a new Django project and app.",
                        "Configure Django REST Framework and implement a robust user authentication system.",
                        "Develop features that allow users to create, view, update, and delete posts and comments.",
                        "Add features for users to follow other users and view a feed of posts from followed users.",
                        "Enable users to like posts and receive notifications for various interactions within the platform.",
                        "Prepare and deploy the Django REST API to a production environment, ensuring it is secure and scalable.",
                    ],
                    "tasks": [
                        {
                            "title": "0. Project Setup and User Authentication for a Social Media API",
                            "instructions": (
                                "Set up a new Django project and implement user authentication with Django REST Framework.\n\n"
                                "Steps:\n"
                                "- Install Django and DRF: pip install django djangorestframework.\n"
                                "- Create project: django-admin startproject social_media_api.\n"
                                "- cd into social_media_api and create app 'accounts': python manage.py startapp accounts.\n"
                                "- Add 'rest_framework' and 'accounts' to INSTALLED_APPS in settings.py.\n"
                                "- Create a custom user model extending AbstractUser with extra fields:\n"
                                "  * bio (e.g. TextField)\n"
                                "  * profile_picture (ImageField or URLField)\n"
                                "  * followers (ManyToManyField to self, symmetrical=False)\n"
                                "- Add 'rest_framework.authtoken' to INSTALLED_APPS and run migrations to create token tables.\n"
                                "- Implement serializers and views in accounts app for:\n"
                                "  * user registration\n"
                                "  * login\n"
                                "  * token retrieval\n"
                                "- Configure accounts/urls.py with paths for /register, /login, and /profile.\n"
                                "- Ensure registration/login endpoints return a token on success.\n"
                                "- Run python manage.py runserver and test registration/login via Postman, checking tokens are returned.\n"
                            ),
                            "order": 0,
                            "is_mandatory": True,
                            "checkers": [
                                "Checks if 'accounts' is added in settings.py INSTALLED_APPS",
                                "Checks for custom user model extending AbstractUser with bio, profile_picture, and followers (ManyToMany to self, symmetrical=False)",
                                "Checks for implementation of views and serializers in accounts app for registration, login, and token retrieval",
                                "Checks for URL patterns in accounts/urls.py for /register, /login, and /profile",
                            ],
                        },
                        {
                            "title": "1. Implementing Posts and Comments Functionality",
                            "instructions": (
                                "Create posts and comments functionality for the social_media_api project.\n\n"
                                "Steps:\n"
                                "- Create a new app 'posts': python manage.py startapp posts.\n"
                                "- Add 'posts' to INSTALLED_APPS in settings.py.\n"
                                "- In posts/models.py, define:\n"
                                "  * Post model: author (FK to User), title, content, created_at, updated_at.\n"
                                "  * Comment model: post (FK to Post), author (FK to User), content, created_at, updated_at.\n"
                                "- Run: python manage.py makemigrations posts; python manage.py migrate.\n"
                                "- In posts/serializers.py, create serializers for Post and Comment handling relationships correctly.\n"
                                "- In posts/views.py, use DRF viewsets (ModelViewSet) to provide CRUD for Post and Comment.\n"
                                "- Implement permissions so users can only edit/delete their own posts and comments.\n"
                                "- In posts/urls.py, configure routers and URL patterns for Post and Comment viewsets.\n"
                                "- Add pagination to list endpoints and implement filtering/search on Post (e.g. by title/content).\n"
                                "- Test all endpoints (list, create, retrieve, update, delete) and permissions using Postman or tests.\n"
                            ),
                            "order": 1,
                            "is_mandatory": True,
                            "checkers": [
                                "Checks if new app 'posts' is created",
                                "Checks if 'posts' app is added to INSTALLED_APPS",
                                "Checks for implementation of Post and Comment models in posts/models.py",
                                "Checks for addition of posts URLs and router configuration",
                                "Checks that viewsets in posts/views.py provide CRUD and enforce 'only owner can edit/delete'",
                            ],
                        },
                        {
                            "title": "2. Implementing Notifications and Likes Functionality",
                            "instructions": (
                                "Add likes and notifications to make the social_media_api interactive.\n\n"
                                "Steps:\n"
                                "- In posts/models.py, create a Like model with ForeignKey to Post and ForeignKey to User.\n"
                                "- Create a new app 'notifications': python manage.py startapp notifications; add it to INSTALLED_APPS.\n"
                                "- In notifications/models.py, create a Notification model with fields:\n"
                                "  * recipient (FK to User)\n"
                                "  * actor (FK to User)\n"
                                "  * verb (Text or CharField, e.g. 'liked your post')\n"
                                "  * target (GenericForeignKey to related object)\n"
                                "  * timestamp (DateTimeField)\n"
                                "- Implement views in posts/views.py (or separate modules) to handle liking and unliking posts:\n"
                                "  * /posts/<int:pk>/like/\n"
                                "  * /posts/<int:pk>/unlike/\n"
                                "  * Ensure authenticated users can like/unlike and cannot like a post multiple times.\n"
                                "  * Update the Like model accordingly and create Notification entries when appropriate.\n"
                                "- In notifications/views.py, implement an endpoint to fetch notifications for the authenticated user (e.g. /notifications/).\n"
                                "- Configure URL patterns:\n"
                                "  * In posts/urls.py: routes for like/unlike endpoints.\n"
                                "  * In notifications/urls.py: route for listing notifications.\n"
                                "- Test: liking/unliking posts, receiving and listing notifications.\n"
                            ),
                            "order": 2,
                            "is_mandatory": True,
                            "checkers": [
                                "Checks that new 'notifications' app is created",
                                "Checks for Like model in posts app with FK to Post and FK to User",
                                "Checks for Notification model in notifications app with recipient, actor, verb, target, timestamp",
                                "Checks for views to handle liking and unliking posts and generating notifications",
                                "Checks that posts/urls.py defines like/unlike URL patterns, e.g. /posts/<int:pk>/like/ and /posts/<int:pk>/unlike/",
                            ],
                        },
                        {
                            "title": "3. Deploying the Django REST API to Production",
                            "instructions": (
                                "Prepare and deploy the social_media_api project to a production environment.\n\n"
                                "Steps:\n"
                                "- Update settings.py for production:\n"
                                "  * DEBUG = False\n"
                                "  * Configure ALLOWED_HOSTS for your domain/host.\n"
                                "  * Configure production DATABASES settings.\n"
                                "  * Configure security settings, e.g. SECURE_BROWSER_XSS_FILTER, X_FRAME_OPTIONS, "
                                "SECURE_CONTENT_TYPE_NOSNIFF, SECURE_SSL_REDIRECT.\n"
                                "- Ensure database credentials and other secrets use environment variables.\n"
                                "- Configure static and media handling for production:\n"
                                "  * Use collectstatic.\n"
                                "  * Optionally configure cloud storage (e.g. AWS S3) for static/media files.\n"
                                "- Choose a hosting service (Heroku, AWS, DigitalOcean, etc.), set up the environment and WSGI server "
                                "(Gunicorn/uWSGI), and configure reverse proxy (e.g. Nginx) and HTTPS.\n"
                                "- Deploy your code (via Git or the host's deployment method), configure environment variables, and run migrations.\n"
                                "- Set up logging/monitoring and perform final tests on the live URL.\n"
                            ),
                            "order": 3,
                            "is_mandatory": True,
                            "checkers": [
                                "Checks that settings.py is adjusted for production (DEBUG=False, ALLOWED_HOSTS, production DATABASES)",
                                "Checks that security settings like SECURE_BROWSER_XSS_FILTER, X_FRAME_OPTIONS, SECURE_CONTENT_TYPE_NOSNIFF, and SECURE_SSL_REDIRECT are configured",
                                "Checks that database credentials are set up correctly via environment or secure config",
                                "Checks that static/media handling for production (collectstatic, external storage) is configured",
                            ],
                        },
                    ],
                },
            ],
        },

          {
            "name": "Capstone Projects",
            "slug": "capstone-projects",
            "description": "Standalone backend capstone projects that combine all topics.",
            "order": 5,
            "topics": [
                {
                    "title": "BE Capstone Project Ideas",
                    "slug": "be-capstone-project-ideas",
                    "description": (
                        "A collection of backend API capstone ideas plus design and review guidelines. "
                        "You are expected to design and implement ALL of these projects over time."
                    ),
                    "order": 1,
                    "objectives": [],
                    "tasks": [
                        {
                            "title": "0. Capstone Overview & Review Criteria",
                            "instructions": (
                                "This task describes how your final project(s) will be reviewed.\n\n"
                                "Review criteria include:\n"
                                "1) Originality:\n"
                                "- Did you come up with your own idea instead of directly using provided examples?\n"
                                "- This encourages creativity and helps you build something you’ll be proud of.\n\n"
                                "2) Commit History:\n"
                                "- Are commits descriptive and meaningful (e.g., 'feat: add user authentication' instead of "
                                "'update file')?\n"
                                "- Is there clear commit history showing progress over time?\n"
                                "- Why do you only have a few commits for a project you worked on for weeks?\n\n"
                                "3) Features & API Functionality:\n"
                                "- Are your endpoints well-structured and following RESTful conventions?\n"
                                "- Are all CRUD operations implemented where needed?\n"
                                "- Are there proper status codes for different responses (200, 201, 400, 401, 403, 500, etc.)?\n\n"
                                "4) API Documentation:\n"
                                "- Is there clear API documentation?\n"
                                "- Does it list endpoints (GET, POST, PUT, DELETE) and expected request/response structures?\n\n"
                                "5) Code Quality & Best Practices:\n"
                                "- Is the code clean, modular, and well-structured?\n\n"
                                "6) Git Usage & Version Control:\n"
                                "- Are commits incremental and meaningful, not one huge commit?\n\n"
                                "7) Database Design & Performance:\n"
                                "- Is the database well-structured with proper relationships?\n"
                                "- Are ForeignKey, OneToOneField, ManyToManyField used appropriately?\n\n"
                                "8) Error Handling & Logging:\n"
                                "- Are custom error responses implemented (e.g., 400 Bad Request, 403 Forbidden, 404 Not Found)?\n"
                                "- Does the API handle common DRF/Django exceptions (ValidationError, PermissionDenied, "
                                "ObjectDoesNotExist)?\n"
                                "- Is there a logging system for tracking errors?\n\n"
                                "Use this task as a checklist when building each capstone API."
                            ),
                            "order": 0,
                            "is_mandatory": True,
                            "checkers": []
                        },
                        {
                            "title": "1. Design Phase: ERD and API Endpoints",
                            "instructions": (
                                "In this phase, you design your backend before coding. Do this once, then reuse/refine it "
                                "as you build each capstone.\n\n"
                                "1) Design Your Database Schema (ERD):\n"
                                "- Identify main entities (e.g., Users, Tasks, Orders, Products, Posts, Comments).\n"
                                "- Define relationships (One-to-Many, Many-to-Many, One-to-One).\n"
                                "- Choose appropriate data types and constraints (primary keys, foreign keys, indexes).\n\n"
                                "Deliverable:\n"
                                "- Use a tool like Miro, draw.io, dbdiagram.io to create your ERD.\n"
                                "- Add a screenshot of the ERD to a Google Document.\n\n"
                                "2) List Your API Endpoints:\n"
                                "- Define core API routes.\n"
                                "- For each route, specify the HTTP methods (GET, POST, PUT, DELETE).\n"
                                "- Describe what each endpoint does and what data it handles.\n"
                                "- Consider authentication and authorization where necessary.\n\n"
                                "Deliverable:\n"
                                "- In the same Google Document, list all planned API endpoints.\n\n"
                                "Final Deliverable for this phase:\n"
                                "- A Google Document containing:\n"
                                "  * A screenshot of your ERD.\n"
                                "  * A list of API endpoints you plan to implement.\n"
                                "- Upload the Google Doc link (publicly accessible) for review.\n"
                                "These will serve as your blueprint for the implementation phase."
                            ),
                            "order": 1,
                            "is_mandatory": True,
                            "checkers": []
                        },
                        {
                            "title": "2. Library Management System API",
                            "instructions": (
                                "Description: Create an API to manage a library system where users can check out and return "
                                "books, and view available books.\n\n"
                                "Requirements:\n"
                                "- CRUD operations for books and users.\n"
                                "- Endpoint for checking out and returning books.\n"
                                "- Use Django ORM for database interactions.\n"
                                "- Deploy the API on Heroku or PythonAnywhere."
                            ),
                            "order": 2,
                            "is_mandatory": True,
                            "checkers": []
                        },
                        {
                            "title": "3. Task Management API",
                            "instructions": (
                                "Description: Build an API to manage tasks where users can create, update, and delete tasks, "
                                "and mark tasks as complete or incomplete.\n\n"
                                "Requirements:\n"
                                "- CRUD operations for tasks and users.\n"
                                "- Endpoint for marking tasks as complete or incomplete.\n"
                                "- Use Django ORM for database interactions.\n"
                                "- Deploy the API on Heroku or PythonAnywhere."
                            ),
                            "order": 3,
                            "is_mandatory": True,
                            "checkers": []
                        },
                        {
                            "title": "4. E-commerce Product API",
                            "instructions": (
                                "Description: Develop an API for managing an e-commerce platform’s products, where users can "
                                "add, update, and delete products, and view product details.\n\n"
                                "Requirements:\n"
                                "- CRUD operations for products and users.\n"
                                "- Endpoint for searching products by name or category.\n"
                                "- Use Django ORM for database interactions.\n"
                                "- Deploy the API on Heroku or PythonAnywhere."
                            ),
                            "order": 4,
                            "is_mandatory": True,
                            "checkers": []
                        },
                        {
                            "title": "5. Movie Review API",
                            "instructions": (
                                "Description: Create an API to manage movie reviews where users can add, update, and delete "
                                "reviews, and view reviews for a specific movie.\n\n"
                                "Requirements:\n"
                                "- CRUD operations for reviews and users.\n"
                                "- Endpoint for viewing reviews by movie.\n"
                                "- Use Django ORM for database interactions.\n"
                                "- Deploy the API on Heroku or PythonAnywhere."
                            ),
                            "order": 5,
                            "is_mandatory": True,
                            "checkers": []
                        },
                        {
                            "title": "6. Event Management API",
                            "instructions": (
                                "Description: Build an API to manage events where users can create, update, and delete events, "
                                "and view upcoming events.\n\n"
                                "Requirements:\n"
                                "- CRUD operations for events and users.\n"
                                "- Endpoint for viewing upcoming events.\n"
                                "- Use Django ORM for database interactions.\n"
                                "- Deploy the API on Heroku or PythonAnywhere."
                            ),
                            "order": 6,
                            "is_mandatory": True,
                            "checkers": []
                        },
                        {
                            "title": "7. Blogging Platform API",
                            "instructions": (
                                "Description: Develop an API for a blogging platform where users can create, update, and "
                                "delete blog posts, and view posts by category or author.\n\n"
                                "Requirements:\n"
                                "- CRUD operations for blog posts and users.\n"
                                "- Endpoint for viewing posts by category or author.\n"
                                "- Use Django ORM for database interactions.\n"
                                "- Deploy the API on Heroku or PythonAnywhere."
                            ),
                            "order": 7,
                            "is_mandatory": True,
                            "checkers": []
                        },
                        {
                            "title": "8. Fitness Tracker API",
                            "instructions": (
                                "Description: Create an API to manage fitness activities where users can log, update, and "
                                "delete activities, and view activity history.\n\n"
                                "Requirements:\n"
                                "- CRUD operations for activities and users.\n"
                                "- Endpoint for viewing activity history.\n"
                                "- Use Django ORM for database interactions.\n"
                                "- Deploy the API on Heroku or PythonAnywhere."
                            ),
                            "order": 8,
                            "is_mandatory": True,
                            "checkers": []
                        },
                        {
                            "title": "9. Recipe Management API",
                            "instructions": (
                                "Description: Build an API to manage recipes where users can add, update, and delete recipes, "
                                "and view recipes by category or ingredient.\n\n"
                                "Requirements:\n"
                                "- CRUD operations for recipes and users.\n"
                                "- Endpoint for viewing recipes by category or ingredient.\n"
                                "- Use Django ORM for database interactions.\n"
                                "- Deploy the API on Heroku or PythonAnywhere."
                            ),
                            "order": 9,
                            "is_mandatory": True,
                            "checkers": []
                        },
                        {
                            "title": "10. Inventory Management API",
                            "instructions": (
                                "Description: Develop an API to manage inventory for a store where users can add, update, and "
                                "delete inventory items, and view inventory levels.\n\n"
                                "Requirements:\n"
                                "- CRUD operations for inventory items and users.\n"
                                "- Endpoint for viewing inventory levels.\n"
                                "- Use Django ORM for database interactions.\n"
                                "- Deploy the API on Heroku or PythonAnywhere."
                            ),
                            "order": 10,
                            "is_mandatory": True,
                            "checkers": []
                        },
                        {
                            "title": "11. Social Media API",
                            "instructions": (
                                "Description: Create an API for a social media platform where users can create, update, and "
                                "delete posts, follow other users, and view a feed of posts.\n\n"
                                "Requirements:\n"
                                "- CRUD operations for posts and users.\n"
                                "- Endpoint for following users and viewing a feed of posts.\n"
                                "- Use Django ORM for database interactions.\n"
                                "- Deploy the API on Heroku or PythonAnywhere."
                            ),
                            "order": 11,
                            "is_mandatory": True,
                            "checkers": []
                        },
                    ],
                },
            ],
        },
    ]

}