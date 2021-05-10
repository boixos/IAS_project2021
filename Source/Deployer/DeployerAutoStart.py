import os
os.system("gnome-terminal -e 'sh -c \"python3 ServerLCM.py; exec bash\" '")
os.system("gnome-terminal -e 'sh -c \"python3 ServiceLCM.py; exec bash\" '")
os.system("gnome-terminal -e 'sh -c \"python3 LoadBalancer.py; exec bash\" '")