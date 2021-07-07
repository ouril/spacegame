class JsonRPCError(TypeError):
    def __init__(self, msg: str):
        self.msg = msg


class JsonRPCData:
    STOP = "stop"
    START = 'start'
    CALC = 'calc'
    TURN = 'turn'

    class MethodKeys:
        STOP = "stop"
        START = 'start'
        REMOTE = 'remote'
        GAME_NAME = 'game_name'
        GAME_ACT = 'game_act'
        TURN_ACT = 'turn_act'

    def __init__(self, map: dict):
        try:
            if 'jsonrpc' in map:
                self._jsonrpc = map['jsonrpc']
            else:
                self._jsonrpc = None
            self.method = map['method']
            self.params = map['params']
            self.id = map['id']
            self._result = None
        except:
            raise JsonRPCError("Not RPC!")

    def set_result(self, result):
        self._result = result

    def get_rpc_result(self) -> tuple:
        if isinstance(self._result, dict) and self._jsonrpc is not None:
            return True, {
                "jsonrpc": "2.0",
                "result": self._result,
                "id": self.id
            }
        if self._jsonrpc is None and self._result is not None:
            return True, {
                "result": self._result,
                "id": self.id
            }
        return False, None
