class RootException(Exception):
    pass


class ClientMissingEmailError(Exception):
    pass


class ClientMissingPasswordError(Exception):
    pass


class InvalidEmailOrPasswordError(Exception):
    pass


class InvalidSecretError(Exception):
    pass


class ServerHasNoSecretError(Exception):
    pass


class ServerMissingEmailError(Exception):
    pass


class ServerMissingPasswordError(Exception):
    pass
