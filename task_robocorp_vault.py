import os
from RPA.Robocorp.Vault import Vault
from tls_utils import set_python_logging, patch_send


def main():
    #
    # CONFIGURATIONS FOR THE REQUEST LOGGING
    #
    set_python_logging()
    patch_send()

    # The bot just tries to read a secret from Control Room Vault to test the connection.
    # The target Robocorp Vault name can be set with environment variable `TARGET_ROBOCORP_VAULT`.
    # The default Vault name is 'ever'
    NAME_OF_THE_VAULT = os.getenv("TARGET_ROBOCORP_VAULT", "ever")
    secrets = Vault().get_secret(NAME_OF_THE_VAULT)


if __name__ == "__main__":
    main()
