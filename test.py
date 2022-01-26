"""
Pytest
"""
from app import app

#hi there
#another one

def test1():
    """
    This function tests that the flask application has a correct response code
    when the application goes live
    """
    response = app.test_client().get("/")
    assert response.status_code == 200

def test2():
    """Dummy docstring"""
    response = app.test_client().get("/edit")
    assert response.status_code == 200

def test3():
    """Dummy docstring"""
    response = app.test_client().get("/edit")
    #test if the string is on the page
    assert b"To Do App" in response.data
    assert b"Todo Title" in response.data
    assert b"Add" in response.data
    #assert b"Project" in response.data