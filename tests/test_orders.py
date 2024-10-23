import pytest
from requests_folders.order_requests import submit_an_order, get_an_order, update_an_order, delete_an_order
from requests_folders.generate_token_request import generate_token

@pytest.fixture
def token():
    return generate_token()

def test_get_an_order(token):
    submit_order_response = submit_an_order(1, "Robert", token)
    order_id = submit_order_response.json()["orderId"]
    get_order_response = get_an_order(order_id, token)
    assert get_order_response.status_code == 200
    assert get_order_response.json()["bookId"] == 1
    assert get_order_response.json()["quantity"] == 1
    assert get_order_response.json()["customerName"] == "Robert"

def test_update_an_order(token):
    submit_order_response = submit_an_order(3, "Pop", token)
    order_id = submit_order_response.json()["orderId"]
    update_an_order_response = update_an_order(order_id, token)
    assert update_an_order_response.status_code == 204

def test_submit_an_order(token):
    submit_order_response = submit_an_order(4, "Pop Robert", token)
    assert submit_order_response.status_code == 201
    assert submit_order_response.json()['created'] == True

def test_delete_an_order(token):
    submit_order_response = submit_an_order(4, "Pop Robert", token)
    order_id = submit_order_response.json()['orderId']
    delete_an_order_response = delete_an_order(order_id, token)
    assert delete_an_order_response.status_code == 204

def test_post_an_order_with_unavailable_book(token):
    submit_order_response = submit_an_order(2, "test_invalid", token)
    assert submit_order_response.status_code == 404

def test_delete_an_order_with_unavailable_book(token):
    submit_order_response = submit_an_order(1, "Random Client", token)
    order_id = submit_order_response.json()['orderId']
    delete_an_order(order_id, token)
    delete_order_response = delete_an_order(order_id, token)
    assert delete_order_response.status_code == 404
    assert delete_order_response.json()["error"] == f"No order with id {order_id}."








