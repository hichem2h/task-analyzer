def main(balance, request):
    if request > balance:
        print("Can't give you all this money !!")

    elif request < 0:
        print("More than zero plz!")

    else:
        balance -= request

        while request > 0:

            if request >= 100:
                request -= 100
                print("give 100")

            elif request >= 50:
                request -= 50
                print("give 50")

            elif request >= 10:
                request -= 10
                print("give 10")

            elif request >= 5:
                request -= 5
                print("give 5")

            elif request < 5:
                print("give " + str(request))
                request = 0

    return locals()