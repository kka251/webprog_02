from flask import Blueprint, request, render_template, redirect, url_for, abort, jsonify

lab8 = Blueprint ("lab8", __name__)

@lab8.route('/lab8/')
def main():
    return render_template('lab8/index.html')

courses = [
    {"name": "C++", "videos": 3, "price": 3000},
    {"name": "basic", "videos": 30, "price": 0},
    {"name": "C#", "videos": 8}
]

@lab8.route('/lab8/api/courses/', methods=['GET'])
def get_courses():
    return jsonify(courses)

@lab8.route('/lab8/api/courses/<int:course_num>', methods=['GET'])
def get_course(course_num):
    if course_num < 0 or course_num >= len(courses):
        return "Error 404: Course not found", 404
    return courses[course_num]

@lab8.route('/lab8/api/courses/<int:course_num>', methods=['DELETE'])
def del_course(course_num):
    if course_num < 0 or course_num >= len(courses):
        return "Error 404: Course not found", 404
    del courses[course_num]
    return '', 204

@lab8.route('/lab8/api/courses/<int:course_num>', methods=['PUT'])
def put_course(course_num):
    if course_num < 0 or course_num >= len(courses):
        return "Error 404: Course not found", 404
    course =request.get_json()
    courses[course_num] = course
    return courses[course_num]

@lab8.route('/lab8/api/courses/', methods=['POST'])
def add_course():
    course = request.get_json()
    courses.append(course)
    return {"num": len(courses)-1}

