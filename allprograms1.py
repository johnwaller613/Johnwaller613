def all_programs():
    a = input("enter program. available programs are calculator, temp, jewish weights, length, m2km, km2m\n").lower()
    def calculator():
        c = "default"
        while c == "default" or c == "yes" or c == "y":
            if c == "yes" or c == "y":
                a = result
            else:
                a = 1
                operator = ""
                b = 2
                ina = input("enter first number\n")
                try: a = int(ina)
                except ValueError:
                    try: a = float(ina)
                    except ValueError:
                        print("invalid. only numbers allowed")
                        calculator()
                        return
            operator = input("enter operator\n")
            inb = input("enter next number\n")
            try: b = int(inb)
            except ValueError:
                try: b = float(inb)
                except ValueError:
                    print("invalid. numbers only here")
                    calculator()
                    return
            if operator == '+':
                result = a + b
            elif operator == '-':
                result = a - b
            elif operator == '*':
                result = a * b
            elif operator == '**':
                result = a ** b
            elif operator == "%":
                result = a % b
            elif operator == '/' or operator == '÷':
                result = a / b
            else:
                print('bad equation. enter number followed by comma and then + - *(for times) or /(for ÷) followed by comma and then the last numb. example: calc(2, \'*\', 3)')
                return
            print("\n", result)
            c = input("would you like to continue the equation? enter yes or no:\n")

        
    def length():
        ina = input("enter number\n")
        try: a = int(ina)
        except ValueError:
            try: a = float(ina)
            except ValueError:
                print("invalid. only numbers allowed here")
                length()
                return
        b = input("enter length type\n").lower()
        if b in ("in", "inch", "inches"):
            print(f"{a} in = {a * 2.54} cm, {a * 0.0254} m, {a / 12} ft, {a / 36} yd, {a * 0.0000254} km, {a / 63360} mile")
        elif b in ("cm", "centimeter", "centimeters"):
            print(f"{a} cm = {a / 2.54} in, {a / 100} m, {a / 30.48} ft, {a / 91.44} yd, {a / 100000} km, {a / 160934} mile")
        elif b in ("m", "meter", "meters"):
            print(f"{a} m = {a * 100} cm, {a * 39.37} in, {a * 3.2808} ft, {a * 1.0936} yd, {a / 1000} km, {a / 1609.34} mile")
        elif b in ("ft", "feet", "foot"):
            print(f"{a} ft = {a * 30.48} cm, {a * 12} in, {a * 0.3048} m, {a / 3} yd, {a / 3280.84} km, {a / 5280} mile")
        elif b in ("yd", "yard", "yards"):
            print(f"{a} yd = {a * 91.44} cm, {a * 36} in, {a * 3} ft, {a * 0.9144} m, {a / 1093.61} km, {a / 1760} mile")
        elif b in ("km", "kilometer", "kilometers"):
            print(f"{a} km = {a * 100000} cm, {a * 1000} m, {a * 39370.1} in, {a * 3280.84} ft, {a * 1093.61} yd, {a / 1.60934} mile")
        elif b == "mile" or b == "miles":
            print(f"{a} mile = {a * 160934} cm, {a * 1609.34} m, {a * 63360} in, {a * 5280} ft, {a * 1760} yd, {a * 1.60934} km")
        else:
            print("Invalid unit. write a number followed by a comma followed by a unit in quotes. acceptible units are cm, in, ft, yd, m, km, mile.")
    
    def m2km():
        ina = input("enter number\n")
        try: a = int(ina)
        except ValueError:
            try: a = float(ina)
            except ValueError:
                print("invalid. only numbers allowed here")
                m2km()
                return
        print(f"{a} miles is {a * 1.60934} km")
    def km2m():
        ina = input("enter number\n")
        try: a = int(ina)
        except ValueError:
            try: a = float(ina)
            except ValueError:
                print("invalid. number only here!")
                km2m()
                return
        print(f"{a} km is {a * 0.621371} miles")
    
    def temp():
        ina = input("enter number\n")
        try: a = int(ina)
        except ValueError:
            try: a = float(ina)
            except ValueError:
                print("invalid. numbers only here")
                temp()
                return
        b = input("enter f or c what your converting from\n").lower()
        c = (a - 32) * 5/9
        f = (a * 9/5) + 32
        if b == 'f':
            print(f"{a} °f is {c} °c")
        elif b == 'c':
            print(f"{a} °c is {f} °f")
    
    def jewishWeights():
        ina = input("enter number\n")
        try: a = int(ina)
        except ValueError:
            try: a = float(ina)
            except ValueError:
                print("invalid. only numbers here!")
                jewishWeights()
                return
        b = input("enter weight type\n").lower()
        if b in ('eifah', "eifa", "eifuh"):
            print(f' {a} eifah = {a * 3} saah, {a * 18} kav, {a * 72} lug, {a * 432} beitza.')
        elif b in ("saah", "sa'ah", "sah"):
            print(f' {a} saah = {a / 3} eifah, {a * 6} kav, {a * 24} lug, {a * 144} beitza.')
        elif b == 'kav' or b == "kov":
            print(f' {a} kav = {a / 18} eifah, {a / 6} saah, {a * 4} lug, {a * 24} beitza.')
        elif b == 'lug':
            print(f' {a} lug = {a / 72} eifah, {a / 24} saah, {a / 4} kav, {a * 6} beitza.')
        elif b in ('beitza', "beitsa", "beitzah", "beitsah"):
            print(f' {a} beitza = {a / 432} eifah, {a / 144} saah, {a / 24} kav, {a / 6} lug')
        else:
            print('invalid operator. valid operators are eifah saah kav lug beitza.')


    if a == "calculator" or a == "calc": calculator()
    elif a == "length": length()
    elif a == "temp" or a == "temperature": temp()
    elif a in ("jewishweights", "jewish weights"):
        jewishWeights()
    elif a in ("m2km", "m-km", "miletokm", "mtokm", "m/km", "mile2km"): m2km()
    elif a in ("km2m", "km-m", "km2mile", "km/m"):
        km2m()
    elif a == "": return
    else: print("wrong program")
    b = input("do you want to continue and start a new program? type y for yes otherwise type n or just leave program\n")
    if b == "y": all_programs()
    else: print("thanks for participating and trying out the safelock/filterflex test apps!\n")
all_programs()