import sys

sys.path.append(r'C:\Users\Parth\Documents\GitHub\TMRemote\scripts')
try:
    import TMRLogger_old as TMR
except:
    print('> Logger: Could not import TMRLogger')

TMR.Log()
