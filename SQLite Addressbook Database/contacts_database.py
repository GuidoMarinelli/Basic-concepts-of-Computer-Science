#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
import pandas as pd

connection = sqlite3.connect('addressbook.db')


def input_contact():
    """Return a tuple with name, surname, phone number."""
    name = input('Inserire il nome del contatto: ')
    surname = input('Inserire il cognome del contatto: ')
    phone = input('Inserire il numero del contatto: ')
    return (name, surname, phone)


def insert_into_contacts_table(data):
    """Inserts contact into contacts table."""
    cur = connection.cursor()
    cur.execute("""INSERT INTO contacts (first, last, phone)
                VALUES (?, ?, ?)""", data)
    connection.commit()


def display_contacts_table():
    """Prints the contacts table."""
    print(pd.read_sql('SELECT * FROM contacts', connection, index_col=['id']))


def main():
    """Main program."""
    num_of_contacts_to_enter = int(input('Digita il numero di contati da' +
                                         ' inserire: '))

    for c in range(num_of_contacts_to_enter):
        contact = input_contact()
        insert_into_contacts_table(contact)

    # Visualizing of the contacts insert into addressbook.db
    display_contacts_table()

    # Closes the database connection
    connection.close()


if __name__ == '__main__':
    main()
