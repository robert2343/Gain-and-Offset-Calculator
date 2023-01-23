#!/usr/bin/python3
import math

vref = float(input("Enter the voltage level of a stable reference (vref): "))
voutfs = float(input("Enter the full-scale output voltage (voutfs): "))
voutzs = float(input("Enter the zero-scale output voltage (voutzs): "))
vinfs = float(input("Enter the full-scale input voltage (vinfs): "))
vinzs = float(input("Enter the zero-scale input voltage (vinzs):"))

m = (voutfs - voutzs)/(vinfs-vinzs)
b = voutzs - m*vinzs

if m > 0 and b > 0:
    r1 = float(input("Enter R1: "))
    r2 = vref*r1*m/b
    rf = float(input("Enter Rf (may be on datasheet): "))
    print("R1", r1)
    print("R2", r2)
    print("Rf", rf)
    print("See page 3 of the PDF for the schematic.")
    filtering = input("Do you want to add filtering? (y/n) [n]: ") == "y"
    if filtering:
        f0 = float(input("Enter the rolloff frequency: "))
        co = 1/(2*math.pi*r1*f0)
        print("Co", co)
        print("See page 6 of the PDF for the schematic.")
elif m > 0 and b < 0:
    enhancedAccuracy = input("Do you want enhanced accuracy? (y/n) [n]: ") == "y"
    if enhancedAccuracy:
        rf = float(input("Enter Rf (may be on datasheet): "))
        rg = rf/(m - 1)
        vrefprime = abs(b)/m
        r1 = float(print("Enter R1: "))
        r2 = vrefprime * r1/(vref - vrefprime)
        print("Rf", rf)
        print("Rg", rg)
        print("Vref'", vrefprime)
        print("R1", r1)
        print("R2", r2)
        print("See page 4 of the PDF for the schematic.")
        filtering = input("Do you want to add filtering? (y/n) [n]: ") == "y"
        if filtering:
            f0 = float(input("Enter the rolloff frequency: "))
            ro = float(input("Enter a value for Ro: "))
            co = 1/(2*math.pi*ro*f0)
            print("Co", co)
            print("See page 7 of the PDF for the schematic.")
    else:
        rf = float(input("Enter Rf (may be on datasheet): "))
        rg = rf/(m - 1)
        rg2 = rg/10 #possibly supposed to be a chosen value, but it is approx equal to rg/10
        rg1 = rg - rg2
        vrefprime = abs(b) * rg1/(rg1 + rf)
        r1 = rg2 * (vref - vrefprime) / vrefprime
        print("Rf", rf)
        print("Rg", rg)
        print("Rg2", rg2)
        print("Rg1", rg1)
        print("Vref'", vrefprime)
        print("R1", r1)
        print("See page 4 of the PDF for the schematic.")
        filtering = input("Do you want to add filtering? (y/n) [n]: ") == "y"
        if filtering:
            f0 = float(input("Enter the rolloff frequency: "))
            ro = float(input("Enter a value for Ro: "))
            co = 1/(2*math.pi*ro*f0)
            print("Co", co)
            print("See page 7 of the PDF for the schematic.")
elif m < 0 and b > 0:
    rf = float(input("Enter Rf (may be on datasheet): "))
    rg = rf/abs(m)
    r2 = float(input("Enter R2, should be same order as Rf (" + str(rf) + "): "))
    r1 = b*r2*rg/(vref*(rf + rg) - b*rg)
    print("Rf", rf)
    print("Rg", rg)
    print("R2", r2)
    print("R1", r1)
    print("See page 5 of the PDF for the schematic.")
    filtering = input("Do you want to add filtering? (y/n) [n]: ") == "y"
    if filtering:
        f0 = float(input("Enter the rolloff frequency: "))
        co = 1/(2*math.pi*rf*f0)
        print("See page 8 of the PDF for the schematic.")
elif m < 0 and b < 0:
    rf = float(input("Enter Rf (may be on datasheet): "))
    rg1 = rf/abs(m)
    rg2 = vref*rf/abs(b)
    print("Rf", rf)
    print("Rg1", rg1)
    print("Rg2", rg2)
    filtering = input("Do you want to add filtering? (y/n) [n]: ") == "y"
    if filtering:
        f0 = float(input("Enter the rolloff frequency: "))
        cf = 1/(2*math.pi*rf*f0)
        print("See page 8 of the PDF for the schematic.")
else:
    print("Something is equal to 0... m =", m, "b =", b)
