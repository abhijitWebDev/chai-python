def printKwArgs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")
        

print(printKwArgs(name="Shaktiman", power="Lasers", enemy="Dr jackal"))
print(printKwArgs(name="Shaktiman", power="Lasers"))
