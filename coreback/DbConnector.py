import pymysql

def connect(host, port, user, password, database):
    return pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database,
        cursorclass=pymysql.cursors.DictCursor,
    )


def execute(connection, sql):
    with connection.cursor() as cursor:
        cursor.execute(sql)
        return cursor.fetchall()


def insert(connection, sql, values):
    with connection.cursor() as cursor:
        cursor.execute(sql, values)
        connection.commit()


def update(connection, sql, values):
    with connection.cursor() as cursor:
        cursor.execute(sql, values)
        connection.commit()


def delete(connection, sql):
    with connection.cursor() as cursor:
        cursor.execute(sql)
        connection.commit()


# def main():
#     connection = connect("localhost", 3306, "root", "password", "test")

#     # 데이터 조회
#     sql = "SELECT * FROM users"
#     users = execute(connection, sql)
#     print(users)

#     # 데이터 삽입
#     sql = "INSERT INTO users (name, age) VALUES ('홍길동', 30)"
#     insert(connection, sql, ("홍길동", 30))

#     # 데이터 수정
#     sql = "UPDATE users SET age = 31 WHERE name = '홍길동'"
#     update(connection, sql, ("홍길동", 31))

#     # 데이터 삭제
#     sql = "DELETE FROM users WHERE name = '홍길동'"
#     delete(connection, sql)

#     connection.close()


# if __name__ == "__main__":
#     main()