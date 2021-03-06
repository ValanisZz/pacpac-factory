#!/usr/bin/env python
from modbus_plc_siemens.r_api import *
# from modbus_plc_siemens.algorithms import *
from modbus_plc_siemens.client_init import ModbusClient


#########################################

if __name__ == "__main__":

    #####################
    #       Init        #
    #####################

    rospy.init_node("modbus_client_app")

    modbus_host = "192.168.0.199"
    modbus_port = 502

    modclient = None

    R = RApi()

    try:
        modclient = ModbusClient(modbus_host, modbus_port)
        R.print("Modbus client session successfully started")
    except:
        R.error("Modbus client session failed to start")
        exit()

    R.sleep(1)

    # in_ports = modclient.readRegisters(0, 112), (1, 112)
    R.print("Press any button on FT to proceed")

    while not in_ports:
        R.sleep(0.2)

    # r_print(out_ports)

    #####################
    #   Application     #
    #####################

    R.print("Available commands: 1, 2, 3, 4, stop")

    command = None

    while command != "stop":
        command = input("Command: ")

        try:
            # if command == "1":
            #     R.post(run_a)
            # elif command == "2":
            #     R.post(run_b)
            # elif command == "3":
            #     R.post(run_c)
            # elif command == "4":
            #     R.post(run_d)
            # else:
            #     exec(command)
            exec(command)
        except Exception as e:
            R.print(e)

    #####################
    #       Exit        #
    #####################

    R.print("Shutting down modbus client session...")

    try:
        rospy.signal_shutdown("Server shutting down")
    except:
        pass

    modclient.stopListening()
