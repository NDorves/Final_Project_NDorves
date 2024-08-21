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


def search_by_genre(genre):
    query = """
    select c.name as genre, f.release_year as year, f.title, f.description 
    from film as f
    join film_category as fc
    on f.film_id = fc.film_id
    join category as c
    on  c.category_id = fc.category_id
    where c.name = %s 
    order by genre
    
    limit 10;
    """
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(query, (genre,))
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results


def search_by_year(year):
    query = """ 
    SELECT release_year as year, title, description 
    FROM film 
    WHERE release_year = %s
    ORDER BY year
    LIMIT 10;
    """
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(query, (year,))
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results


def search_by_actor_name1(Actor):
    query = """ 
    SELECT a.first_name AS Actor, a.last_name as name, f.title, f.description 
    FROM actor AS a
    inner join film_actor AS fa ON a.actor_id = fa.actor_id
    right join film AS f ON f.film_id = fa.film_id
    WHERE a.first_name LIKE CONCAT('%', %s, '%')
    order by a.first_name
    LIMIT 10;
    """
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(query, (Actor,))
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results

def search_by_actor_name2(name):
    query = """ 
    SELECT a.first_name AS Actor, a.last_name as name, f.title, f.description 
    FROM actor AS a
    inner join film_actor AS fa ON a.actor_id = fa.actor_id
    right join film AS f ON f.film_id = fa.film_id
    WHERE 
    a.last_name LIKE CONCAT('%', %s, '%')
    order by a.last_name
    LIMIT 10;
    """
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(query, (name,))
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
    connection = get_connection2()
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results
