def BLE():


    from bluedot.btcomm import BluetoothServer
    from signal import pause

    def ReceptionMessage(data):
        print(data)
        
        # Bon je peux commencer le code à partir d'ici
        if data=="enfant":
            test(os,3)
            
        elif data=="enfant_auto":
            test_enfant(qs,1)

        elif data=="enfant_manuelle":
            test_adulte(qs,3)

        elif data=="suivant":
            print("nice")

        elif data=="arriere":
            print("nice")

        elif data=="pause":
            print("nice")

        elif data=="retour":
            print("nice")

    s = BluetoothServer(ReceptionMessage)


    pause()
