from abc import ABC, abstractmethod
from flask import jsonify, Response
from bson import ObjectId

from api.entities.course_entity import CourseEntity


class CourseInterface(ABC):
    @abstractmethod
    def create(entity: CourseEntity) -> None:
        pass
    
    @abstractmethod
    def find_all() -> Response:
        pass
    
    @abstractmethod
    def find_one(course_id: ObjectId) -> Response:
        pass
    
    @abstractmethod
    def update(course_id: ObjectId, entity: CourseEntity) -> None:
        pass
    
    @abstractmethod
    def delete(course_id: ObjectId) -> None:
        pass
    