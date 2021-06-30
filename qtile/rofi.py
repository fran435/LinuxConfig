import subprocess

def rofi(options, name):

    sp = subprocess.Popen("echo '{0}' | rofi -dmenu -p '{1}'".format(options, name),
            shell = True,
            stdout=subprocess.PIPE,
            universal_newlines=True)

    rc = sp.wait()
    select = sp.communicate()
    return select[0]
