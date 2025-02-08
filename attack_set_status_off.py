# modbus_client_set_status_off.py

from pyModbusTCP.client import ModbusClient

# Server configuration
SERVER_HOST = "192.168.168.7"  # Replace with your server's IP if running remotely
SERVER_PORT = 5020

# Register address for Status
STATUS_ADDR = 2  # This should match the STATUS_ADDR in your server code

def set_status_off():
    """Function to set the status register to 'Off' (0)."""
    client = ModbusClient(host=SERVER_HOST, port=SERVER_PORT, auto_open=True)
    try:
        # Write '0' to the status register to set status to 'Off'
        success = client.write_single_register(STATUS_ADDR, 0)
        if success:
            print("Status set to 'Off'.")
        else:
            print("Failed to write to the status register.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    set_status_off()
