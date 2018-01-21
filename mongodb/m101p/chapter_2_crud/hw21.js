use students
db.grades.find({score: {$gte: 65}}, {_id: 0, student_id: 1}).sort({score: 1}).limit(1)