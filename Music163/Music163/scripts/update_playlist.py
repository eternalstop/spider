# _*_coding: utf8_*_
import pymysql
import pandas as pd


db = pymysql.connect(host="localhost", user="root", passwd="Missy@u777", db="music163", charset="utf8")
cursor = db.cursor()
info = pd.read_csv('../test.csv', header=None, names=['name', 'tags', 'plays', 'collections', 'url'])


for flag in range(len(info['name'])):
	update_sql = "update music163.playlist set name='{}',plays='{}',tags='{}',collections='{}' where url='{}'".format(info['name'][flag], info['plays'][flag], info['tags'][flag], info['collections'][flag], info['url'][flag])
	try:
		cursor.execute(update_sql)
		result = cursor.fetchall()
	except:
		print(update_sql)
		continue
	# print(result)
	# break

db.commit()
db.close()
