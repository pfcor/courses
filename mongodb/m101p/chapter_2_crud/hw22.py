import pymongo

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.students

docs = db.grades.find({"type": "homework"}).sort([("student_id", pymongo.ASCENDING), ("score", pymongo.ASCENDING)])

std_id = "PLACE_HOLDER"
deleted = 0
for doc in docs:
    if doc['student_id'] != std_id:
        std_id = doc['student_id']
        d = db.grades.delete_one({'_id': doc['_id']})
        deleted += d.deleted_count
print('{} docs deleted'.format(deleted))
