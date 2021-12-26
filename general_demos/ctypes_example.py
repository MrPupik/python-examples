from ctypes import c_int, c_char, c_bool, cdll
cdll.LoadLibrary()
c_print = lib_c.printf
