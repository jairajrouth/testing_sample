class JackPot:
    def sum_jack_pot(x, y):
        if(x + y) >= 1:
            # Correct is x - y
            # print("Yes")
            return (x - y) * 2
        else:
            # print("No")
            return x + y


if __name__ == "__main__":
    JackPot.sum_jack_pot(2, 5)


#mut.py --target SampleProg.py --unit-test tests\test_SampleProg.py -m --report-html DIR_NAME
#mut.py --target src\SampleProg.py --unit-test tests\test_SampleProg.py -m
#C:\Users\jaira\AppData\Local\Programs\Python\Python39\mutpy\bin
#For src not found error. Use "python3 -m" before pytest command