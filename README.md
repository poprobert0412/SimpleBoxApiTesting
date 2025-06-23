# 📦 SimpleBoxApiTesting

This project is a simple framework for **API testing** using Python and `requests`. It targets the Box REST API or similar RESTful APIs for learning and testing purposes.

---

## 🔧 Tech Stack

- Python 3.x
- `requests` – HTTP client for Python
- `pytest` – test runner (optional but recommended)
- `json` – for handling API responses

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/poprobert0412/SimpleBoxApiTesting.git
cd SimpleBoxApiTesting
````

### 2. Install dependencies

```bash
pip install requests
```

If you use `pytest`:

```bash
pip install pytest
```

---

## ▶️ Run the Tests

You can run the script manually:

```bash
python box_api_test.py
```

Or, if using pytest:

```bash
pytest box_api_test.py
```

---

## 📡 What It Does

* Sends GET/POST/PUT/DELETE requests to specified API endpoints
* Validates HTTP status codes
* Parses and prints response data
* Useful for learning, debugging, and practicing REST API testing

---

## 🧪 Example Test (in code)

```python
import requests

def test_get_file_metadata():
    url = "https://api.box.com/2.0/files/{file_id}"
    headers = {"Authorization": "Bearer YOUR_ACCESS_TOKEN"}

    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    print(response.json())
```

> Replace `YOUR_ACCESS_TOKEN` and `{file_id}` with valid values for testing.

---

## 🧠 Notes

* Make sure your API token (if needed) is valid.
* Handle rate limits or errors gracefully in production scripts.
* This is a minimal project for learning or extension.

---

## 👤 Author

**Pop Robert**
GitHub: [@poprobert0412](https://github.com/poprobert0412)
