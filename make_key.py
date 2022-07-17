import os
import sys
import winreg as reg


cwd = os.getcwd()
python_exe = sys.executable

key_path = r'Directory\\Background\\shell\\DecryptPDF\\'

key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path)
reg.SetValue(key, '', reg.REG_SZ, '&Decrypt PDFs') 

key1 = reg.CreateKey(key, r"command")
reg.SetValue(key1, '', reg.REG_SZ, python_exe + f' "{cwd}\\decrypt.py"')


# checkout this git repo for more info on adding python script to windows registry
# https://github.com/seddie95/python_script_in_right_click_menu