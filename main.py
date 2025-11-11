def greet(Name=None):
    if Name:
        return f"Hello {Name},from main"
    return "Hello from Main!"

if __name__=="__main__":
    print(greet("Vinay"))