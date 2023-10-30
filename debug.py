import ipdb
from lib import *

# Test your code below...

r1 = Role("Juliet")
r2 = Role("Romeo")

a1 = Audition("Jen", "NYC", False, r1 )
a2 = Audition("Jill", "NYC", False, r1)
a3 = Audition("Jim", "Georgia", True, r1)
a4 = Audition("Jennifer", "NYC", False, r2)
a5 = Audition("Jeer", "NYC", True, r2)
a6 = Audition("Jelly", "NYC", True, r2)


# the below line allows us to stop & try stuff!
ipdb.set_trace()
