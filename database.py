import psycopg2
import psycopg2.extras

class database:
    '''
    Mediator Design Pattern
    database class functions as mediator to control all execution function for all tables
    database class rely on one connection from psycogn2
    '''

    def __init__(self):
        self.conn = psycopg2.connect("host=localhost port='5432' dbname='dot' user='xxx' password='xxx'")
        self.cursor = self.conn.cursor()

    def insert_new_user(self, RIN, RCS_id, owned):
        '''
        insert one new student into Student table
        :param RIN: student RIN eg. 6616XXXX
        :param RCS_id: stduent RCS ID, eg. johnl3
        :param owned: the item user owned, eg. iPad
        '''
        insert_command = "INSERT INTO students(rin, rcs_id, owned)" \
                         "VALUES (%s, %s)"

        self.cursor.execute(insert_command, [RIN, RCS_id, owned])
        self.conn.commit()

    def insert_new_item(self, id, description):
        '''
        :param id: the id of item
        :param description: the description of this question
        '''
        insert_command = "INSERT INTO items(id, description)" \
                         "VALUES (%s, %s)"

        self.cursor.execute(insert_command, [id, description])
        self.conn.commit()

    def look_up_items(self, cmd):
        '''
        :param index: the index of question started from 1
        :return timelength, a string of time eg."0:00:05"
        '''
        select_command = "SELECT id FROM items WHERE description LIKE %cmd%"

        self.cursor.execute(select_command, [id, cmd])
        result = self.cursor.fetchall()

        return result[0][0]
