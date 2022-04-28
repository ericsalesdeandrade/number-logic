import pytest
from number_logic.src.number_logic import NumberLogic


@pytest.fixture(scope="session")
def number_logic():
    """Create NumberLogic object"""
    number_logic = NumberLogic()
    return number_logic
