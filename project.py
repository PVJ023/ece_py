"""
This project was created on 2023-09-08 by Parshwanath V Jain (PVJ)
It is a project in which I seek to combine the electronics and computer science fields on a surface level though they are always intertwined.
Here, is a program which displays a menu when first called, then the user sees the menu and chooses what he wants to find/calculate today!
Though limited in functionality now, I sure hope that the open source contributers on Git can make this better :)

"""

import re
import sys
import argparse
from tabulate import tabulate
import numpy as np
import matplotlib.pyplot as plt
import math


class ElecPy:
    # We start off with the main menu of our system that explains in detail how to utilize this tool
    main_menu = [
        {"I": "command line arg", "W": "Fuction"},
        {
            "I": "--ohm",
            "W": "Takes in 2 parameters and gives the third according to Ohm's Law (enter in 'value_unit' format) all in V,A,O(Ohms) only",
        },
        {
            "I": "--dracurr",
            "W": "Takes in input of Vgs and Vt (respectively) to give the drain current 2 parameters both are float values enter without units",
        },
        {
            "I": "--csamp",
            "W": "Calculates midband gain of CS Amplifier in mid and high freq range, 6 values, in this order: Rg,Rin,gm,ro,Rd,Rl resistance in kohm and gm in mA",
        },
        {
            "I": "--csamp_g",
            "W": "Plots the amplified plot for the given wave and gain in dB along with frequency modulated wave enter Amplitude, gain, freq i V,dB,Hz",
        },
        {
            "I": "--ceamp",
            "W": "Calculates midband gain of CE Amplifier in mid and high freq range, 8 values in order: Rb,Ri,rpi,rx,gm,Rl,Rc,Ro resistance in kohm and gm in mA",
        },
        {
            "I": "--ceamp_g",
            "W": "Plots the amplified plot for the given wave and gain in dB along with frequency modulated wave enter Amplitude, gain, freq i V,dB,Hz",
        },
        {
            "I": "--sample",
            "W": "Plots the sampled version of the given wave enter 0 to activate",
        },
        {
            "I": "--fft",
            "W": "Outputs the fast fourier transform of the given sequence takes 2 inputs sampling rate and freq both float type respectively",
        },
        {
            "I": "",
            "W": "Enter your choice among the above instructions in the command line correctly",
        },
    ]

    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description="A program to help you check basic calculations and formulae of important Basic Electronics quesitons"
        )
        self.parser.add_argument("--ohm", nargs=2, type=str)
        self.parser.add_argument("--dracurr", nargs=2, type=float)
        self.parser.add_argument("--sample", nargs=1, type=int)
        self.parser.add_argument("--csamp", nargs=6, type=float)
        self.parser.add_argument("--ceamp", nargs=8, type=float)
        self.parser.add_argument("--csamp_g", nargs=3, type=float)
        self.parser.add_argument("--ceamp_g", nargs=3, type=float)
        self.parser.add_argument("--fft", nargs=2, type=float)

    def __str__(self):
        return tabulate(self.main_menu, headers="firstrow", tablefmt="rounded_grid")

    def ohm(self, values):
        val = []
        uni = []
        for value in values:
            if matches := re.findall("^([0-9]+.?[0-9]*?)_(V|A|O)$", value):
                for i in range(1):
                    num, unit = matches[i]
                    # print(matches[i])
                    val.append(float(num))
                    if unit not in uni:
                        uni.append(unit)
                    else:
                        sys.exit("Units aren't right!")
        answer = 0
        if not "O" in uni:
            if "V" == uni[0]:
                answer = val[0] / val[1]
            else:
                answer = val[1] / val[0]
            return str(round(answer, 3)) + " ohm"

        if not "V" in uni:
            if "O" == uni[0]:
                answer = val[0] * val[1]
            return str(round(answer, 3)) + " V"
        if not "A" in uni:
            if "V" == uni[0]:
                answer = val[0] / val[1]
            else:
                answer = val[1] / val[0]
            return str(round(answer, 3)) + " A"
        return answer

    def dracurr(self, values):
        k = 1
        ask = input("Is k known? (y/n) ")
        if ask == "y":
            k = float(input("Enter k value: "))
        else:
            un = float(input("Enter un (for unCox w/L):"))
            Cox = float(input("Enter Cox (in uF)(for unCox w/L):"))
            w = float(input("Enter W (for unCox w/L):"))
            l = float(input("Enter L (for unCox w/L):"))
            k = un * Cox * w / l
        try:
            answer = k * ((float(values[0]) - float(values[1])) ** 2)
        except TypeError:
            print("Input isn't float try again!")
            sys.exit()
        return str(round(answer, 3)) + " uA"

    def csamp(self, val):
        rg = val[0]
        rin = val[1]
        gm = val[2]
        ro = val[3]
        rd = val[4]
        rl = val[5]
        ans = (rg / (rg + rin)) * gm * (1 / ((1 / ro) + (1 / rd) + (1 / rl)))
        return str(round(ans, 2)) + " dB"

    def csamp_g(self, val):
        amp = val[0]
        g = val[1]
        f = val[2]
        n = np.linspace(0, 10, 100)
        gain = 10 ** (g / 20)
        x = amp * np.sin(2 * np.pi * f * n)
        plt.subplot(2, 1, 1)
        plt.title("Analog Signal", fontsize=20)
        plt.plot(n, x, linewidth=3, label="expression")
        plt.xlabel("t", fontsize=15)
        plt.ylabel("amplitude", fontsize=15)
        y = amp * gain * np.sin(2 * np.pi * f * n)
        plt.subplot(2, 1, 2)
        plt.title("amplified Signal", fontsize=20)
        plt.plot(n, y, linewidth=3, label="expression")
        plt.xlabel("t", fontsize=15)
        plt.ylabel("amplitude", fontsize=15)
        plt.tight_layout()
        plt.show()
        return "In the graphs"

    def ceamp(self, val):
        rb = val[0]
        ri = val[1]
        rpi = val[2]
        rx = val[3]
        gm = val[4]
        rl = val[5]
        rc = val[6]
        ro = val[7]
        Rl = 1 / ((1 / ro) + (1 / rc) + (1 / rl))
        Rx = gm * Rl * rpi / (rpi + rx + (1 / ((1 / rb) + (1 / ri))))
        ans = 20 * math.log(((rb / (rb + ri)) * Rx), 10)
        return str(abs(round(ans, 2))) + " dB"

    def ceamp_g(self, val):
        amp = val[0]
        g = val[1]
        f = val[2]
        n = np.linspace(0, 10, 100)
        gain = 10 ** (g / 20)
        x = amp * np.sin(2 * np.pi * f * n)
        plt.subplot(2, 1, 1)
        plt.title("Analog Signal", fontsize=20)
        plt.plot(n, x, linewidth=3, label="expression")
        plt.xlabel("t", fontsize=15)
        plt.ylabel("amplitude", fontsize=15)
        y = amp * gain * np.sin(2 * np.pi * f * n)
        plt.subplot(2, 1, 2)
        plt.title("amplified Signal", fontsize=20)
        plt.plot(n, y, linewidth=3, label="expression")
        plt.xlabel("t", fontsize=15)
        plt.ylabel("amplitude", fontsize=15)
        plt.tight_layout()
        plt.show()
        return "In the graphs"

    def sample(self, _):
        signal_list = ["poly", "sin", "cos", "tan", "pow"]
        for i in range(len(signal_list)):
            print(i + 1, signal_list[i])
        signal = input("Which signal do you want to plot? ")
        n = np.linspace(0, 10, 100)
        t = np.arange(0, 100)
        x = 1
        if signal in signal_list:
            match signal:
                case "sin":
                    amp = float(input("Enter amplitude: "))
                    freq = float(input("Enter frequency: "))
                    x = amp * np.sin(2 * np.pi * freq * n)
                case "tan":
                    amp = float(input("Enter amplitude: "))
                    freq = float(input("Enter frequency: "))
                    x = amp * np.tan(2 * np.pi * freq * n)
                case "cos":
                    amp = float(input("Enter amplitude: "))
                    freq = float(input("Enter frequency: "))
                    x = amp * np.cos(2 * np.pi * freq * n)
                case "poly":
                    a = float(input("Enter coeff of x^4: "))
                    b = float(input("Enter coeff of x^3: "))
                    c = float(input("Enter coeff of x^2: "))
                    d = float(input("Enter coeff of x: "))
                    e = float(input("Enter constant: "))
                    x = a * (t**4) + b * (t**3) + c * (t**2) + d * t + e
                case "pow":
                    amp = float(input("Enter amplitude: "))
                    x = amp**t
                case _:
                    print("signal sent isn't recognized!")
        else:
            sys.exit("signal sent isn't recognized!")
        # 1. Plotting Analog Signal
        plt.subplot(2, 1, 1)
        plt.title("Analog Signal", fontsize=20)
        plt.plot(t, x, linewidth=3, label="expression")
        plt.xlabel("t", fontsize=15)
        plt.ylabel("amplitude", fontsize=15)
        # plt.legend(loc='upper right')

        # 2. Sampling and Plotting of Sampled signal
        plt.subplot(2, 1, 2)
        plt.title("Sampling", fontsize=20)
        plt.plot(t, x, linewidth=3)
        n = t

        markerline, stemlines, baseline = plt.stem(x)
        plt.setp(stemlines, "linewidth", 3, label="sampled expression")
        plt.xlabel("n", fontsize=15)
        plt.ylabel("amplitude", fontsize=15)
        # plt.legend(loc='upper right')

        plt.tight_layout()
        plt.show()
        return "In the graphs"

    def fft(self, val):
        # sampling rate
        sr = val[0]
        # sampling interval
        ts = 1.0 / sr
        t = np.arange(0, 1, ts)
        freq = val[1]
        x = 3 * np.sin(2 * np.pi * freq * t)

        X = np.fft.fft(x)
        N = len(X)
        n = np.arange(N)
        T = N / sr
        freq = n / T
        print(X)

        plt.figure(figsize=(12, 6))
        plt.subplot(121)

        plt.stem(freq, np.abs(X), "b", markerfmt=" ", basefmt="-b")
        plt.xlabel("Freq (Hz)")
        plt.ylabel("FFT Amplitude |X(freq)|")
        plt.xlim(0, 10)

        plt.subplot(122)
        plt.plot(t, np.fft.ifft(X), "r")
        plt.xlabel("Time (s)")
        plt.ylabel("Amplitude")
        plt.tight_layout()
        plt.show()
        return "In the graphs"


def value_finder(inp):
    """
    cmd_args = [
        "ohm",
        "dracurr",
        "csamp",
        "csamp_g",
        "ceamp",
        "ceamp_g",
        "sample",
        "fft",
    ]
    """
    keys = list(inp.keys())
    op = "_"
    for key in keys:
        if inp[key]:
            op = key
    values = inp[op]
    a = call_values(values, op)
    ans = print_answer(a)
    return ans


def call_values(values, op):
    e = ElecPy()
    a = 0
    if values:
        match op:
            case "ohm":
                a = e.ohm(values)
            case "dracurr":
                a = e.dracurr(values)
            case "csamp":
                a = e.csamp(values)
            case "csamp_g":
                a = e.csamp_g(values)
            case "ceamp":
                a = e.ceamp(values)
            case "ceamp_g":
                a = e.ceamp_g(values)
            case "sample":
                a = e.sample(values)
            case "fft":
                a = e.fft(values)
            case _:
                return "No argument"
    return a


def print_answer(a):
    return "The final answer is : " + a


"""
Here lies all that the user should do in the code, as their main worklies in the terminal window where they input commands and values
into the function of their choice and get the results.

"""


def main():
    e = ElecPy()
    if len(sys.argv) == 1:
        print(e)
        sys.exit()
    else:
        args = e.parser.parse_args()
        inp = vars(args)
    answer = value_finder(inp)
    print(answer)


if __name__ == "__main__":
    main()
