from PIL import Image
import pickle


def dumps(filename) -> str:
    """
    Serialize an image to a byte array.
    """
    return pickle.dumps(Image.open(filename))


def loads(pickled_image: bytes) -> str:
    """
    Deserialize an image from a byte array.
    """
    return pickle.loads(pickled_image, encoding="utf-8")
