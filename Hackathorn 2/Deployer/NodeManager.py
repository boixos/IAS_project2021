import sys
import flask
from flask import request, jsonify
import threading
import random
import json
import datetime
import communication_api as cm
import time
from flask import request
import os
import shutil
import subprocess
import tempfile

# ip = sys.argv[1]
# port = int(sys.argv[2])
# heartBeatInterval = int(sys.argv[3])
NetworkFilePath = "./"

ip = "127.10.10.10"
port = 40000
heartBeatInterval = 10

class Expando(object):
    pass

class Stats:
    def __init__(self) -> None:
        self.cpu = 0
        self.temperature = 0
        self.bandwidthUsage = 0
    
    def AssignRandom(self):
        self.cpu = random.randint(0, 100)
        self.temperature = random.randint(30, 90)
        self.bandwidthUsage = round(random.uniform(0, 1), 2)

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    #print("adfadfadfasdfa")
    return ''' Hi, Ur deployer Running At {}:{} is Up and active ....... have a naise day '''.format(ip, port)

@app.route("/GetLoadStats", methods=['GET'])
def GetLoadAndStats():
    currentStats = Stats()
    currentStats.AssignRandom()
    return  json.dumps(currentStats.__dict__)

#@app.route("/Deploy/", methods=['GET'])'
def Copy_dir(source, destination):
    if(os.path.exists(destination)):
        shutil.rmtree(destination)
    shutil.copytree(source, destination)



def generate_files(appl_name,algo_name) :
    tempDirectory =  "Deployer/temp" 
    
    source = NetworkFilePath + "{}".format(appl_name)
    destination = tempDirectory
    Copy_dir(source, destination)
    #shutil.copyfile(source, destination)
    str1 = "FROM python:3.7"
    str1 = str1 + "\n" + "RUN mkdir /app" 
    str1 = str1 + "\n" + "WORKDIR /app"
    str1 = str1 + "\n" + "ADD . /app/".format(appl_name)
    str1 = str1 + "\n" + "RUN pip3 install -r requirements.txt"
    str1 = str1 + "\n" + "CMD [\"python3\", \""+algo_name+"\"]"
    file1 = open("{}/Dockerfile".format(destination),"w")
    file1.write(str1)
    file1.close()
    file1 = open("{}/Deploy.sh".format(destination),"w")
    file1.write("\
    docker build -f Dockerfile -t {}:latest .\n\
    docker run --network host -dit {} \
    ".format(algo_name, algo_name))
    file1.close()
    #subprocess.Popen(["Deploy.sh"], stdin=subprocess.PIPE, cwd=destination)
    os.system("gnome-terminal -e 'sh -c \"{} {} {}; exec bash\" '".format(parentDirectory, ip, port, heartBeatInterval))

@app.route("/Deploy", methods=['GET'])
def deployer_file_generator() :
    appl_name = request.args.get('appName')
    algo_name = request.args.get('algoName')
    generate_files(appl_name,algo_name)
	

def HeartBeatMonitor(interval):
    while True:
        dynamicObj = Expando()
        dynamicObj.Ip = ip
        dynamicObj.Port = port
        dynamicObj.Status = "OK"
        now = datetime.datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        dynamicObj.Time = date_time
        jsonConverted = json.dumps(dynamicObj.__dict__)
        cm.depmanager_nodeheartbeat(jsonConverted)
        #print(jsonConverted)
        time.sleep(interval)


    

#heartBeatThread = threading.Thread(target=HeartBeatMonitor, args=(heartBeatInterval,))
#heartBeatThread.start()
#app.run(port=port+40, host=ip)
generate_files("app_name", "algo1.py")