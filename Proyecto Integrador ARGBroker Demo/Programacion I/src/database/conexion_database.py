import mysql.connector
import random
from datetime import datetime,timedelta

connection =mysql.connector.connect(
        host="camila-database.cwzjkyq4owgc.us-east-1.rds.amazonaws.com",
        database="argbroker",
        user="admin",
        password="8xXnpE4d9BXXeheu2pWH"
    )