import pytest
from app import app  # Import your Flask app instance


@pytest.fixture
def client():
    # Put the app into testing mode so exceptions propagate clearly
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_holand_route(client, capsys):
    # 1. Simulate a GET request to /holand
    response = client.get("/holand")

    # 2. Verify the HTTP status code is 200 (OK)
    assert response.status_code == 200

    # 3. Verify the returned response body (decode bytes to string)
    assert response.get_data(as_text=True) == "Hello, Holand!"

    # 4. (Optional) Verify the print output using pytest's built-in capsys fixture
    captured = capsys.readouterr()
    assert "hello Holand" in captured.out