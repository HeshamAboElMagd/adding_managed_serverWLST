from java.util import *
from javax.management import *

username = 'weblogic'
password = 'weblogic8'

connect(username,password,"t3://localhost:7001")
edit()
startEdit()
svr = cmo.createServer("myManagedServer1")
svr.setListenPort(7004)
svr.setListenAddress("localhost")
save()
activate(block="true")
disconnect()
exit()