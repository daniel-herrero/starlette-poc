# Create a database instance, and connect to it.
from databases import Database
import asyncio


# database = Database('sqlite:///example.db')


# await database.connect()


# # Create a table.
# query = """CREATE TABLE HighScores (id INTEGER PRIMARY KEY, name VARCHAR(100), score INTEGER)"""
# await database.execute(query=query)
#
# # Insert some data.
# query = "INSERT INTO HighScores(name, score) VALUES (:name, :score)"
# values = [
#     {"name": "Daisy", "score": 92},
#     {"name": "Neil", "score": 87},
#     {"name": "Carol", "score": 43},
# ]
# await database.execute_many(query=query, values=values)

# Run a database query.
# query = "SELECT * FROM HighScores"
# rows = await database.fetch_all(query=query)


async def get_dbconnection(db_url: str):
    database = await Database(db_url)
    return database


async def get_query_results(database, query: str):
    rows = await database.fetch_all(query=query)
    return rows


async def main():
    database = await get_dbconnection('postgresql://taiga:taiga@localhost:5432/taiga')
    query = """SELECT * from users"""
    query_result = await get_query_results(database, query)
    print('Users:', query_result)


loop = asyncio.new_event_loop()
task = loop.create_task(main())
print('Waiting result')
loop.run_until_complete(task)
loop.close()
