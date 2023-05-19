from flask import Response, json, jsonify
from bson import json_util, ObjectId
 
from api import db
from api.entities.course_entity import CourseEntity
from api.interfaces.course_interface import CourseInterface


class CourseRepository(CourseInterface):
    def create(entity: CourseEntity) -> None:
        db.courses.insert_one({
            'name': entity.name,
            'description': entity.description
        })
    
    def find_all() -> Response:
        courses_db = db.courses.find()
        return json.loads(json_util.dumps([course for course in courses_db]))
    
    def find_one(course_id: ObjectId) -> Response:
        course_db = db.courses.find_one({ '_id': course_id })
        return json.loads(json_util.dumps(course_db))
    
    def update(course_id: ObjectId, entity: CourseEntity) -> None:
        course_db = db.courses.update_one(
            { '_id': course_id },
            { '$set': {
                    'name': entity.name,
                    'description': entity.description
                }
            }
        )
    
    def delete(course_id: ObjectId) -> None:
        db.courses.find_one_and_delete({ '_id': course_id })
    