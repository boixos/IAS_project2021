    docker build -f Dockerfile -t algo1.py:latest .
    docker run --network host -dit algo1.py     