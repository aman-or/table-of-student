import os
import dotenv

dotenv.load_dotenv('.env')
DB_PASSWORD = os.environ['DB_PASSWORD']

DB_CONFIG = {
    'database': 'test_db',
    'user': 'postgres',
    'password': DB_PASSWORD,
    'host': 'db',
    'port': '5432'
}