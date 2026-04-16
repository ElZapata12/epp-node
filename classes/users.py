from classes.auth import Authenticator
from classes.model import IAModel


class Department:

    def __init__(self, name:str, epp:list[str]):
        self._name = name
        self._epp = epp


class EPPNodeFacade:

    def __init__(self, epp_model : IAModel, auth : Authenticator):
        self._epp_model = epp_model
        self._auth = auth

    def scan_frame(self):
        return self._epp_model.scan_frame()

