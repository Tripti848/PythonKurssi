while True:
    tuumat = float(input("Anna tuumat (negatiivinen lopettaa): "))

    if tuumat < 0:
       break

    senttimetrit = tuumat * 2.54
    print(senttimetrit)