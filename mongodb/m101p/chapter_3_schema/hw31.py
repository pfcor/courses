import pymongo
import pprint

db = pymongo.MongoClient()['school']

updates = []
for student in db.students.find({}, {'scores': 1}):
    scores = sorted(student['scores'], key=lambda d: d['score'])
    for i, score in enumerate(scores):
        if score['type'] == 'homework':
            del scores[i]
            break
    updates.append(pymongo.UpdateOne({'_id': student['_id']},
                                     {'$set': {'scores': scores}}))
db.students.bulk_write(updates)    
