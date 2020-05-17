class Open:
    def __enter__(self):
        print("open")

    def __exit__(self, type, value, trace):
        print("close")
 
    def __call__(self):
        pass

with Open() as f:
    pass
# 上下文协议