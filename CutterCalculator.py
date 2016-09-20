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
elif CalcType == "RPM":
    IPM = int(input("Please input desired IPM: "))
    WOC = float(input("Please input width of cut at desired depth: "))

    RPM = (IPM * 1000) / (3.14 * WOC)
    print (RPM)
elif CalcType == "SFM":
    RPM = int(input("Please input RPM: "))
    WOC = float(input("Please input width of cut at desired depth: "))

    SFM = WOC * 0.2618 * RPM
    print (SFM)
elif CalcType == "FPT":
    IPM = int(input("Please input desired IPM: "))
    Teeth = int(input("Please input amount of teeth on cutter: "))
    RPM = int(input("Please input RPM: "))

    FPT = IPM / (Teeth * RPM)
    print (FPT)
elif CalcType == "Efficiency comparison":
    IPM1 = int(input("Please input IPM of cutter 1: "))
    DOC1 = float(input("Please input depth of cut of cutter 1: "))

    IPM2 = int(input("Please input IPM of cutter 2: "))
    DOC2 = float(input("Please input depth of cut of cutter 2: "))

    MaterialPerMinute1 = IPM1 * DOC1
    MaterialPerMinute2 = IPM2 * DOC2

    if MaterialPerMinute1 > MaterialPerMinute2:
        Difference = MaterialPerMinute1 - MaterialPerMinute2
        print ("Cutter 1 is more efficient by " + Difference + " cubic inches per minute.")
    elif MaterialPerMinute1 < MaterialPerMinute2:
        Difference = MaterialPerMinute2 - MaterialPerMinute1
        print ("Cutter 2 is more efficient by " + Difference + " cubic inches per minute.")
else:
    print ("That is not a valid choice")
