import psycopg2
import config

def test_insert():
    try:
        # config.py 파일 내 db 설정 내용 호출
        conn = psycopg2.connect(**config.db)

        cursor = conn.cursor()
        cursor.execute("insert into pets values('성탄이', '박진영', '개', 'f', now(), null)")

    except Exception as e:
        print(f'error : {e}')
    finally:
        conn and (conn.commit() or conn.close())
        'cursor' in locals() and cursor and cursor.close()


def test_select():
    try:
        # config.py 파일 내 db 설정 내용 호출
        conn = psycopg2.connect(**config.db)

        cursor = conn.cursor()
        cursor.execute("select * from pets")
        records = cursor.fetchall()

        for record in records:
            print(record)

    except Exception as e:
        print(f'error : {e}')
    finally:
        conn and (conn.commit() or conn.close())
        'cursor' in locals() and cursor and cursor.close()

def test_delete():
    try:
        # config.py 파일 내 db 설정 내용 호출
        conn = psycopg2.connect(**config.db)

        cursor = conn.cursor()
        cursor.execute("delete from pets where name = '성탄이'")

    except Exception as e:
        print(f'error : {e}')
    finally:
        conn and (conn.commit() or conn.close())
        'cursor' in locals() and cursor and cursor.close()

def test_update():
    pass

def main():
    test_insert()
    test_select()

    test_delete()
    test_select()

    test_update()
    test_select()


__name__ == '__main__' and main()