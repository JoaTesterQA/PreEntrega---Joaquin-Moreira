import pytest

test_files = [
    "test/test_login.py",
    "test/test_inventory.py",
    "test/test_cart.py"
]

pytest_args = test_files + ["--html=report.html", "-v"]

pytest.main(pytest_args)