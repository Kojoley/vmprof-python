import ctypes
import platform
import sys
import struct

print(platform.platform())
print(sys.version)
print("struct.calcsize('Q') == %d" % struct.calcsize('Q'))
print("struct.calcsize('L') == %d" % struct.calcsize('L'))
print("ctypes.sizeof(ctypes.c_long) == %d" % ctypes.sizeof(ctypes.c_long))
