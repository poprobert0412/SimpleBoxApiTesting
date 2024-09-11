import unittest

from requests_folders.order_requests import submit_an_order, get_an_order, update_an_order, delete_an_order


class TestOrders(unittest.TestCase):
    # bookid can have valid values from 1 to 6 inclusively and has availability(this can be checked with GET list of book request)
    def test_get_an_order(self):
        submit_order_response = submit_an_order(1, "Robert")
        order_id = submit_order_response.json()["orderId"]
        get_order_response = get_an_order(order_id)
        assert get_order_response.status_code == 200
        assert get_order_response.json()["bookId"] == 1
        assert get_order_response.json()["quantity"] == 1
        assert get_order_response.json()["customerName"] == "Robert"

    def test_update_an_order(self):
        submit_order_response = submit_an_order(3, "Pop")
        order_id = submit_order_response.json()["orderId"]
        update_an_order_response = update_an_order(order_id)
        assert update_an_order_response.status_code == 204

    def test_submit_an_order(self):
        submit_order_response = submit_an_order(4, "Pop Robert")
        assert submit_order_response.status_code == 201
        assert submit_order_response.json()['created'] == True

    def test_delete_an_order(self):
        submit_order_response = submit_an_order(4, "Pop Robert")
        order_id = submit_order_response.json()['orderId']
        delete_an_order_response = delete_an_order(order_id)
        assert delete_an_order_response.status_code == 204
