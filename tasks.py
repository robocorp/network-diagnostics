import logging
import requests
from RPA.Robocorp.Vault import Vault
from http.client import HTTPConnection  # py3

import requests
from requests.packages.urllib3.connection import VerifiedHTTPSConnection

SOCK = None

_orig_connect = requests.packages.urllib3.connection.VerifiedHTTPSConnection.connect


def _connect(self):
    global SOCK
    _orig_connect(self)
    SOCK = self.sock


requests.packages.urllib3.connection.VerifiedHTTPSConnection.connect = _connect

# requests.get('https://yahoo.com')


def main():
    req_log = logging.getLogger("requests.packages.urllib3")
    req_log.setLevel(logging.DEBUG)
    req_log.propagate = True

    # logging from urllib3 to console
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    req_log.addHandler(ch)

    # print statements from `http.client.HTTPConnection` to console/stdout
    HTTPConnection.debuglevel = 1

    secrets = Vault().get_secret("ever")
    # print(dir(SOCK))
    # print(dir(SOCK.context))
    # DIR: SOCK
    # ['__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__',
    # '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__',
    # '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slots__', '__str__', '__subclasshook__',
    #  '__weakref__', '_accept', '_checkClosed', '_check_connected', '_check_sendfile_params', '_closed', '_connected', '_context',
    # '_create', '_decref_socketios', '_io_refs', '_real_close', '_real_connect', '_sendfile_use_send', '_sendfile_use_sendfile',
    # '_session', '_sslobj', 'accept', 'bind', 'cipher', 'close', 'compression', 'connect', 'connect_ex', 'context', 'detach',
    # 'do_handshake', 'do_handshake_on_connect', 'dup', 'family', 'fileno', 'get_channel_binding', 'get_inheritable', 'getblocking',
    #  'getpeercert', 'getpeername', 'getsockname', 'getsockopt', 'gettimeout', 'ioctl', 'listen', 'makefile', 'pending', 'proto', 'read',
    #  'recv', 'recv_into', 'recvfrom', 'recvfrom_into', 'recvmsg', 'recvmsg_into', 'selected_alpn_protocol', 'selected_npn_protocol',
    # 'send', 'sendall', 'sendfile', 'sendmsg', 'sendto', 'server_hostname', 'server_side', 'session', 'session_reused', 'set_inheritable',
    # 'setblocking', 'setsockopt', 'settimeout', 'share', 'shared_ciphers', 'shutdown', 'suppress_ragged_eofs', 'timeout', 'type', 'unwrap',
    # 'verify_client_post_handshake', 'version', 'write']
    #
    # DIR: SOCK.context
    # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
    # '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
    # '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_encode_hostname',
    # '_host_flags', '_load_windows_store_certs', '_msg_callback', '_set_alpn_protocols', '_set_npn_protocols', '_windows_cert_stores',
    # '_wrap_bio', '_wrap_socket', 'cert_store_stats', 'check_hostname', 'get_ca_certs', 'get_ciphers', 'hostname_checks_common_name',
    # 'keylog_filename', 'load_cert_chain', 'load_default_certs', 'load_dh_params', 'load_verify_locations', 'maximum_version',
    # 'minimum_version', 'num_tickets', 'options', 'post_handshake_auth', 'protocol', 'session_stats', 'set_alpn_protocols', 'set_ciphers',
    # 'set_default_verify_paths', 'set_ecdh_curve', 'set_npn_protocols', 'set_servername_callback', 'sni_callback', 'sslobject_class',
    # 'sslsocket_class', 'verify_flags', 'verify_mode', 'wrap_bio', 'wrap_socket']
    tlscon = SOCK.context
    ciphers = tlscon.get_ciphers()
    for cip in ciphers:
        print(f"Cipher: {cip}")
    print(f"CERT LOCATION: {requests.certs.where()}")
    print(f"SERVER HOSTNAME: {SOCK.server_hostname}")
    print(f"SOCK CONTEXT version: {SOCK.version()}")
    print(f"SOCK CONTEXT minimum_version: {SOCK.context.minimum_version}")
    print(f"SOCK CONTEXT maximum_version: {SOCK.context.maximum_version}")
    # print("Remote certificates: %s" % (tlscon.get_peer_certificate()))
    # print("Protocol version: %s" % tlscon.get_protocol_version_name())


if __name__ == "__main__":
    main()
