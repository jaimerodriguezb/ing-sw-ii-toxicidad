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
    

# Fixtures usando el modelo

@pytest.fixture
def mensaje_no_toxico():
    return "As always, yours is dripping with sarcasm, which as I quoted from Psychology Today to you yesterday is a form of bullying."

@pytest.fixture
def mensaje_medio_toxico():
    return "Okay.....Should we not be investigating Eric Holder for ""Fast and Furious"", Obama/Hillary for Benghazi, The secret meeting of Susan Rice and Bill Clinton, Hillary/Obama selling 20 percent of US uranium to RUSSIA, Releasing five terrorist at gitmo for one traitor.......?"

@pytest.fixture
def mensaje_muy_toxico():
    return "B.S.  Taking a knee disrespects everyone who died fighting under it.  Who do they think watches them and pays for tickets?  It's hard working patriotic people, veterans, cops, firefighters etc.  To take a knee in England disrespected the British people and their traditions.   My remote too will never waste my time watching what is now a political sounding board.  People watched football to get away from this type garbage."


def test_modelo_toxicidad_alta_ok(mocker, mensaje_muy_toxico):
    toxicidad = MedidorToxicidad().medir_toxicidad(mensaje_muy_toxico)

    assert toxicidad > 0.34



# Fixtures PARCIAL

@pytest.fixture
def mensajes():
    return ["As always, yours is dripping with sarcasm, which as I quoted from Psychology Today to you yesterday is a form of bullying.", "Okay.....Should we not be investigating Eric Holder for ""Fast and Furious"", Obama/Hillary for Benghazi, The secret meeting of Susan Rice and Bill Clinton, Hillary/Obama selling 20 percent of US uranium to RUSSIA, Releasing five terrorist at gitmo for one traitor.......?", "B.S.  Taking a knee disrespects everyone who died fighting under it.  Who do they think watches them and pays for tickets?  It's hard working patriotic people, veterans, cops, firefighters etc.  To take a knee in England disrespected the British people and their traditions.   My remote too will never waste my time watching what is now a political sounding board.  People watched football to get away from this type garbage." ]

def test_parcial_mensajes(moker, mensajes):
      mocker.patch('modelo.medidor_toxicidad.MedidorToxicidad.medir_toxicidad_varios', return_value = [0.2, 0.4, 0.7])