from daos.user_dao_mongo import UserDAOmongo
from models.user import User

dao = UserDAOmongo()

def test_user_select():
    user = User(None, 'Test1', 'Test1@example.com')
    dao.insert(user)
    user = User(None, 'Test2', 'Test2@example.com')
    dao.insert(user)
    user = User(None, 'Test3', 'Test3@example.com')
    dao.insert(user)
    user_list = dao.select_all()
    assert len(user_list) >= 3

def test_user_insert():
    user = User(None, 'Margaret Hamilton', 'hamilton@example.com')
    dao.insert(user)
    user_list = dao.select_all()
    emails = [u.email for u in user_list]
    assert user.email in emails

def test_user_update():
    user = User(None, 'Charles Babbage', 'babage@example.com')
    assigned_id = dao.insert(user)

    corrected_email = 'babbage@example.com'
    user.id = assigned_id
    user.email = corrected_email

    dao.update(user)

    user_list = dao.select_all()
    emails = [u.email for u in user_list]
    assert corrected_email in emails

def test_user_delete():
    user = User(None, 'Douglas Engelbart', 'engelbart@example.com')
    assigned_id = dao.insert(user)
    dao.delete(assigned_id)

    user_list = dao.select_all()
    emails = [u.email for u in user_list]
    assert user.email not in emails