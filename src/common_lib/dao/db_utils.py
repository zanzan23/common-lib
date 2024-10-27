from typing import List
from sqlalchemy.engine.base import Engine



def upsert_query(engine: Engine, table_name: str, columns: List[str], matching: List[str]) -> str:
    return _upsert_query(engine.dialect.name, table_name, columns, matching)


def _upsert_query(dialect_name: str, table_name: str, columns: List[str], matching: List[str]) -> str:
        columns_clause = ', '.join(columns)
        columns_values_clause = [':' + s for s in columns]
        columns_values_clause = ', '.join(columns_values_clause)
        matching_clause = ', '.join(matching)
        if dialect_name.__contains__('firebird'):
            return 'update or insert into ' + table_name + ' (' + columns_clause + \
                    ') values (' + columns_values_clause + ') matching ( ' + matching_clause + ')'
        
        elif dialect_name.__contains__('sqlite') or dialect_name.__contains__('postgresql'):
            update_set_clause = [s + '=excluded.' + s for s in columns]
            update_set_clause = ', '.join(update_set_clause)
            return 'INSERT INTO ' + table_name + ' ( '+ columns_clause + \
                        ') VALUES ('+ columns_values_clause + ') ON CONFLICT(' + matching_clause +  \
                        ') DO UPDATE SET ' + update_set_clause
        
        else:
            raise ValueError('PORTMON: Dialect not implemented yet')