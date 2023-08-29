import subprocess

from logging_settings import logging


def get_phone_udid():
    try:
        command_result = subprocess.run(["adb", "devices"], capture_output=True, text=True)
        output = command_result.stdout.strip()

        lines = output.split('\n')

        if lines[0] == "List of devices attached" and "daemon not running" not in lines[1]:
            udid = lines[1].split()[0]
            return udid

        if lines[0] == "List of devices attached" and "daemon not running" in lines[1]:
            udid = lines[3].split()[0]
            return udid

    except Exception as e:
        logging.error(e)
