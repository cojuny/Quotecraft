from django.db import connection

def get_quote():
    with connection.cursor() as cursor:
        query = "SELECT quote, author FROM quote_table;"
        cursor.execute(query)
        results = cursor.fetchall()
    return {'quotes': results}


def insert_quote(quote:str, author:str):
    quote = quote + '.' if not quote.endswith('.') else quote
    author = author.upper()

    with connection.cursor() as cursor:
        query = "INSERT INTO quote_table (quote, author) VALUES ('{}','{}');".format(quote, author)
        cursor.execute(query)