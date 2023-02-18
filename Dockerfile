from python

workdir /app
copy requirements.txt requirements.txt

run apt update & \
    apt install nano & \
    pip install --upgrade pip & \
    pip install -r requirements.txt
    