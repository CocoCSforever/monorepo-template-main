from jsonapi import YEncoder, YDecoder, dumps, loads
import json

SAMPLE_COMPLEX = complex(5, 8)
SAMPLE_RANGE  = range(1, 8, 4)
SAMPLE_DATA = {
    "Yijia": complex(1, 2),
    "Ma": range(1, 10, 3),
    "6666": True,
}

# test for YEncoder
def test_YEncoder():
    encoder = YEncoder()
    encoded_complex = encoder.encode(SAMPLE_COMPLEX) # return str
    default_complex = encoder.default(SAMPLE_COMPLEX) # return dict

    expected_encoded_complex = "{\"real\": 5.0, \"imag\": 8.0, \"__extended_json_type__\": \"complex\"}"
    expected_default_complex = {'real': 5.0, 'imag': 8.0, '__extended_json_type__': 'complex'}
    name = type(SAMPLE_COMPLEX).__name__
    assert(
        encoded_complex == expected_encoded_complex
        and default_complex == expected_default_complex
        and encoder.__getattribute__(f"encode_{name}") == encoder.encode_complex
    )

# test for YDecoder
def test_YDecoder():
    encoder = YEncoder()
    encoded_complex = encoder.encode(SAMPLE_COMPLEX) # return str

    decoder = YDecoder()
    decoded_complex = decoder.decode(encoded_complex) # return complex

    object_hook_complex = decoder.object_hook(encoder.default(SAMPLE_COMPLEX))
    name = type(SAMPLE_COMPLEX).__name__
    expected_decoded_complex = SAMPLE_COMPLEX

    assert(
        decoded_complex == expected_decoded_complex
        and object_hook_complex == SAMPLE_COMPLEX
        and decoder.__getattribute__(f"decode_{name}") == decoder.decode_complex
    )

# test for encode_{name}()
def test_encode_complex():
    encoded_complex = json.dumps(SAMPLE_COMPLEX, cls=YEncoder) # return str
    expected_encoded_complex = "{\"real\": 5.0, \"imag\": 8.0, \"__extended_json_type__\": \"complex\"}"
    assert(encoded_complex == expected_encoded_complex)

def test_encode_range():
    encoded_range = json.dumps(SAMPLE_RANGE, cls=YEncoder)
    expected_encoded_range = "{\"start\": 1, \"stop\": 8, \"step\": 4, \"__extended_json_type__\": \"range\"}"
    assert(encoded_range == expected_encoded_range)

def test_encode_data():
    encoded_data = json.dumps(SAMPLE_DATA, cls=YEncoder)
    expected_encoded_data = "{\"Yijia\": {\"real\": 1.0, \"imag\": 2.0, \"__extended_json_type__\": \"complex\"}, \"Ma\": {\"start\": 1, \"stop\": 10, \"step\": 3, \"__extended_json_type__\": \"range\"}, \"6666\": true}"
    assert(encoded_data == expected_encoded_data)

# test for decode_{name}()
def test_decode_complex():
    encoded_complex = json.dumps(SAMPLE_COMPLEX, cls=YEncoder)
    decoded_complex = json.loads(encoded_complex, cls=YDecoder)
    expected_decoded_complex = SAMPLE_COMPLEX
    assert(decoded_complex == expected_decoded_complex)

def test_decode_range():
    encoded_range = json.dumps(SAMPLE_RANGE, cls=YEncoder)
    decoded_range = json.loads(encoded_range, cls=YDecoder)
    expected_decoded_range = SAMPLE_RANGE
    assert(decoded_range == expected_decoded_range)

def test_decode_data():
    encoded_data = json.dumps(SAMPLE_DATA, cls=YEncoder)
    decoded_data = json.loads(encoded_data, cls=YDecoder)
    expected_decoded_data = SAMPLE_DATA
    assert(decoded_data == expected_decoded_data)

#  test for dumps
def test_dumps_complex():
    encoded_complex = dumps(SAMPLE_COMPLEX)
    expected_encoded_complex = "{\"real\": 5.0, \"imag\": 8.0, \"__extended_json_type__\": \"complex\"}"
    assert(encoded_complex == expected_encoded_complex)

def test_dumps_range():
    encoded_range = dumps(SAMPLE_RANGE)
    expected_encoded_range = "{\"start\": 1, \"stop\": 8, \"step\": 4, \"__extended_json_type__\": \"range\"}"
    assert(encoded_range == expected_encoded_range)

def test_dumps_data():
    encoded_data = dumps(SAMPLE_DATA)
    expected_encoded_data = "{\"Yijia\": {\"real\": 1.0, \"imag\": 2.0, \"__extended_json_type__\": \"complex\"}, \"Ma\": {\"start\": 1, \"stop\": 10, \"step\": 3, \"__extended_json_type__\": \"range\"}, \"6666\": true}"
    assert(encoded_data == expected_encoded_data)

#  test for loads
def test_loads_complex():
    encoded_complex = dumps(SAMPLE_COMPLEX)
    decoded_complex = loads(encoded_complex)
    expected_decoded_complex = SAMPLE_COMPLEX
    assert(decoded_complex == expected_decoded_complex)

def test_loads_range():
    encoded_range = dumps(SAMPLE_RANGE)
    decoded_range = loads(encoded_range)
    expected_decoded_range = SAMPLE_RANGE
    assert(decoded_range == expected_decoded_range)

def test_loads_data():
    encoded_data = dumps(SAMPLE_DATA)

    decoded_data = loads(encoded_data)
    expected_decoded_data = SAMPLE_DATA
    assert(decoded_data == expected_decoded_data)