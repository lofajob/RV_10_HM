#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb

from database_settings import credentials


class Model(object):
    """Class for simple imitation ORM"""
    # Define error messages
    error_message = "An error occurred with database"
    error_empty = "Unable to fecth data. Probably database is empty"

    def __init__(self, *credentials):
        # Open connection
        self.connection = MySQLdb.connect(*credentials)
        self.cursor = self.connection.cursor()

    def create(self):
        """
        Table create method
        """
        self.cursor.execute("DROP TABLE IF EXISTS f_table")

        self._sql = """CREATE TABLE f_table(
                       col1 CHAR(10) NOT NULL,
                       col2 CHAR(20),
                       col3 INT)
                    """
        try:
            self.cursor.execute(self._sql)
            print "Table was successfuly created"
        except:
            print error_message

    def insert(self, attr1, attr2, attr3):
        """
        Upgrade database fields method
        """
        self._sql = "INSERT INTO f_table\
                     VALUES ('%s', '%s', %d)" \
                     % (attr1, attr2, attr3)
        try:
            self.cursor.execute(self._sql)
            self.connection.commit()
            print "Database was successfuly updated"
        except:
            self.connection.rollback
            print error_message

    def read(self, param=None):
        """
        Method for extracting
        """
        self._sql = "SELECT col1, col2, col3 FROM f_table"

        self.cursor.execute(self._sql)

        # Check whether we need to get all rows of data or one
        if param == 'all':
            self.results = self.cursor.fetchall()

            if self.results != ():
                for result in self.results:
                    print result[0],result[1],result[2]
            else:
                print Model.error_empty

        elif param == None:
            self.result = self.cursor.fetchone()
            if self.result != ():
                print self.result[0], self.result[1], self.result[2]
            else:
                print Model.error_empty

    def close(self):
        self.connection.close()


if __name__ == "__main__":
    e = Model(*credentials)
    e.create()
    e.insert('new', 'text', 99)
    #e.read()
    e.read('all')
    e.close()
