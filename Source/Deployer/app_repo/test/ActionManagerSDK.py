from kafka import KafkaProducer
import json
# sys.path.append('../communication_module')
# import communication_api as ca
# import prodapi

deptoact = { 'action': None,
  'receiver_id' :None,
  'sensor_info': 
  { 
      'loc': None,
      'type':None,
      'value':None
    }
}
sensor_info = {'loc':None,'type':None,'value':None}


producer = KafkaProducer(bootstrap_servers='localhost:9092',
value_serializer=lambda v: json.dumps(v).encode('utf-8'))  
def send_message(topic,message):
    producer.send(topic, value = message)
    producer.flush()

def set_action(action_type,receiver_email,sensor_type,sensor_location,sensor_value):
    deptoact['action'] = action_type
    deptoact['receiver_id'] = receiver_email
    sensor_info['type'] = sensor_type
    sensor_info['loc'] = sensor_location
    sensor_info['value'] = sensor_value
    deptoact['sensor_info'] = sensor_info
    send_message('dep_act',deptoact)