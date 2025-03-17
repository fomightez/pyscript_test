from pyscript import display
from datetime import datetime
now = datetime.now()
s1 = "Hello world!"
s2 = "This is the current date and time, as computed by Python:"
display(s1,s2,now.strftime("%m/%d/%Y, %H:%M:%S"))
