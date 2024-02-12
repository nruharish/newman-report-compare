import json
CONFIG_FILE = r'./config.json'
class Config:
    __shared_state = {}
    def __init__(self):
        if(len(self.__shared_state) == 0):
            with open(CONFIG_FILE) as f:
                self.__shared_state = json.load(f)
    def get_value(self, key):
        return self.__shared_state["config"][key]


