import json
from urllib.request import urlopen
import pymysql

with urlopen("https://gymkhana.iitb.ac.in/~ugacademics/model.json") as response:
    source = response.read()

data = json.loads(source)
#print(data)
#print(json.dumps(data, indent=2))


def validate_string(val):
   if val != None:
        if type(val) is int:
            #for x in val:
            #   print(x)
            return str(val).encode('utf-8')
        else:
            return val


# connect to MySQL
con = pymysql.connect(host = 'localhost',user = 'root',passwd = '',db = 'test')
cursor = con.cursor()


# parse json data to SQL insert
for i, item in enumerate(data):
    username = validate_string(item.get("username", None))
    password = validate_string(item.get("password", None))
    name = validate_string(item.get("name", None))

    cursor.execute("INSERT INTO test (username,  password,   name) VALUES (%s,    %s, %s)", (username,  password,   name))
con.commit()
con.close()
