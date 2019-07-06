
from common import *

json_db = db_operators.JsonDb("common/posts_db.json")

for value in json_db.data.values():
    print(value['body'])