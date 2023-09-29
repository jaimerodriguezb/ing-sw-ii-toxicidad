import pytest


@pytest.fixture
def toxicidad_baja():
    return "Persona de mal gusto"

def test_toxicidad_baja(mocker, toxicidad_baja):
    

    met_tox= MedidorToxicidad()
    toxicidad = met_tox.medir_toxicidad(toxicidad_baja)
    
    assert toxicidad > 0 and toxicidad < 0.5
    



