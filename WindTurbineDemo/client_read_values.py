# modbus_client_read_values.py
from pyModbusTCP.client import ModbusClient

SERVER_HOST = "localhost"
SERVER_PORT = 5020

def read_wind_farm_values():
    client = ModbusClient(host=SERVER_HOST, port=SERVER_PORT, auto_open=True)
    try:
        regs = client.read_holding_registers(0, 3)
        if regs:
            pitch_angle = regs[0] / 100.0
            wind_speed = regs[1] / 100.0
            status = regs[2]

            print(f"Pitch Angle: {pitch_angle:.2f} degrees")
            print(f"Wind Speed: {wind_speed:.2f} m/s")
            print(f"Status: {'On' if status else 'Off'}")
        else:
            print("Failed to read registers.")
    finally:
        client.close()

if __name__ == "__main__":
    read_wind_farm_values()
