import sqlite3
# conn = sqlite3.connect('PM_Tool.db')
# query = "<SQLite Query goes here>"
# result = conn.execute(query)


class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('PM_Tool.db')
        # self.create_user_table()
        self.create_Requirements_table()

    def create_Requirements_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "Requirements" (
            RequirementName TEXT,
            RequirementSource TEXT,
            DueDate Date);
        """

        self.conn.execute(query)

    # def create_user_table(self):
    #     query = """
    #     CREATE TABLE IF NOT EXISTS "User" (
    #         id INTEGER PRIMARY KEY AUTOINCREMENT,
    #         Name TEXT NOT NULL,
    #         Email TEXT);
    #     """
    #     self.conn.execute(query)


class RequirementsModel:
    TABLENAME = "Requirements"

    def __init__(self):
        self.conn = sqlite3.connect('PM_Tool.db')
        self.conn.row_factory = sqlite3.Row

    def create(self, params):
        print(params)
        query = f'insert into {self.TABLENAME}' \
                f'(RequirementName, RequirementSource, DueDate)' \
                f'values ("{params.get("RequirementName")}", "{params.get("RequirementSource")}", ' \
                f'"{params.get("DueDate")}")'

        result = self.conn.execute(query) 
        return result