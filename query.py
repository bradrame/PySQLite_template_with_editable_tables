from database import DatabaseManager
import os
import re

class QueryExecutor:
    def __init__(self, db_path='database.db'):
        self.db_manager = DatabaseManager(db_path)
        self.sql_file_path = 'query.sql'
    
    def read_sql_file(self, file_path=None):
        if file_path is None:
            file_path = self.sql_file_path
        with open(file_path, 'r') as file:
            return file.read()
    
    def clean_sql_content(self, sql_content):
        sql_content = re.sub(r'--.*$', '', sql_content, flags=re.MULTILINE)
        sql_content = re.sub(r'/\*.*?\*/', '', sql_content, flags=re.DOTALL)
        return sql_content.strip()
    
    def split_sql_statements(self, sql_content):
        statements = [stmt.strip() for stmt in sql_content.split(';')]
        return [stmt for stmt in statements if stmt]
    
    def execute_sql_file(self, file_path=None):
        if file_path is None:
            file_path = self.sql_file_path
        sql_content = self.read_sql_file(file_path)
        cleaned_sql = self.clean_sql_content(sql_content)
        statements = self.split_sql_statements(cleaned_sql)
        results = []
        for statement in statements:
            if statement.strip().upper().startswith('SELECT'):
                result = self.db_manager.execute_query(statement)
                results.append(result)
            else:
                self.db_manager.execute_non_query(statement)
        return results
    
    def execute_custom_query(self, query, params=None):
        if query.strip().upper().startswith('SELECT'):
            return self.db_manager.execute_query(query, params)
        else:
            return self.db_manager.execute_non_query(query, params)

def print_table(data):
    if not data:
        return
    headers = list(data[0].keys())
    print(' | '.join(headers))
    print('-' * (len(' | '.join(headers))))
    for row in data:
        values = [str(row[header]) for header in headers]
        print(' | '.join(values))

if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    executor = QueryExecutor()
    results = executor.execute_sql_file()
    for result in results:
        print_table(result)
        print()