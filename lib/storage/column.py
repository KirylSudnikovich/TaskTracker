import sqlite3

import lib.conf as conf
from lib.models.column import Column
from lib.storage.project import ProjectStorage
from lib.exception import *


class ColumnStorage:

    @classmethod
    def add_column_to_db(cls, column):
        """
        Add the sent column to the database
        :param column: an instance of the Column type to be added to the database
        :return:
        """
        conn = sqlite3.connect(conf.get_path_to_db())
        c = conn.cursor()
        c.execute("SELECT name FROM columns WHERE project_id==('%s')" % column.project_id)
        data = c.fetchall()
        have = False
        for i in data:
            if i[0] == column.name:
                have = True
        if not have:
            c.execute("INSERT INTO columns (name, desc, project_id) VALUES ('%s', '%s', '%d')" % (column.name,
                                                                                                  column.desc,
                                                                                                  column.project_id))
            conn.commit()
            conn.close()
        else:
            raise ColumnWithThisNameAlreadyExist

    @classmethod
    def save(self, column):
        """
        Saves all instance fields to the database
        :param column: the instance that you want to keep
        :return:
        """
        conn = sqlite3.connect(conf.get_path_to_db())
        c = conn.cursor()
        c.execute(
            "UPDATE columns SET name=('%s'),desc=('%s'),project_id=('%s') WHERE id==('%d')" % (column.name, column.desc,
                                                                                               column.project_id,
                                                                                               column.id))
        conn.commit()
        conn.close()

    @classmethod
    def delete_column_from_db(cls, column):
        """
        Remove the transferred instance from the database
        :param column: the instance you want to delete
        :return:
        """
        conn = sqlite3.connect(conf.get_path_to_db())
        c = conn.cursor()
        c.execute("DELETE FROM columns WHERE name == ('%s') AND project_id==('%s')" % (column.name, column.project_id))
        conn.commit()
        conn.close()

    @classmethod
    def get_column(cls, project_name, name):
        """
        Get an instance of a class with the specified name
        :param project_name: the name of the project that contains the column
        :param name: the name of the column
        :return:
        """
        conn = sqlite3.connect(conf.get_path_to_db())
        c = conn.cursor()
        project = ProjectStorage.get_project(project_name)
        c.execute("SELECT * FROM columns WHERE name==('%s') AND project_id==('%s')" % (name, project.id))
        data = c.fetchone()
        try:
            column = Column(data[1], data[2], data[3], data[0])
            conn.close()
            return column
        except:
            conn.close()
            raise NoColumnWithThisName

    @classmethod
    def get_all_columns(cls, project_name):
        """
        Get a list consisting of all columns included in the project
        :param project_name: the name of the project
        :return:
        """
        cols = []
        conn = sqlite3.connect(conf.get_path_to_db())
        c = conn.cursor()
        project = ProjectStorage.get_project(project_name)
        c.execute("SELECT * FROM columns WHERE project_id==('%s')" % project.id)
        data = c.fetchall()
        for i in data:
            column = Column(i[1], i[2], i[3], i[0])
            cols.append(column)
        return cols

    @classmethod
    def create_table(cls):
        """

        :return:
        """
        path = conf.get_path_to_db()
        conn = sqlite3.connect(path)
        c = conn.cursor()
        c.execute("CREATE TABLE `columns` (`id`	INTEGER PRIMARY KEY AUTOINCREMENT, `name` TEXT, `desc` TEXT, "
                  "`project_id` TEXT)")
        conn.commit()
        conn.close()