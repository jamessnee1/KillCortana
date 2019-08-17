import os
print("Killing Cortana process...")
os.system("taskkill /F /IM SearchUI.exe")
os.system("taskkill /F /IM RuntimeBroker.exe")
os.system("taskkill /F /IM RemindersServer.exe")
print("Process completed!")