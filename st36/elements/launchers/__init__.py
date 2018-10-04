
def pipeline(*args):
    for func in args:
        if len(func) > 1:
            func[0](*func[1:])
        else:
            func[0]()
