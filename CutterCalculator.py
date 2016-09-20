CalcType = "Null"
FPT = 0.0
Teeth = 0
RPM = 0
IPM = 0
WOC = 0.0

CalcType = str(input("What would you like to calculate today?"))
if CalcType == "IPM":
    FPT = float(input("Please input FPT: "))
    Teeth = int(input("Please input amount of teeth on cutter: "))
    RPM = int(input("Please input RPM: "))

    IPM = FPT * Teeth * RPM
    print (IPM)
    return
elif CalcType == "RPM":
    IPM = int(input("Please input desired IPM: "))
    WOC = float(input("Please input width of cut at desired depth: "))

    RPM = (IPM * 1000) / (3.14 * WOC)
    print (RPM)
    return
elif CalcType == "SFM":
    RPM = int(input("Please input RPM: "))
    WOC = float(input("Please input width of cut at desired depth: "))

    SFM = WOC * 0.2618 * RPM
    print (SFM)
    return
elif CalcType == "FPT":
    IPM = int(input("Please input desired IPM: "))
    Teeth = int(input("Please input amount of teeth on cutter: "))
    RPM = int(input("Please input RPM: "))

    FPT = IPM / (Teeth * RPM)
    print (FPT)
    return
else:
    print ("That is not a valid choice")
    return
