
import json
import subprocess
import os
from pathlib import Path
import communication_api as CM
import sys
import requests
import re

class Node:
    def __init__(self, ip, port) -> None:
        self.ip = ip
        self.port = port
        self.currentLoad = sys.maxsize
    def GetDeployUrl(self):
        return "http://{}:{}/Deploy".format(self.ip, self.port)
    def GetStatsUrl(self):
        return "http://{}:{}/GetLoadStats".format(self.ip, self.port)

    def CalculateLoad(self, cpu, bandwidth, temperature):
        coeff1 = 0.2
        coeff2 = 0.9
        coeff3 = 0.6
        stat = coeff1 * bandwidth + coeff2 * cpu + coeff3 * temperature
        return stat

#worker_nodes = [Node("127.0.0.10", "40010")]
worker_nodes = []

dir_path = os.path.dirname(os.path.realpath(__file__))
configFile = "{}/DeployerConfig.json".format(dir_path)
path = Path(dir_path)
parentDirectory = path.parent.absolute()

#load_balancing_api = []
#pat = re.compile(r"(,)")
#print (pat.sub(" \\1 ", str(parentDirectory)))
parentDirectory = str(parentDirectory).replace(" ", "\ ")
nodes = []
def CreateWorkerNodes():
    with open(configFile, 'r') as f:
        config = json.load(f)
    heartBeatInterval = config["HeartBeatInterval"]
    for node in config["Nodes"]:
        ip = node["IP"]
        port = node["PORT"]
        worker_nodes.append(Node(ip, port))
        #shellscript = subprocess.Popen(["python3",  "Deployer/NodeManager.py",  ip, port, heartBeatInterval], stdin=subprocess.PIPE, cwd=parentDirectory)
        #shellscript = subprocess.call(['gnome-terminal', '-x', "python3 Deployer/NodeManager.py {} {} {}".format(ip, port, heartBeatInterval)], cwd=parentDirectory)
        #shellscript = subprocess.check_output(['gnome-terminal', '-x', "cd {} & python3 Deployer/NodeManager.py {} {} {}".format(parentDirectory,ip, port, heartBeatInterval)], cwd=parentDirectory, shell=True)
        os.system("gnome-terminal -e 'sh -c \"cd {}; python3 Deployer/NodeManager.py {} {} {}; exec bash\" '".format(parentDirectory, ip, port, heartBeatInterval))
        #nodes.append(shellscript)
def CreateSensorBindingApi(ip, port):
    os.system("gnome-terminal -e 'sh -c \"cd {}; python3 Deployer/SensorBinding.py {} {} {}; exec bash\" '".format(ip, port))


def LoadBalance():
    stats = []
    min_load_node = None
    min_load = sys.maxsize
    for node in worker_nodes:
        api = node.GetStatsUrl()
        response = requests.get(api)
        if(response.ok):
            respObj = json.loads(response.text)
            bandwidth = respObj['bandwidthUsage']
            cpu = respObj['cpu']
            temperature = respObj['temperature']
            node.currentLoad = node.CalculateLoad(cpu, bandwidth, temperature)
            if(node.currentLoad < min_load):
                min_load_node = node
                min_load = node.currentLoad
    return min_load_node
        
    

    



def ListenToDeployments():
    appName = "appname"
    algoName = "algoName"
    nodeToDeploy = LoadBalance()
    if(nodeToDeploy != None):
        apiToDeploy = nodeToDeploy.GetDeployUrl()
        apiWithParameters = apiToDeploy + "/?appName={}&algoName={}".format(appName, algoName)
        deployResponse = requests.get(apiWithParameters)
        if(deployResponse.ok):
            print("Deployment Successful")        
        else: #Deployment Failed Report back to scheduler
            pass

    else: #Report to fault tolerance 
        #to do
        pass
    #while(True):
    #    pass

CreateWorkerNodes()
ListenToDeployments()



