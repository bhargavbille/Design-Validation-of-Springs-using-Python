def fatigue_load_dia(w,C):
    import math
    MOR = {'1':80000,'2':80000,'3':80000,'4':80000,'5':70000,'6':44000,'7':44000,'8':35000}
    fos = float(input("\tEnter the design Factor of Safety : "))
    Ty = float(input("\tEnter the Yield Shear Stress in MPa or N/mm2 : "))
    Te = float(input("\tEnter the Endurance Shear Stress in Mpa or N/mm2: "))
    G = float(input("\tEnter the value of Modulus of Rigidity in N/mm2: ")) 
    Wm = (w[0] + w[1])/2
    Wv = (w[1] - w[0])/2
    Ks = 1 + 1 / (2*C)
    K = (4 * C - 1) / (4 *  C - 4) + 0.615 / C
    d = ((8*C*fos)/math.pi * ((Ks*Wm)/Ty - (K*Wv)/Ty+(2*K*Wv)/Te)) ** 0.5
    return fos, Ty, Te, G, d 
          
