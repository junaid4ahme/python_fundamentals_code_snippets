# write a program that will take annual salary and return monthly salary with deductions

a_sal_ctc = int(input("What is your CTC    : "))

m_sal_ctc = a_sal_ctc / 12

def deductions(x):
    if x < 500000:
        x = 0
    elif x < 1000000:
        x = x * 0.12
    else:
        x = x * 0.25
    return x

taxable = deductions(a_sal_ctc)

a_sal_inhand = a_sal_ctc - taxable

m_sal_inhand = int(a_sal_inhand / 12)


print("Your total CTC is :{}. \
\nYou monthly ctc is :{}. \n\
Your inhand Yearly component is :{}. \n\
Your deductions are :{}.\
Your Monthly inhand component is :{}"\
    .format(a_sal_ctc, m_sal_ctc, a_sal_inhand, taxable, m_sal_inhand))

