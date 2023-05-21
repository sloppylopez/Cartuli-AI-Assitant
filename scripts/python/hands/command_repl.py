import sys
import subprocess


def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if output:
        print(output.decode().strip())
    if error:
        print(error.decode().strip(), file=sys.stderr)


while True:
    try:
        user_input = input(">> ")
        run_command(user_input)
    except KeyboardInterrupt:
        print("\nExiting...")
        break
