# dumps every attribute of an object to the console
# obj = object you want to dump
# magic = True if you want to output "magic" attributes (like __init__, ...) too
def dump(obj, magic = False):
    for attr in dir(obj):
        if magic is True:
            print("obj.%s = %s" % (attr, getattr(obj, attr)))
        else:
            if not attr.startswith('__'):
                print("obj.%s = %s" % (attr, getattr(obj, attr)))