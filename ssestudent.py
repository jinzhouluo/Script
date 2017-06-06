import os
import time


for port in range(8080,8090):
    cmd = 'D: &cd \Strongene\ssestudentV2\web &start http-server -a 0.0.0.0 -p ' + str(port)
    os.system(cmd)

time.sleep(3)

for port in range(8080,8090):
    cmds = 'start chrome http://127.0.0.1:'+str(port)+'/dist/scripts/'
    os.system(cmds)