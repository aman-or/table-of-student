CREATE TABLE IF NOT EXISTS groups (
    group_id SERIAL PRIMARY KEY,
    group_name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS students (
    student_id SERIAL PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    group_id INTEGER REFERENCES groups(group_id)
);

INSERT INTO groups (group_name) VALUES ('Group A'), ('Group B'), ('Group C') ON CONFLICT DO NOTHING;
