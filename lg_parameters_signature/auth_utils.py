import base64
import logging

import cryptography.hazmat.backends
import cryptography.hazmat.primitives


import urllib.parse


logger = logging.getLogger(__name__)


def get_parameters_unique_auth_key(params, private_key):
    """
    params: list((param_name, param_value))
    private_key: shared private key between handshaking endpoints
    """
    private_key = str.encode(private_key)

    data_filtered = filter(lambda x: bool(x[1]), params)
    data_sorted = sorted(data_filtered, key=lambda x: x[0])
    data_encoded = str.encode(urllib.parse.urlencode(data_sorted))

    h = cryptography.hazmat.primitives.hmac.HMAC(
        private_key,
        cryptography.hazmat.primitives.hashes.SHA256(),
        backend=cryptography.hazmat.backends.default_backend()
    )
    h.update(data_encoded)
    return base64.b16encode(h.finalize()).decode()


def validate_unique_key(params, private_key, key_for_comparison):
    return get_parameters_unique_auth_key(params, private_key) == key_for_comparison
