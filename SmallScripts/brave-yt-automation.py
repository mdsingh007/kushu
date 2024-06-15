import subprocess
import time
import psutil
import random

def run_and_kill(command, timeout):
  """
  Runs a command-line process and kills it after a specified timeout.

  Args:
      command: The command string to execute.
      timeout: The time in seconds to wait before killing the process.
  """
  process = subprocess.Popen(command)

  def kill_descendants(parent_pid):
      try:
          parent = psutil.Process(parent_pid)
          children = parent.children(recursive=True)
          for child in children:
              child.kill()
          parent.kill()
      except psutil.NoSuchProcess:
          return

  try:
    # Wait for the specified time
    time.sleep(timeout)
  except KeyboardInterrupt:
    print("Exiting due to keyboard interrupt.")
    pass
  finally:
    # Kill the process and its descendants 
    kill_descendants(process.pid)

if __name__ == "__main__":
  # Replace "your_command" with the actual command you want to run
  command = r'"C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe" --incornito --tor https://youtu.be/pXw2n__tP8E?feature=shared'
  # Set the desired timeout in seconds
  timeout = 200 + random.choice(range(70))

  # Run the command and kill it after timeout
  i = 0
  while i < 100:
    print (i, timeout)
    run_and_kill(command, timeout)

  print("Process killed successfully.")


# https://youtu.be/pXw2n__tP8E?feature=shared
# https://youtube.com/watch?v=BilyJF8d2pY&feature=shared
  