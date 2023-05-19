from flask import make_response, Response
from bson import ObjectId

from api.entities.course_entity import CourseEntity
from api.repositories.course_repository import CourseRepository
from api.requests.course_request import CourseBody, CoursePath


class CourseService:
    def create_course(request: CourseBody) -> Response:
        course_entity: CourseEntity = CourseEntity(
            name=request.name,
            description=request.description
        )
        
        CourseRepository.create(course_entity)
        return make_response({
            'message': 'Course created with success.'    
        }, 201)
        
    def list_courses() -> Response:
        return CourseRepository.find_all() 
    
    def get_course(course_id: ObjectId) -> Response:
        return CourseRepository.find_one(course_id)  
    
    def update_course(course_id: ObjectId, request: CourseBody) -> Response:
        course_entity: CourseEntity = CourseEntity(
            name=request.name,
            description=request.description
        )
        
        return make_response({
            'message': 'Course updated with success.'    
        }, 202)
    
    def delete_course(course_id: ObjectId) -> Response:
        CourseRepository.delete(course_id)

        return make_response({
            'message': 'Course deleted with success.'    
        }, 200)
        