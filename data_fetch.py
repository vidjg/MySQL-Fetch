# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 23:43:29 2018

@author: Shuai
"""

import pandas as pd
import mysql.connector


rasp = mysql.connector.connect(user='martin', password='ronaldo', host='192.168.137.162')
cursor = rasp.cursor()

query = "SELECT * FROM {0}".format('company_data.company_profile')

cursor.execute(query)
field_names = [i[0] for i in cursor.description]

data = pd.DataFrame(cursor.fetchall(), columns=field_names)

print('Done!')
