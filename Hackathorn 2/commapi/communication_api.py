import prodapi
import json
import threading

def sensormanager_monitor(data):
    prodapi.send_message('sen_mo',data)

def monitor_sensormanager(func):
    from kafka import KafkaConsumer
    consumer = KafkaConsumer('sen_mo',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda x: json.loads(x.decode('utf-8')))
    for message in consumer:
        th = threading.Thread(target=func,args=(message.value,))
        th.start()



def appmanager_monitor(data):
    prodapi.send_message('app_mo',data)

def monitor_appmanager(func):
    from kafka import KafkaConsumer
    consumer = KafkaConsumer('app_mo',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda x: json.loads(x.decode('utf-8')))
    for message in consumer:
        th = threading.Thread(target=func,args=(message.value))
        th.start()

def actionmanager_monitor(data):
    prodapi.send_message('act_mo', data)


def monitor_actionmanager(func):
    from kafka import KafkaConsumer
    consumer = KafkaConsumer('act_mo',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda x: json.loads(x.decode('utf-8')))
    for message in consumer:
        th = threading.Thread(target=func,args=(message.value))
        th.start()



def depmanager_monitor(data):
    prodapi.send_message('dep_mo',data)

def monitor_depmanager(func):
    from kafka import KafkaConsumer
    consumer = KafkaConsumer('dep_mo',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda x: json.loads(x.decode('utf-8')))
    for message in consumer:
        th = threading.Thread(target=func,args=(message.value))
        th.start()

def scheduler_monitor(data):
    prodapi.send_message('sch_mo',data)

def monitor_scheduler(func):
    from kafka import KafkaConsumer
    consumer = KafkaConsumer('sch_mo',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda x: json.loads(x.decode('utf-8')))
    for message in consumer:
        th = threading.Thread(target=func,args=(message.value))
        th.start()

def depstack_monitor(data):
    prodapi.send_message('depst_mo',data)

def monitor_depstack(func):
    from kafka import KafkaConsumer
    consumer = KafkaConsumer('depst_mo',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda x: json.loads(x.decode('utf-8')))
    for message in consumer:
        th = threading.Thread(target=func,args=(message.value))
        th.start()

def topman_monitor(data):
   prodapi.send_message('top_mo',data)

def monitor_topman(func):
    from kafka import KafkaConsumer
    consumer = KafkaConsumer('top_mo',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda x: json.loads(x.decode('utf-8')))
    for message in consumer:
        th = threading.Thread(target=func,args=(message.value))
        th.start()

def topman_monitor_req(data):
    prodapi.send_message('top_mo_r',data)

def monitor_topman_req(func):
    from kafka import KafkaConsumer
    consumer = KafkaConsumer('top_mo_r',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda x: json.loads(x.decode('utf-8')))
    for message in consumer:
        th = threading.Thread(target=func,args=(message.value))
        th.start()


def appmanager_depstack(data):
    prodapi.send_message('app_dep',data)

def depstack_appmanager(func):
    from kafka import KafkaConsumer
    consumer = KafkaConsumer('app_dep',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda x: json.loads(x.decode('utf-8')))
    for message in consumer:
        th = threading.Thread(target=func,args=(message.value))
        th.start()

def sensordata(topic):
    from kafka import KafkaConsumer
    consumer = KafkaConsumer(topic,
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda x: json.loads(x.decode('utf-8')))
    for message in consumer:
        mess= (message.value)
        yield mess
	

def depmanager_senmanager(data):
    prodapi.send_message('dep_sen',data)

def senmanager_depmanager(func):
    from kafka import KafkaConsumer
    consumer = KafkaConsumer('dep_sen',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda x: json.loads(x.decode('utf-8')))
    for message in consumer:
        th = threading.Thread(target=func,args=(message.value,))
        th.start()
        break

def depmanager_senmanager_rep(data):
    prodapi.send_message('dep_sen_rep',data)

def senmanager_depmanager_rep():
    from kafka import KafkaConsumer
    consumer = KafkaConsumer('dep_sen_rep',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda x: json.loads(x.decode('utf-8')))
    for message in consumer:
        #th = threading.Thread(target=func,args=(message.value,))
        #th.start()
        return message.value
        break


def depmanager_appmanager(data):
    prodapi.send_message('dep_app',data)

def appmanager_depmanager(func):
    from kafka import KafkaConsumer
    consumer = KafkaConsumer('dep_app',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda x: json.loads(x.decode('utf-8')))
    for message in consumer:
        th = threading.Thread(target=func,args=(message.value))
        th.start()

def depmanager_actmanager(data):
    prodapi.send_message('dep_act',data)

def actmanager_depmanager(func):
    from kafka import KafkaConsumer
    consumer = KafkaConsumer('dep_act',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda x: json.loads(x.decode('utf-8')))
    for message in consumer:
        th = threading.Thread(target=func,args=(message.value))
        th.start()


def appmanager_senmanager(data):
    prodapi.send_message('app_sen',data)

def senmanager_appmanager(func):
    from kafka import KafkaConsumer
    consumer = KafkaConsumer('app_sen',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda x: json.loads(x.decode('utf-8')))
    for message in consumer:
        th = threading.Thread(target=func,args=(message.value))
        th.start()