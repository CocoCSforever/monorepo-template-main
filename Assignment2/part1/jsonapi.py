# extend the json library to support complex and range objects
import json

class YEncoder(json.JSONEncoder):
    def default(self, obj):
        name = type(obj).__name__
        try:
            encoder = getattr(self, f"encode_{name}")
        except AttributeError():
            return super().default(obj)
        else:
            encoded = encoder(obj)
            encoded["__extended_json_type__"] = name
            return encoded
    
    def encode_complex(self, c):
        return {"real": c.real, "imag": c.imag}
    
    def encode_range(self, r):
        return {"start": r.start, "stop": r.stop, "step": r.step}
    
    
class YDecoder(json.JSONDecoder):
    def __init__(self, **kwargs):
        kwargs["object_hook"] = self.object_hook
        super().__init__(**kwargs)
    
    def object_hook(self, obj):
        try:
            # basic value doesn't have key named "__extended_json_type__", and will get KeyError
            name = obj["__extended_json_type__"]
            decoder = getattr(self, f"decode_{name}")
        except (KeyError, AttributeError):
            return obj
        else:
            return decoder(obj)
    
    def decode_complex(self, obj):
        real = obj["real"]
        imag = obj["imag"]
        return complex(real, imag)
    
    def decode_range(self, obj):
        start = obj["start"]
        stop = obj["stop"]
        step = obj["step"]
        return range(start, stop, step)
    

def dumps(obj, cls=YEncoder, *args, **kwargs):
    return json.dumps(obj, cls=cls, *args, **kwargs)

def loads(s, cls=YDecoder, *args, **kwargs):
    return json.loads(s, cls=cls, *args, **kwargs)


# my_data = {
#     "hey": complex(1, 2),
#     "there": range(1, 10, 3),
#     73: False,
# }

# # print("my_data: \n", my_data)

# json_data = dumps(my_data)
# decoded = loads(json_data)

# print("json_data: \n",json_data)
# print("decoded_json_data: \n", decoded)


SAMPLE_COMPLEX = complex(5, 8)
# SAMPLE_COMPLEX = {
#     "Yijia": complex(1, 2),
#     "Ma": range(1, 10, 3),
#     6666: True,
# }
encoded_complex = dumps(SAMPLE_COMPLEX)

print(encoded_complex)