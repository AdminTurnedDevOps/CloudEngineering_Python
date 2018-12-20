import pymysql
import sys
import traceback
import json

global dbname


def create_mysql_db(*kwargs):
    log = open(logs, 'w')

    try:
        with open(db_name_path) as f:
            json_path = json.load(f)

        for line in json_path[json_config]:
            dbname = (str(line[db_key]))

            db_connect = pymysql.connect(host=mysql_host,
                                         user="{}".format(dbuser),
                                         password="{}".format(dbpassword))
            conn = db_connect.cursor()
            conn.execute('create database {}'.format(dbname))

    except OSError:
        print('Command does not exist')

    except ValueError:
        print('Error: Value not passed in successfully')

    except Exception:
        traceback.print_exc(file=log)


dbuser = sys.argv[1]
dbpassword = sys.argv[2]
logs = sys.argv[3]
db_name_path = sys.argv[4]
json_config = sys.argv[5]
mysql_host = sys.argv[6]
db_key = sys.argv[7]

if __name__ == '__main__':
    create_mysql_db(dbuser, dbpassword, logs, db_name_path, json_config, mysql_host, db_key)
