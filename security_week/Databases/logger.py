import time

log_file = "security.log"

def monitor_log_file():
    with open(log_file, "r") as file:
        file.seek(0, 2)  # Go to the end of the file
        while True:
            line = file.readline()
            if line:
                # Analyze the log entry
                if "Unauthorized access attempt" in line:
                    # Trigger an alert or perform further actions
                    print("Unauthorized access attempt detected!")
            else:
                time.sleep(1)  # Wait for new log entries

monitor_log_file()


'''
log_file = "security.log"
log_format = "%(asctime)s %(levelname)s %(message)s"

# Log a successful login event
logging.info("User '{}' logged in successfully.".format(username))

# Log an unauthorized access attempt
logging.warning("Unauthorized access attempt by '{}'.".format(username))

# Log an error during authentication
logging.error("Authentication failed for user '{}'.".format(username))

'''