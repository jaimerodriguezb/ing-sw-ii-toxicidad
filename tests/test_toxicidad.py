import pytest
from modelo.medidor_toxicidad import MedidorToxicidad

@pytest.fixture
def toxicidad_baja():
    return "Persona de mal gusto"

def test_toxicidad_baja_ok(mocker, toxicidad_baja):
    mocker.patch('modelo.medidor_toxicidad.MedidorToxicidad.medir_toxicidad', return_value = 0.2)

    met_tox= MedidorToxicidad()
    toxicidad = met_tox.medir_toxicidad(toxicidad_baja)
    
    assert toxicidad > 0 and toxicidad < 0.5
    
def test_toxicidad_baja_fail(mocker, toxicidad_baja):
    mocker.patch('modelo.medidor_toxicidad.MedidorToxicidad.medir_toxicidad', return_value = 0.7)

    met_tox= MedidorToxicidad()
    toxicidad = met_tox.medir_toxicidad(toxicidad_baja)
    
    assert toxicidad > 0.5
    

