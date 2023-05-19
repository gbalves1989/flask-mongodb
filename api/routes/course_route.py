from api import app 
from flask_openapi3 import APIBlueprint, Tag
from bson import ObjectId

from api.requests.course_request import CourseBody, CoursePath
from api.responses.course_response import CourseResponse, CourseListResponse, CourseMessage
from api.services.course_service import CourseService


tag: Tag = Tag(name='Courses', description='List of routes')
api_courses: APIBlueprint = APIBlueprint(
    'courses',
    __name__,
    url_prefix='/courses',
    abp_tags=[tag]
)


@api_courses.post(
    '/',
    summary='Create a new course',
    description='Responsible to create and return a new course',
    responses={'201': CourseMessage}
)
async def store(body: CourseBody):
    return CourseService.create_course(body)


@api_courses.get(
    '/',
    summary='Return a list of courses',
    description='Responsible to return a list of courses',
    responses={'200': CourseListResponse}
)
async def index():
    return CourseService.list_courses()


@api_courses.get(
    '/<course_id>',
    summary='Return some course by id',
    description='Responsible to return some course by id',
    responses={
        '200': CourseResponse
    }
)
async def show(path: CoursePath):
    return CourseService.get_course(ObjectId(path.course_id))


@api_courses.put(
    '/<course_id>',
    summary='Update the data course by id',
    description='Responsible to update the data course by id',
    responses={
        '202': CourseMessage
    }
)
async def update(path: CoursePath, body: CourseBody):
    return CourseService.update_course(ObjectId(path.course_id), body)


@api_courses.delete(
    '/<course_id>',
    summary='Remove some course by id',
    description='Responsible to remove some course by id',
    responses={
        '200': CourseMessage,
    }
)
async def delete(path: CoursePath):
    return CourseService.delete_course(ObjectId(path.course_id))


app.register_api(api_courses)
