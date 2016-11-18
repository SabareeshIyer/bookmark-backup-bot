import shutil
import datetime

d = datetime.date.today()
filename = "bookmarks_"+str(d.month)+"_"+str(d.day)+"_"+str(d.year)
filepath = r"C:\Users\username\Documents\bm_export_files\\"+filename

shutil.copy2(r"C:\Users\username\AppData\Local\Google\Chrome\User Data\Default\Bookmarks", filepath)

