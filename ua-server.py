# encoding: utf-8
import logging
import random
import time
from opcua import ua, Server

if __name__ == "__main__":

    logging.basicConfig(level=logging.WARN)
    logger = logging.getLogger("opcua.server.internal_subscription")
    logger.setLevel(logging.DEBUG)  # logging level of this logger: 10

    # setup our server
    server = Server()
    server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")

    # setup our own namespace, not really necessary but should as spec
    uri = "http://examples.freeopcua.github.io"
    idx = server.register_namespace(uri)

    # get Objects node, this is where we should put our nodes
    objects = server.get_objects_node()

    # populating our address space
    myobj = objects.add_object(idx, "dht22")
    var_temp = myobj.add_variable(idx, "Temperature", 0, ua.VariantType.Double)
    var_hum = myobj.add_variable(idx, "Humidity", 0, ua.VariantType.Double)

    server.start()

    try:
        humidity, temperature = 0, 0
        while True:
            time.sleep(1)
            humidity += 0.01
            temperature += 0.02
            var_temp.set_value(temperature)
            var_hum.set_value(humidity)
            logger.info('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
    finally:
        server.stop()
