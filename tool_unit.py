import time


def succeed(msg: str):
    return "<font color='green'>[%s] %s </font>" % (time.strftime("%H:%M:%S", time.localtime()), msg)


def fail(msg: str):
    return "<font color='red'>[%s] %s </font>" % (time.strftime("%H:%M:%S", time.localtime()), msg)


# 检测正负数
def is_natural_num(z):
    try:
        z = float(z)
        return isinstance(z, float)
    except ValueError:
        return False
