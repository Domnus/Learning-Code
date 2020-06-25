l1 = input().split(" ")
l2 = input().split(" ")
cdp1, qp1, vp1 = l1
cdp2, qp2, vp2 = l2

valorAPagar = (int(qp1) * float(vp1)) + (int(qp2) * float(vp2))

print("VALOR A PAGAR: R$ %0.2f" %valorAPagar)