from bluedot.btcomm import BluetoothServer
from signal import pause

def ReceptionMessage(data):
    print('le message recu est ' + data)
    msgEnvoye = 'coucou '+data+'\n'
    s.send(msgEnvoye)

s = BluetoothServer(ReceptionMessage)
pause()