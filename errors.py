import sys, warnings

print("this is normal print")
sys.stderr.writelines(["this is an error"])
warnings.warn("this is a warning")