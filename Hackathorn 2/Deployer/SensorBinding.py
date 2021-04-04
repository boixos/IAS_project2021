from flask import request
import flask
import sys
import communication_api as cm


ip = sys.argv[1]
port = int(sys.argv[2])
heartBeatInterval = int(sys.argv[3])


app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def GetSensorData():
    dictm = {"LocationId" : "Pune", "SensorId" : "SensorId"}
    cm.depmanager_senmanager(dictm)
    topics = cm.senmanager_depmanager_rep()
    #topics = []
    for topic in topics:
        data = cm.sensordata(topic)
     

    #Do what ever u want with it ....... Convert it to json and expose

app.run()