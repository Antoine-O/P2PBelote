import json
import pytest
from app.functions_externe import estegal
# --- Fixture Pytest pour fournir les données ---

def test_basic():
    assert True;

def test_estegal_oui():
    assert estegal(1,1);


def test_estegal_non():
    assert not estegal(0,1);

