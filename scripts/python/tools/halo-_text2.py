from halo import Halo
from spinners import Spinners

spinner = Halo(text='Such Spins', spinner=Spinners.pong.value)

try:
    spinner.start()
    # Simulate some time-consuming task
    import time
    time.sleep(5)
    spinner.succeed("Task completed!")
except (KeyboardInterrupt, SystemExit):
    spinner.stop()