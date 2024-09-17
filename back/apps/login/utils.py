import jwt
import time
import psycopg2


def generate_jwt_token():
    unix_time_now = int(time.time())
    token = jwt.encode({'exp':unix_time_now + 60}, 'secret')
    return token


def validate_jwt_token(token):
    decoded_token = jwt.decode(token, 'secret', algorithms=['HS256'], options={'verify_exp':False})
    if decoded_token['exp'] >= int(time.time()):
        print('TIME1', decoded_token['exp'])
        print('TIME2', time.time())
        return True
    return False


conn = psycopg2.connect('dbname=shopdb user=postgres password=123')
cur = conn.cursor()

def check_user_exists_in_db(username, email=None):
    user = cur.execute(f"SELECT * FROM users WHERE username = '{username}'")
    exists = cur.fetchone()
    # email_exists = cur.execute(f"select * from users where email = '{email}'")
    result = {}
    print('USER TYPE', user, type(user))
    print('USER', exists)
    if exists is None:
        return {'exists': False}

    result['exists'] = True
    result['username'] = exists[1]
    result['password'] = exists[2]
    result['message'] = f'User {exists[1]} already registered'
    print('RESULT', result)
    return result
