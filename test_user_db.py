import pytest
from .user_db import connect_db, create_table, create_user, get_user, update_user_email, delete_user

# Fixture to setup test DB
@pytest.fixture
def db():
    conn = connect_db()
    create_table(conn)
    yield conn
    conn.close()

# Create User
@pytest.mark.parametrize("username, email", [
    ("john", "john@example.com"),
    ("alice", "alice@mail.com"),
])
def test_create_user(db, username, email):
    create_user(db, username, email)
    user = get_user(db, username)
    assert user is not None
    assert user[1] == username
    assert user[2] == email

# Update User Email
def test_update_user_email(db):
    create_user(db, "testuser", "old@mail.com")
    update_user_email(db, "testuser", "new@mail.com")
    user = get_user(db, "testuser")
    assert user[2] == "new@mail.com"

# Delete User
def test_delete_user(db):
    create_user(db, "tempuser", "temp@mail.com")
    delete_user(db, "tempuser")
    user = get_user(db, "tempuser")
    assert user is None
