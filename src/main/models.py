from django.db import connection

def get_quote():
    with connection.cursor() as cursor:
        query = "SELECT quote, author FROM quote_table;"
        cursor.execute(query)
        results = cursor.fetchall()
    return results