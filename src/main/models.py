from django.db import connection

def get_quote(sort='latest'):
    if sort not in (('latest', 'oldest', 'random')):
        sort = 'latest'
        
    with connection.cursor() as cursor:
        query = "SELECT quote, author FROM quote_table ORDER BY {};".format(to_order_format(sort))
        cursor.execute(query)
        results = cursor.fetchall()
    return {'quotes': results}


def insert_quote(quote:str, author:str):
    quote = quote + '.' if not quote.endswith('.') else quote
    author = author.upper()

    with connection.cursor() as cursor:
        query = "INSERT INTO quote_table (quote, author) VALUES ('{}','{}');".format(quote, author)
        cursor.execute(query)

def to_order_format(sort):
    switch_dict = {
        'latest': 'id DESC',
        'oldest': 'id ASC',
        'random': 'RAND()'
    }
    return switch_dict.get(sort, 'default')