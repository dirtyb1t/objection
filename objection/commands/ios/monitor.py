from objection.state.connection import state_connection


def crypto_disable(args: list = None) -> None:
    """
        Attempts to disable ios crypto monitoring.

        :param args:
        :return:
    """

    api = state_connection.get_api()
    api.ios_monitor_crypto_disable()


def crypto_enable(args: list = None) -> None:
    """
        Attempts to enable ios crypto monitoring.

        :param args:
        :return:
    """

    api = state_connection.get_api()
    api.ios_monitor_crypto_enable()
