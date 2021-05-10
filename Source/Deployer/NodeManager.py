
import pymongo
import ConfigHelper
import os
import requests
from pathlib import Path
import Logger
import json
import sys

class NodeManager:
    def __init__(self, nodeConfig):
        self.NodeConfig = nodeConfig
        self.StatusUrl = ConfigHelper.GetStatusEndPoint().format(nodeConfig.Ip, nodeConfig.Port)
        self.LoadUrl = ConfigHelper.GetLoadEndPoint().format(nodeConfig.Ip, nodeConfig.Port)
        self.cpu = sys.maxsize
        self.temperature = sys.maxsize
        self.bandwidthUsage = sys.maxsize
        self.Up = True

    def StartNode(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        path = Path(dir_path)
        parentDirectory = path.parent.absolute()
        dir_path = str(dir_path).replace(" ", r"\ ")
        #os.system("gnome-terminal -e 'sh -c \"cd {}; python3 NodeManager.py {} {} {}; exec bash\" '".format(dir_path, ip, port, heartBeatInterval))
        os.system("gnome-terminal -e 'sh -c \"cd {}; python3 Node.py {} {} {}; exec bash\" '".format(dir_path, self.NodeConfig.Ip, self.NodeConfig.Port, self.NodeConfig.HeartbeatInterval))
        return True
    
    def CheckIfUp(self):
        try:
            response = requests.get(self.StatusUrl)
            if(response.ok):
                responseText = response.text
                responseJson = json.loads(responseText)
                if(responseJson["Status"] == "Alive"):
                    return True
            return False
        except Exception as e:
            Logger.Log(e)
            return False
    
    def SetStats(self):
        try:
            response = requests.get(self.LoadUrl)
            if(response.ok):
                responseText = response.text()
                responseJson = json.loads(responseText)
                self.cpu = responseJson["cpu"]
                self.temperature = responseJson["temperature"]
                self.bandwidthUsage = responseJson["bandwidthUsage"]
        except Exception as e:
            Logger.Log(e)


    



# try:
    
    
# except Exception as e:
#     raise e
#     print(e)
#     print("Cant open the config file Deployer.config. Cant start deployer")