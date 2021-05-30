import mysql.connector
from mysql.connector import errorcode
from datetime import datetime
#from urlparse import urlparse
##===============================================

class DatabaseUtility: 
	def __init__(self, database, tableName):
		self.db = database
		self.tableName = tableName
		self.cnx = mysql.connector.connect(user = 'root',password = '1729',host = '127.0.0.1')
		self.cursor = self.cnx.cursor()

		self.ConnectToDatabase()
		self.CreateTable()
		
	def ConnectToDatabase(self):
		try:
			print("Here1")
			self.cnx.database = self.db
		except:
			print("Here2")
			self.CreateDatabase()
			self.cnx.database = self.db
			

	def CreateDatabase(self):
		try:
			self.RunCommand("CREATE DATABASE %s DEFAULT CHARACTER SET 'utf8';" %self.db)
		except mysql.connector.Error as err:
			print("Failed creating database: {}".format(err))

	def CreateTable(self):
		cmd = (" CREATE TABLE IF NOT EXISTS " + self.tableName + " ("
			" `RM_Name` char(50) NOT NULL,"
			" `RM_Code` char(50) NOT NULL,"
			" `RM_Qty` int(10) NOT NULL,"
			" `RM_Floor_X` float(10) NOT NULL,"
			" `RM_Floor_Y` float(10) NOT NULL,"
			" `RM_Stack_X` int(10) NOT NULL,"
			" `RM_Stack_Y` int(10) NOT NULL,"
			" 'RM_Num_Processes' int(10) NOT NULL"
			" `RM_Process1_Name` char(50) NULL,"
			" `RM_Process1_X` float(10) NULL,"
			" `RM_Process1_Y` float(10) NULL,"
			" `RM_Process2_Name` char(50) NULL,"
			" `RM_Process2_X` float(10) NULL,"
			" `RM_Process2_Y` float(10) NULL,"
			" `RM_Process3_Name` char(50) NULL,"
			" `RM_Process3_X` float(10) NULL,"
			" `RM_Process3_Y` float(10) NULL,"
			" `RM_Process4_Name` char(50) NULL,"
			" `RM_Process4_X` float(10) NULL,"
			" `RM_Process4_Y` float(10) NULL,"
			" `RM_Process5_Name` char(50) NULL,"
			" `RM_Process5_X` float(10) NULL,"
			" `RM_Process5_Y` float(10) NULL,"
			" `RM_Process6_Name` char(50) NULL,"
			" `RM_Process6_X` float(10) NULL,"
			" `RM_Process6_Y` float(10) NULL,"
			" `RM_Process7_Name` char(50) NULL,"
			" `RM_Process7_X` float(10) NULL,"
			" `RM_Process7_Y` float(10) NULL,"
			" `RM_Process8_Name` char(50) NULL,"
			" `RM_Process8_X` float(10) NULL,"
			" `RM_Process8_Y` float(10) NULL,"
			" PRIMARY KEY (`RM_Name`, `RM_ID`)"
			") ENGINE=InnoDB;")
		self.RunCommand(cmd)

	def GetTable(self):
		self.CreateTable()
		return self.RunCommand("SELECT * FROM %s;" % self.tableName)

	def GetColumns(self):
		return self.RunCommand("SHOW COLUMNS FROM %s;" % self.tableName)

	def RunCommand(self, cmd):
		print ("RUNNING COMMAND: " + cmd)
		try:
			self.cursor.execute(cmd)
		except mysql.connector.Error as err:
			print ('ERROR MESSAGE: ' + str(err.msg))
			print ('WITH ' + cmd)
		try:
			msg = self.cursor.fetchall()
		except:
			msg = self.cursor.fetchone()
		return msg

	def AddEntryToTable(self, RMname, RMCode, RMQty, RM_Floor_X, RM_Floor_Y, RM_Stack_X, RM_Stack_Y, RM_Num_Processes, RM_Process1_Name, RM_Process1_X, RM_Process1_Y, RM_Process2_Name, RM_Process2_X, RM_Process2_Y, RM_Process3_Name, RM_Process3_X, RM_Process3_Y, RM_Process4_Name, RM_Process4_X, RM_Process4_Y, RM_Process5_Name, RM_Process5_X, RM_Process5_Y, RM_Process6_Name, RM_Process6_X, RM_Process6_Y, RM_Process7_Name, RM_Process7_X, RM_Process7_Y, RM_Process8_Name, RM_Process8_X, RM_Process8_Y):
		
		cmd = " INSERT INTO " + self.tableName + " (`RM_Name`, `RM_Code`, `RM_Qty`, `RM_Floor_X`, `RM_Floor_Y`, `RM_Stack_X`, `RM_Stack_Y`, 'RM_Num_Processes',`RM_Process1_Name`, `RM_Process1_X`, `RM_Process1_Y`, `RM_Process2_Name`, `RM_Process2_X`, `RM_Process2_Y`, `RM_Process3_Name`, `RM_Process3_X`, `RM_Process3_Y`, `RM_Process4_Name`, `RM_Process4_X`, `RM_Process4_Y`, `RM_Process5_Name`, `RM_Process5_X`, `RM_Process5_Y`, `RM_Process6_Name`, `RM_Process6_X`, `RM_Process6_Y`, `RM_Process7_Name`, `RM_Process7_X`, `RM_Process7_Y`, `RM_Process8_Name`, `RM_Process8_X`, `RM_Process8_Y`)"
		cmd += " VALUES ('%s', '%s', %d, %f, %f, %d, %d, %d, '%s', %f, %f, '%s', %f, %f, '%s', %f, %f, '%s', %f, %f, '%s', %f, %f, '%s', %f, %f, '%s', %f, %f, '%s', %f, %f)" % (RMname, RMCode, RMQty, RM_Floor_X, RM_Floor_Y, RM_Stack_X, RM_Stack_Y, RM_Num_Processes, RM_Process1_Name, RM_Process1_X, RM_Process1_Y, RM_Process2_Name, RM_Process2_X, RM_Process2_Y, RM_Process3_Name, RM_Process3_X, RM_Process3_Y, RM_Process4_Name, RM_Process4_X, RM_Process4_Y, RM_Process5_Name, RM_Process5_X, RM_Process5_Y, RM_Process6_Name, RM_Process6_X, RM_Process6_Y, RM_Process7_Name, RM_Process7_X, RM_Process7_Y, RM_Process8_Name, RM_Process8_X, RM_Process8_Y)
		self.RunCommand(cmd)

	def __del__(self):
		self.cnx.commit()
		self.cursor.close()
		self.cnx.close()

##===============================================
##===============================================


if __name__ == '__main__':
	db = 'CandidateProducts'
	tableName = 'HydraulicFlange'

	dbu = DatabaseUtility(db, tableName)

	dbu.AddEntryToTable('Sheet', 11, 25, 100.00, 100.00, 2, 2, 4, 'CNC Milling', 25.00, 25.00, 'CNC Grinding', 50.00, 50.00, 'Inspection', 75.00, 75.00, 'Welding', 150.00, 150.00, 'NULL', -1.00, -1.00, 'NULL', -1.00, -1.00, 'NULL', -1.00, -1.00, 'NULL', -1.00, -1.00)
	dbu.AddEntryToTable('Pipe', 12, 30, 200.00, 200.00, 3, 4, 4, 'CNC Turning', 33.00, 33.00, 'CNC Grinding', 50.00, 50.00, 'Inspection', 75.00, 75.00, 'Welding', 150.00, 150.00, 'NULL', -1.00, -1.00, 'NULL', -1.00, -1.00, 'NULL', -1.00, -1.00, 'NULL', -1.00, -1.00)
	#print (dbu.GetColumns())
	#print(dbu.GetTable())
