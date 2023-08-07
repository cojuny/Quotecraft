from django.db import connection, models

class Quote(models.Model):
    quote = models.CharField(max_length=100)
    author = models.CharField(max_length=50)

def get_quote(sort='latest'):
    if sort not in (('latest', 'oldest', 'random')):
        sort = 'latest'
        
    with connection.cursor() as cursor:
        results = Quote.objects.raw("SELECT * FROM quote_table ORDER BY {};".format(to_order_format(sort)))
    return results


def insert_quote(quote:str, author:str):
    quote = quote + '.' if not quote.endswith('.') else quote
    quote = quote.replace("'", "''")
    quote = quote.replace('"', '""')
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