from RPA.Robocorp.Vault import Vault
from tls_utils import set_python_logging, patch_send


def main():
    set_python_logging()
    patch_send()
    # The bot just tries to read a secret from Control Room Vault to test the connection.
    secrets = Vault().get_secret("ever")


if __name__ == "__main__":
    main()
