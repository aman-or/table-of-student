# Проект создан в качестве PET- проекта с использованием технологий: Docker, Flask, предназначен для записывания студентов в их группы и просмотр, списка всех студентов 


## Инструкции по развертыванию проекта

### Требования

Для развертывания проекта вам нужно:
1. Установленный Docker.
2. Установленный Docker Compose.

### Установка Docker и Docker Compose

1. Перейдите на [официальный сайт Docker](https://docs.docker.com/get-docker/) и следуйте инструкциям для вашей операционной системы, чтобы установить Docker.
2. Перейдите на [официальный сайт Docker Compose](https://docs.docker.com/compose/install/) и следуйте инструкциям для вашей операционной системы, чтобы установить Docker Compose.

### Развертывание проекта

1. Распакуйте архив проекта в удобное место на вашем компьютере.

   ```bash
   git clone https://github.com/aman-or/table-of-student.git
   ```
   
### Перейдите в директорию, куда вы распаковали проект.

   ```bash
    cd /path/to/your/project
   ```
      
### Запустите проект с помощью Docker Compose.

   ```bash
    docker-compose up --build
   ```


### Проверка работы приложения

   ```
   http://localhost:5000
   ```
### Остановка проекта
   
  ```bash
    docker-compose down
   ```
   

