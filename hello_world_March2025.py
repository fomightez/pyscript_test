from pyscript import display
from datetime import datetime
now = datetime.now()
s = 'Hello world!\n\nThis is the current date and time, as computed by Python:\n'
display(s,now.strftime("%m/%d/%Y, %H:%M:%S"))
