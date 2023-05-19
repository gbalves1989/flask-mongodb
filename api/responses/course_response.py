from pydantic import BaseModel, Field


class CourseResponse(BaseModel):
    _id: str = Field(description='course id')
    name: str = Field(description='course name')
    description: str = Field(description='description of course')


class CourseListResponse(BaseModel):
    courses: list[CourseResponse]
    
    
class CourseMessage(BaseModel):
    message: str = Field(description='message of success')
