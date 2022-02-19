import platform

def getPlatform():
	os_dict = {}

	os = platform.system()
	os_release = platform.release()
	os_version = platform.version()

	os_dict.update({'OS': os, 'Release': os_release, 'Version':os_version})

	return os_dict