# JSONAPI

JSONAPI is a Python library that extends the functionalities of the built-in `json` module to support serialization and deserialization of more complex Python objects, such as `complex` numbers and `range` objects.

## Installation

To install JSONAPI, use the following command:

```bash
pip install dist/jsonapi-0.0.1.tar.gz
```

## Usage

Here is how you can use the ExtendedEncoder and ExtendedDecoder classes from the JSONAPI package to work with JSON strings representing complex numbers and range objects:

```python
from jsonapi import ExtendedEncoder, ExtendedDecoder

# Encoding a complex number and a range object to a JSON string
encoder = ExtendedEncoder()
data = {
    'complex_number': complex(1, 2),
    'range_obj': range(0, 10, 2)
}
json_str = encoder.encode(data)
print(json_str)

# Decoding the JSON string back to Python objects
decoder = ExtendedDecoder()
decoded_data = decoder.decode(json_str)
print(decoded_data)
```

## Testing

To run the unit tests, use the following command from the project root directory:

```bash
python -m unittest tests.test_jsonapi
```