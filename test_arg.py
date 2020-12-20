
import sys

def praise(sb):
	print(f"{sb} is awesome!")

this_module = sys.modules[__name__]
getattr(this_module, sys.argv[1])(*sys.argv[2:])
