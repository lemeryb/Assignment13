# Benjamin Lemery
# 4/30

import sqlite3
from sqlite3 import Error

def create_connection(path):
    conn = None
    try:
        conn = sqlite3.connect(path)
        print("Connection to SQLite DB Successful")
    except Error as e:
        print(f"The error {e} occurred")
    return conn

connection = create_connection("Assignment13.db")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return  result
    except Error as e:
        print(f"The error '{e} occurred.")

create_customers_table = """
CREATE TABLE IF NOT EXISTS Customers(
customer_id INTEGER PRIMARY KEY AUTOINCREMENT, 
first_name TEXT NOT NULL , 
last_name TEXT NOT NULL,
street_address TEXT NOT NULL,
city TEXT NOT NULL,
state TEXT NOT NULL,
zip INTEGER
);
"""
execute_query(connection, create_customers_table)

#drop_customers_table = """
#DROP TABLE Customers
#"""
#execute_query(connection, drop_customers_table)

create_books_table = """
CREATE TABLE IF NOT EXISTS BOOKS (
book_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, 
title TEXT NOT NULL, 
author TEXT NOT NULL,
ISBN INTEGER NOT NULL,
edition TEXT NOT NULL,
price INTEGER, 
publisher TEXT NOT NULL
)
"""
execute_query(connection, create_books_table)

def main_menu():
    main_menu_selection = int(input(""
                                "\nPress 1 for the customers table\n"
                                "Press 2 for the books table\n"
                                "Press 3 to exit: "))

    if main_menu_selection == 1:
        customer_menu_selection = int(input("\nPress 1 to add a new customer\n"
                                            "Press 2 to modify an existing customer\n"
                                            "Press 3 to print a list of all customers\n"
                                            "Press 4 to delete a customer\n"
                                            "Press 5 to return to the main menu: "))
        if customer_menu_selection == 1:
            first_name = str(input("First name:\n"))
            last_name = str(input("Last name:\n"))
            street_address = str(input("Street address:\n"))
            city = str(input("City:\n"))
            state = str(input("State:\n"))
            zip = int(input("Zip code:\n"))
            add_new_customer = f"""
                           INSERT INTO
                             Customers (first_name, last_name, street_address, city, state, zip)
                           VALUES
                             ('{first_name}', '{last_name}', '{street_address}', '{city}', '{state}', '{zip}');
                           """
            execute_query(connection, add_new_customer)
            main_menu()

        elif customer_menu_selection == 2:
            customer_id = int(input("Enter the customer ID that you'd like to update: "))

            change = int(input("\nWhat would you like to update? \n\n"
                               "Press 1 to update the customer's first name.\n"
                               "Press 2 to update the customer's last name\n"
                               "Press 3 to update the customer's street address\n"
                               "Press 4 to update the customer's city\n"
                               "Press 5 to update the customer's state\n"
                               "Press 6 to update the customer's zip code :"))
            if change == 1:
                new_first_name = input("Enter the new first name: ")
                update_customer = f"""
                UPDATE 
                    Customers
                SET 
                     first_name = '{new_first_name}'
                WHERE 
                    customer_id = '{customer_id}'
                """
            elif change == 2:
                new_last_name = input("Enter the new last name: ")
                update_customer = f"""
                UPDATE 
                    Customers
                SET 
                     last_name = '{new_last_name}'
                WHERE 
                    customer_id = '{customer_id}'
                """
            elif change == 3:
                new_street_address = input("Enter the new street address: ")
                update_customer = f"""
                UPDATE 
                    Customers
                SET 
                     street_address = '{new_street_address}'
                WHERE 
                    customer_id = '{customer_id}'
                """
            elif change == 4:
                new_city = input("Enter the new city: ")
                update_customer = f"""
                UPDATE 
                    Customers
                SET 
                     city = '{new_city}'
                WHERE 
                    customer_id = '{customer_id}'
                """
            elif change == 5:
                new_state = input("Enter the new state: ")
                update_customer = f"""
                UPDATE 
                    Customers
                SET 
                     state = '{new_state}'
                WHERE 
                    customer_id = '{customer_id}'
                """
            elif change == 6:
                new_zip = input("Enter the new zip: ")
                update_customer = f"""
                UPDATE 
                    Customers
                SET 
                     zip = '{new_zip}'
                WHERE 
                    customer_id = '{customer_id}'
                """
            execute_query(connection, update_customer)
            main_menu()



        elif customer_menu_selection == 3:
            print("Listing all customers!")
            # Create a query to return data from the users table
            select_customers = "SELECT * FROM Customers"
            customer = execute_read_query(connection, select_customers)
            for customer in customer:
                print(customer)
            main_menu()

        elif customer_menu_selection == 4:
            delete_customer_id = int(input("Customer ID: "))
            delete_customer  = f"DELETE FROM Customers WHERE customer_id = {delete_customer_id}"

            print("Customer: " + str(delete_customer_id) + " has been deleted successfully")
            execute_query(connection, delete_customer)
            main_menu()

        elif customer_menu_selection == 5:
            main_menu()

    elif main_menu_selection == 2:
        book_menu_selection = int(input("Press 1 to add a new book\n"
                                        "Press 2 to modify an existing book\n"
                                        "Press 3 to print a list of all books\n"
                                        "Press 4 to delete a book\n"
                                        "Press 5 to return to main menu: "))

        if book_menu_selection == 1:
            if book_menu_selection == 1:
                title = input("Title:\n")
                author = input("Author:\n")
                ISBN = input("ISBN:\n")
                edition = input("Edition:\n")
                price = str(input("Price:\n"))
                publisher = input("Publisher:\n")
                add_new_book = f"""
                                      INSERT INTO
                                        Books (title, author, ISBN, edition, price, publisher)
                                      VALUES
                                        ('{title}', '{author}', '{ISBN}', '{edition}', '{price}', '{publisher}');
                                      """
                execute_query(connection, add_new_book)
                main_menu()
        elif book_menu_selection == 2:
            book_id = int(input("Enter the book ID that you'd like to update: "))

            change = int(input("\nWhat would you like to update? \n\n"
                               "Press 1 to update the book's title\n"
                               "Press 2 to update the book's author\n"
                               "Press 3 to update the book's ISBN\n"
                               "Press 4 to update the book's edition\n"
                               "Press 5 to update the book's price\n"
                               "Press 6 to update the book's publisher :"))
            if change == 1:
                new_title = input("Enter the new book title: ")
                update_book = f"""
                        UPDATE 
                            Books
                        SET 
                             title = '{new_title}'
                        WHERE 
                            book_id = '{book_id}'
                        """
            elif change == 2:
                new_author = input("Enter the new author: ")
                update_book = f"""
                        UPDATE 
                            Customers
                        SET 
                             last_name = '{new_author}'
                        WHERE 
                            customer_id = '{book_id}'
                        """
            elif change == 3:
                new_ISBN = input("Enter the new ISBN: ")
                update_customer = f"""
                        UPDATE 
                            Books
                        SET 
                             ISBN = '{new_ISBN}'
                        WHERE 
                            book_id = '{book_id}'
                        """
            elif change == 4:
                new_edition = input("Enter the new edition: ")
                update_book = f"""
                        UPDATE 
                            Books
                        SET 
                             edition = '{new_edition}'
                        WHERE 
                            book_id = '{book_id}'
                        """
            elif change == 5:
                new_price = input("Enter the new book's price ")
                update_book = f"""
                        UPDATE 
                            Books
                        SET 
                             price = '{new_price}'
                        WHERE 
                            book_id = '{book_id}'
                        """
            elif change == 6:
                new_publisher = input("Enter the new publisher: ")
                update_book = f"""
                        UPDATE 
                            Books
                        SET 
                             publisher = '{new_publisher}'
                        WHERE 
                            book_id = '{book_id}'
                        """
            execute_query(connection, update_book)
            main_menu()

        elif book_menu_selection == 3:
            print("Listing all books!")
            # Create a query to return data from the users table
            select_books = "SELECT * FROM Books"
            book = execute_read_query(connection, select_books)
            for book in book:
                print(book)
            main_menu()

        elif book_menu_selection == 4:
            delete_book_id = int(input("Book ID: "))
            delete_book = f"DELETE FROM Books WHERE book_id = {delete_book_id}"

            print("Book: " + str(delete_book_id) + " has been deleted successfully")
            execute_query(connection, delete_book)
            main_menu()

        elif book_menu_selection == 5:
            main_menu()

    #elif main_menu_selection == 3:
     #   exit()


main_menu()