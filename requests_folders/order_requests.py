import requests

def submit_an_order(book_id, customer_name, token):
    header = {'Authorization': token}
    data = {
        "bookId": book_id,
        "customerName": customer_name
    }
    response = requests.post("https://simple-books-api.glitch.me/orders", headers=header, json=data)
    return response

def update_an_order(order_id, token):
    header = {'Authorization': token}
    data = {
        "customerName": "John"
    }
    response = requests.patch(f"https://simple-books-api.glitch.me/orders/{order_id}", headers=header, json=data)
    return response

def get_an_order(order_id, token):
    header = {'Authorization': token}
    response = requests.get(f"https://simple-books-api.glitch.me/orders/{order_id}", headers=header)
    return response

def delete_an_order(order_id, token):
    header = {'Authorization': token}
    response = requests.delete(f"https://simple-books-api.glitch.me/orders/{order_id}", headers=header)
    return response
