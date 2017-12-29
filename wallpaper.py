import ctypes,winreg,sys
try:
	REG_PATH=r'Software\Microsoft\Windows\CurrentVersion\Lock Screen\Creative'
	name='LandscapeAssetPath'
	registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH,0,winreg.KEY_READ)
	value, regtype = winreg.QueryValueEx(registry_key, name)
	winreg.CloseKey(registry_key)
except WindowsError:
	sys.exit()
ctypes.windll.user32.SystemParametersInfoW(20, 0, value, 3)