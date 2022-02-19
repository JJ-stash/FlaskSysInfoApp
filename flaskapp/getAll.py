from flaskapp.getCPU import *
from flaskapp.getMemory import *
from flaskapp.getPlatform import *
from flaskapp.getProcs import *
from flaskapp.getUptime import *
from flaskapp.getUsers import *

def getAll():

	CPU = getCPU()
	Memory = getMemory()
	Platform = getPlatform()
	Procs = getProcs()
	Uptime = getUptime()
	Users = getUsers()

	sys_data = {
		'OS': Platform['OS'], 'Release': Platform['Release'], 'Version': Platform['Version'],
		'Cores': CPU['Cores'], 'Threads': CPU['Threads'],
		'Memory': Memory,
		'UptimeHr': Uptime['Hr'],  'UptimeMin': Uptime['Mn'], 'UptimeSec': Uptime['Sc'],
		'Users': Users,
		'Procs': Procs,
	}

	return sys_data