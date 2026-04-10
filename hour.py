T=int(input())
H_total = int(input())
if H_total < 24 or H_total % 2 != 0 or T >= H_total:
    print("INVALID INPUT")
else:
    found = False
    for D in range(T, 0, -1):
        H = T - D
        if H > 0:
            remaining = H_total - (D * 24)
            if remaining > 0 and remaining % H == 0:
                unit_size = remaining // H

                if unit_size == 18:
                    print("D = " + str(D) + ", H = " + str(H))
                    found = True
                    break

       if not found:
        for D in range(T, 0, -1):
            H = T - D
            if H > 0:
                remaining = H_total - (D * 24)
                if remaining > 0 and remaining % H == 0:
                    print("D = " + str(D) + ", H = " + str(H))
                    found = True
                    break

    if not found:
        print("INVALID INPUT")
