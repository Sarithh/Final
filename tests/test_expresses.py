from fastapi.testclient import TestClient
import sys
sys.path.insert(0, '../Final02')
from main import app

client = TestClient(app)
_id = None

def test_hello_msg():
    url = "/hello"
    expected_result = {"msg": "Hello World"}
    actual_result = client.get(url)
    assert actual_result.status_code == 200
    assert actual_result.json() == expected_result

def test_post_insert():
    url = "/"
    actual_result = client.post(
        url,
        json = {
            "weight": "less 10kg",
            "price":"200 bath",
            "region":"ภาคกลาง, ภาคตะวันออก, ภาคตะวันตก ",
            "price1":"240 bath",
            "region2":"ภาคเหนือ, ภาคอีสาน, ภาคใต้ ",

            "weight": " 10kg to 20kg",
            "price":"420 bath",
            "region":"ภาคกลาง, ภาคตะวันออก, ภาคตะวันตก ",
            "price1":"460 bath",
            "region2":"ภาคเหนือ, ภาคอีสาน, ภาคใต้ ",

            "weight": " greater 20kg",
            "price":"500 bath",
            "region":"ทั่วประเทศไทย",
            "price1":"-",
            "region2":"- ",

        }
    )
    expected_result = "less 10kg"
    global _id 
    _id = actual_result.json()[0]['id']
    assert actual_result.status_code == 200
    assert actual_result.json()[0]['weight'] == expected_result


def test_get_by_id():
    url = "/"+_id
    actual_result = client.get(url)
    expected_result = "less 10kg"
    assert actual_result.status_code == 200


def test_delete_by_id():
    url = "/"+_id
    actual_result = client.delete(url)
    assert actual_result.status_code == 200
    assert actual_result.json()['status'] == "ok"
