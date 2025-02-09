# wind_farm_modbus_server.py

from pyModbusTCP.server import ModbusServer
import threading
import time
import random
import logging

# Configure logging
logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', level=logging.INFO)

# Server configuration
SERVER_HOST = "0.0.0.0"  # Listen on all interfaces
SERVER_PORT = 5020       # Use port 5020 to avoid requiring admin privileges

# Register addresses
PITCH_ANGLE_ADDR = 0     # Holding Register address for Pitch Angle
WIND_SPEED_ADDR = 1      # Holding Register address for Wind Speed
STATUS_ADDR = 2          # Holding Register address for Status (0: Off, 1: On)

def update_wind_farm_values(server):
    """Function to simulate and update wind farm values."""
    while True:
        # Simulate data
        pitch_angle = random.uniform(0, 90)   # Pitch angle between 0 and 90 degrees
        wind_speed = random.uniform(0, 25)    # Wind speed between 0 and 25 m/s

        # Read the status register
        status_list = server.data_bank.get_holding_registers(STATUS_ADDR, 1)
        if status_list:
            status = status_list[0]
        else:
            status = 1  # Default status is 'On'

        # Check if status is 'Off' (0)
        if status == 0:
            logging.info("Status is 'Off'. Exiting the program.")
            server.stop()
            break

        # Scale values to integers (Modbus registers are 16-bit integers)
        pitch_angle_scaled = int(pitch_angle * 100)  # Multiply by 100 to preserve two decimal places
        wind_speed_scaled = int(wind_speed * 100)

        # Update the DataBank via the server instance
        server.data_bank.set_holding_registers(PITCH_ANGLE_ADDR, [pitch_angle_scaled])
        server.data_bank.set_holding_registers(WIND_SPEED_ADDR, [wind_speed_scaled])
        # The status register can be written by the client, so we don't overwrite it here

        # Log the updated values
        logging.info(f"Updated values - Pitch Angle: {pitch_angle:.2f}°, "
                     f"Wind Speed: {wind_speed:.2f} m/s, Status: {'On' if status else 'Off'}")

        # Wait before the next update
        time.sleep(10)

def run_server():
    # Create an instance of ModbusServer
    server = ModbusServer(host=SERVER_HOST, port=SERVER_PORT, no_block=True)

    # Initialize the DataBank with default values
    server.data_bank.set_holding_registers(0, [0] * 100)  # Initialize 100 registers to zero
    server.data_bank.set_holding_registers(STATUS_ADDR, [1])  # Set initial status to 'On'

    # Start the server
    try:
        server.start()
        logging.info(f"Modbus server started on {SERVER_HOST}:{SERVER_PORT}")

        # Start the update thread, passing the server instance
        updater_thread = threading.Thread(target=update_wind_farm_values, args=(server,))
        updater_thread.daemon = True
        updater_thread.start()

        # Keep the main thread running
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info("Server is shutting down...")
        server.stop()

if __name__ == "__main__":
    run_server()
