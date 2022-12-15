import pytest
from rest_framework.test import APIClient
from students.models import Course, Student
from model_bakery import baker
from rest_framework.filters import SearchFilter, BaseFilterBackend
from students.filters import CourseFilter


@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def student():
    return Student.objects.create(name="name test", birth_date='1994-01-21')

@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
       return baker.make(Course, make_m2m=True, *args, **kwargs)
    return factory

@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
       return baker.make(Student, make_m2m=True, *args, **kwargs)
    return factory


@pytest.mark.django_db
def test_get_first_course(client, student_factory, course_factory):
    course = course_factory(_quantity=10)
    # student = student_factory(_quantity=10)
    response = client.get(f'/courses/{course[0].id}/')
    assert response.status_code == 200
    data = response.json()
    count = 0
    for i, m in data.items():
        if i == 'id':
            count += 1
        assert count == 1
        if i == 'name':
            assert m == course[0].name

@pytest.mark.django_db
def test_get_list_course(client, student_factory, course_factory):
    course = course_factory(_quantity=10)
    # student = student_factory(_quantity=10)
    response = client.get('/courses/')
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(course)
    for i, m in enumerate(data):
        assert m['name'] == course[i].name

@pytest.mark.django_db
def test_get_filter_id_course(client, student_factory, course_factory):
    course = course_factory(_quantity=10)
    student = student_factory(_quantity=10)
    response = client.get(f'/courses/?id={course[0].id}')
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["id"] == course[0].id

@pytest.mark.django_db
def test_get_filter_name_course(client, student_factory, course_factory):
    course = course_factory(_quantity=10)
    student = student_factory(_quantity=10)
    response = client.get(f'/courses/?name={course[0].name}')
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["name"] == course[0].name


@pytest.mark.django_db
def test_post_course(client):
    count = Course.objects.count()
    # student = student_factory(_quantity=1)
    response = client.post('/courses/', data={'name': "test name"})
    assert response.status_code == 201
    assert Course.objects.count() == count + 1


@pytest.mark.django_db
def test_patch_course(client, student_factory, course_factory):
    course = course_factory(_quantity=10)
    count = Course.objects.count()
    response = client.patch(f'/courses/{course[0].id}/', {'name': "test name"})
    assert response.status_code == 200
    # data = response.json()
    assert Course.objects.count() == count


@pytest.mark.django_db
def test_delete_course(client, student_factory, course_factory):
    course = course_factory(_quantity=10)
    count = Course.objects.count()
    response = client.delete(f'/courses/{course[0].id}/')
    assert response.status_code == 204
    # data = response.json()
    assert Course.objects.count() == count - 1