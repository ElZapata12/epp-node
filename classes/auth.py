from abc import ABC, abstractmethod

import requests


class Authenticator(ABC):

    @abstractmethod
    def set_server_url(self, **kwargs) -> None:
        pass

    @abstractmethod
    def set_server_credentials(self, **kwargs) -> None:
        pass


class JWTAuthenticator(Authenticator):

    def __init__(self):
        self._server_url = ""
        self._credentials = {
            "username": "",
            "password": ""
        }
        self.access_token = "",
        self.refresh_token= "",



    def set_server_url(self, **kwargs) -> None:
        self._server_url = kwargs.get("url")

    def set_server_credentials(self, **kwargs) -> None:
        self._credentials = {
            "username": kwargs.get("username"),
            "password": kwargs.get("password")
        }

    def login(self):
        response = requests.post(self._server_url, json=self._credentials)

        if response.ok:
            self._set_server_tokens(refresh="",access="")

        self.set_server_credentials(username='', password='')

    def _set_server_tokens(self, **kwargs):
        self.access_token = kwargs.get("access")
        self.refresh_token = kwargs.get("refresh")

