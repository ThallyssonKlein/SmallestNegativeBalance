def main(debts):
    result = []

    for i, debt in enumerate(debts, start=0):
        d = debt.split()
        borrower = d[0]
        lender = d[1]
        value = d[2]
        borrowerSum = value

        for i2, debt2 in enumerate(debts, start=1):
            d2 = debt2.split()
            borrower2 = d2[0]
            lender2 = d2[1]
            value2 = d2[2]

            if borrower == borrower2:
                borrowerSum -= value2
            elif borrower == lender2:
                borrowerSum += value2
        
        if borrowerSum < 0:
            result.append(borrower + ' ' + borrowerSum)
        
    return result.sort()

if __name__ == "__main__":
    print(main(['Fulano Siclano 2', 'Siclano Fulano 1']))