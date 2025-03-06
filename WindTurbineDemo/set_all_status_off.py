from pyModbusTCP.client import ModbusClient

# Server configuration
SERVER_HOST = "192.168.168.7"  # Replace with your server's IP if running remotely
SERVER_PORT = 5020

# Register address range
MIN_STATUS_ADDR = 0
MAX_STATUS_ADDR = 65535

def set_all_status_off():
    """Function to set all status registers (0-65535) to 'Off' (0)."""
    client = ModbusClient(host=SERVER_HOST, port=SERVER_PORT, auto_open=True)
    try:
        for addr in range(MIN_STATUS_ADDR, MAX_STATUS_ADDR + 1):
            success = client.write_single_register(addr, 0)
            if success:
                print(f"Status at address {addr} set to 'Off'.")
            else:
                print(f"Failed to write to status register at address {addr}.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    set_all_status_off()
