from db import get_connection
from db import get_connection2


def search_by_keyword(keyword):
    query = "SELECT title, description FROM film WHERE title LIKE CONCAT('%', %s, '%') LIMIT 10;"
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(query, (keyword,))
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results


def search_by_genre_and_year(genre, year):
    query = """
    select c.name as genre, f.release_year as year, f.title, f.description 
    from film as f
    join film_category as fc
    on f.film_id = fc.film_id
    join category as c
    on  c.category_id = fc.category_id
    where name = %s and
    release_year = %s
    limit 10;
    """
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(query, (genre, year))
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results


def save_search_query(query):
    insert_query = "INSERT INTO search_queries (query) VALUES (%s);"
    connection = get_connection2()
    cursor = connection.cursor()
    cursor.execute(insert_query, (query,))
    connection.commit()
    cursor.close()
    connection.close()


def get_popular_queries():
    query = "SELECT query, COUNT(*) as count FROM search_queries GROUP BY query ORDER BY count DESC;"
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results
