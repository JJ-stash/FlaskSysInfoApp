from uptime import uptime

def getUptime():
    uptime_dict = {}

    uptimeA = int(uptime())

    uptimeHr = int(uptimeA / 3600)
    uptimeMn = int(uptimeA / 60 % 60)
    uptimeSc = int(uptimeA % 60)

    uptime_dict.update({'Hr': uptimeHr, 'Mn': uptimeMn, 'Sc': uptimeSc})

    return uptime_dict