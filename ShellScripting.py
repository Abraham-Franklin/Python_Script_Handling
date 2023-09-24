import subprocess, os

subprocess.Popen("echo 'shell scripting made easy with python'", shell=True)
os.system("echo 'using os to shellscript'")
os.system('pwd')
os.system('ls')