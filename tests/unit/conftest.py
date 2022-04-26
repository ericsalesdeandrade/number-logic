import pytest
from number_logic.src.number_logic import NumberLogic


@pytest.fixture(scope="session")
def number_logic():
    """Create Write ElasticSearch object for R/W Operations"""
    number_logic = NumberLogic()
    return number_logic
