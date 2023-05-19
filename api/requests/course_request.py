from pydantic import BaseModel, Field
from bson import ObjectId


class CoursePath(BaseModel):
    course_id: str = Field(description='course id')


class CourseBody(BaseModel):
    name: str = Field(min_length=5, max_length=100, description='course name')
    description: str = Field(min_length=5, max_length=180, description='course description')