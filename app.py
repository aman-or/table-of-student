from flask import Flask, render_template, request
import psycopg2
from psycopg2 import OperationalError
from settings import DB_CONFIG

app = Flask(__name__)


# Настройки подключения к базе данных
def create_connection():
    try:
        # Установка соединение с базой данных
        connection = psycopg2.connect(**DB_CONFIG)
        print("Соединение с базой данных установлено")
        return connection
    except OperationalError as e:
        print(f"Ошибка подключения к базе данных: {e}")
        return None


@app.route('/')
def form():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT group_id, group_name FROM groups")
        groups = cursor.fetchall()
        connection.close()
        return render_template('index.html',
                               groups=[{'group_id': group[0], 'group_name': group[1]} for group in groups])
    else:
        return "Ошибка подключения к базе данных"


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    student = request.form['student']
    group = request.form['group']
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO students (student_name, group_id) VALUES (%s, %s)", (student, group))
        connection.commit()
        cursor.execute("SELECT s.student_name, g.group_name FROM students s JOIN groups g ON s.group_id = g.group_id")
        students = cursor.fetchall()
        connection.close()
        return render_template('students.html', students=students)
    else:
        return "Ошибка подключения к базе данных"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
