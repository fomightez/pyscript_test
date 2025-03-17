from pyscript import display
from datetime import datetime
now = datetime.now()
s = 'Hello world! <br />This is the current date and time, as computed by Python:<br/>'
display(s,now.strftime("%m/%d/%Y, %H:%M:%S"))
