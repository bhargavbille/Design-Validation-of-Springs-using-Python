import math
import sys 
from sys import exit
from math import ceil
import sys 
import os
from sys import exit
Shear_Stress = {1:{1:420,2:525,3:651},2:{1:392,2:490,3:612},3:{1:336,2:420,3:525},
                4:{1:280,2:350,3:437.5},5:{1:280,2:350,3:437.5},6:{1:196,2:245,3:306},7:{1:196,2:245,3:306},8:{1:140,2:175,3:219}}
mat = {1:'Carbon Steel',2:'Music Wire',3:'Oil Temperd Wire',4:'Hard-drawn Spring Wire',5:'Stainless-steel Wire',6:'Monel Metal',7:'Phospor Bronze',8:'Brass'}
ser = {1:'Severe Service',2:'Average Service',3:'Light Service'}
MOR = {1:80000,2:80000,3:80000,4:80000,5:70000,6:44000,7:44000,8:35000}
z = [0.0711, 0.0813, 0.0914, 0.1016, 0.1118, 0.1219, 0.1321, 0.1524, 0.1727, 0.193, 0.2134, 0.2337, 0.254,
         0.2743, 0.2946, 0.315, 0.3454, 0.3759, 0.4166, 0.457, 0.508, 0.559, 0.61, 0.711, 0.813, 0.914, 1.016,
         1.219, 1.422, 1.626, 1.829, 2.032, 2.337, 2.642, 2.946, 3.251, 3.658, 4.064, 4.47, 4.877, 5.385, 5.893,
         6.401, 7.01, 7.62, 8.229, 8.839, 9.49, 10.16, 10.973, 11.785, 12.7]
SWGno = {12.700:'7/0',11.785:'6/0',10.973:'5/0',10.160:'4/0',9.490:'3/0',8.839:'2/0',8.229:'0',7.620:'1',7.010:'2',6.401:'3',
         5.893:'4',5.385:'5',4.877:'6',4.470:'7',4.064:'8',3.658:'9',3.251:'10',2.946:'11',2.642:'12',2.337:'13',2.032:'14',
         1.829:'15',1.626:'16',1.422:'17',1.219:'18',1.016:'19',0.914:'20',0.813:'21',0.711:'22',0.610:'23',0.559:'24',0.508:'25',
         0.457:'26',0.4166:'27',0.3759:'28',0.3454:'29',0.3150:'30',0.2946:'31',0.2743:'32',0.2540:'33',0.2337:'34',0.2134:'35',0.1930:'36',
            0.1727:'37',0.1524:'38',0.1321:'39',0.1219:'40',0.1118:'41',0.1016:'42',0.0914:'43',0.0813:'44',0.0711:'45'}
no_of_turns = {'1':0,'2':0,'3':2,'4':2}
end = {'1':'Plain Ends','2':'Ground Ends','3':'Squared Ends','4':'Squared and Ground Ends'}
load = input("1.'Designing of Helical Springs'\n\tEnter the type of load i.e. static/fatigue : ")
if load != "static" and load != "fatigue":
    print("Sorry Wrong Option Try Again !!!!!!!")
    import design_of_springs
    sys.exit()
w = list(map(float,input("\tEnter the load range (i.e. A-B)in N : ").split("-")))
x = (w[0] - w[1]) if w[0] > w[1] else (w[1] - w[0])
dif = float(input("\tEnter the deflection of the spring in mm: "))
C = float(input("\tEnter the Spring Index: "))
ends = input("\tSelect the type of ends,\n\t1. Plain Ends\n\t2. Ground Ends\n\t3. Squared Ends\n\t4. Squared and Grounded Ends\n\t...........: ")
nds = end[ends]
if load == 'static':
    xl = [['Type of Spring','Type of Load','Load     (N)','Diflection   (m)','Spring Constant','Material','Service','Type of Ends','Modulus of Rigidity     (N/mm2)','Shear Stress    N/mm2',
       'Wire Diameter  (mm)','No. of active Coils','Total Coils','Free Length    (mm)','Solid Length    (mm)','Pitch     (mm)']]
    if input("\tDo you know the values of Shear Stress and Modulus of \n\trigidity? (yes/no) : ")== 'yes':
        G = float(input("\tThen enter the value of Modulus of Rigidity in N/mm2: "))
        xxx = G
        t = float(input("\tEnter the value of Shear Stress in MPa or N/mm2: "))
        material = '-----'
        service = '-----'
        d = ((((max(w) * 8 * C) / (math.pi * t)) ** 0.5))
        xx = d
        y = x        
        if d <= 12.7:
            for i in range(len(z)):
                 if z[i] > d:
                     d = z[i]
                     print("\n\tResult:..................................................,\n\tFrom SWG %s,the wire diameter is (d) = %.3f mm" %(SWGno[d],d))  
                     break
        else:
            d = ceil(d)
            while(1):
                if d%2 == 0 or d%5 == 0:
                    d = d
                    break
                else:
                    d = +1
                    print("\n\tResult:..................................................,\n\tThe Diamter of wire (d) = %.2f mm" %(d))
        D = C * d
        Do = D + d
        Di = D - d
        n = ceil((dif * G * d)/(8 * y * (C ** 3)))
        n1 = n + no_of_turns[ends]
        maxdif = (dif * max(w))/ x
        if ends == 1:
            xyz = n1+2
            free_length = round(xyz * d + (0.15 * maxdif) + maxdif,3)
        else:
            free_length = round(n1 * d + (0.15 * maxdif) + maxdif,3)
        solid_length = round(d * n1,3)
        pitch = round(free_length/(n1 - 1),3)        
        xm = []
        xm.extend(('Helical',load,max(w),dif,C,material,service,nds,G,t,d,n,n1,free_length,solid_length,pitch))
        xl.append(xm)
        for i in range(9):
            if i == 0:      
                print("\tMean Diameter of Spring Coil (D) = %.2f mm\n\tOuter Diamter of Spring Coil (Do) = %.2f mm\n\tInner Diameter of Spring Coil (Di) = %.2f mm" %(D,Do,Di))
                print("\tFor %s the total No. of Coils(n)= %d\n\tTotal no. of. Active Coils (n1) = %d\n\tMax Compression under the load %.2f N = %.2f mm" %(end[ends],n1,n,max(w),maxdif))
                print("\tFree length of the Spring (Lf) = %.2f mm\n\tSolid Length of the Spring (Ls) = %.2f mm\n\tPitch of the Coil (p) = %.2f mm" %(free_length,solid_length,pitch))
            else:
                material = mat[i]
                for j in range(1,4):
                    service = ser[j]
                    G = MOR[i]
                    t = Shear_Stress[i][j]
                    d = round(((max(w) * 8 * C) / (math.pi * t)) ** 0.5)
                    y = x
                    if d <= 12.7:
                        for k in range(len(z)):
                             if z[k] > d:
                                 d = z[k]
                                 break
                    else:
                        d = ceil(d)
                        while(1):
                            if d%2 == 0 or d%5 == 0:
                                d = d
                                break
                            else:
                                d += 1
                    D = C * d
                    Do = D + d
                    Di = D - d
                    n = ceil((dif * G * d)/(8 * y * (C ** 3)))
                    n1 = n + no_of_turns[ends]
                    maxdif = (dif * max(w))/ x
                    if ends == 1:
                        xyz = n1+2
                        free_length = round(xyz * d + (0.15 * maxdif) + maxdif,3)
                    else:
                        free_length = round(n1 * d + (0.15 * maxdif) + maxdif,3)
                    solid_length = round(d * n1,3)
                    pitch = round(free_length/(n1 - 1),3)
                    xm = []
                    xm.extend(('Helical',load,max(w),dif,C,material,service,nds,G,t,d,n,n1,free_length,solid_length,pitch))       
                    xl.append(xm)
        d = xx
        G = xxx
        D = C * d
        Do = D + d
        Di = D - d
        n = ceil((dif * G * d)/(8 * y * (C ** 3)))
        n1 = n + no_of_turns[ends]
        maxdif = (dif * max(w))/ x
        if ends == '1' :
            xyz = n1+2
            free_length = round(xyz * d + (0.15 * maxdif) + maxdif,3)
        else:
            free_length = round(n1 * d + (0.15 * maxdif) + maxdif,3)
        solid_length = (d * n1)
        pitch = (free_length/(n1 - 1))
        print("\n\tResult:...............original...................................,\n\tthe wire diameter is (d) = %.3f mm" %d)
        print("\tMean Diameter of Spring Coil (D) = %.2f mm\n\tOuter Diamter of Spring Coil (Do) = %.2f mm\n\tInner Diameter of Spring Coil (Di) = %.2f mm" %(D,Do,Di))
        print("\tFor %s the total No. of Coils (n)= %d\n\tTotal no. of. Active Coils (n1) = %d\n\tMax Compression under the load %.2f N = %.2f mm" %(end[ends],n1,n,max(w),maxdif))
        print("\tFree length of the Spring (Lf) = %.2f mm\n\tSolid Length of the Spring (Ls) = %.2f mm\n\tPitch of the Coil (p) = %.2f mm" %(free_length,solid_length,pitch))
        import xlsxwriter
        import uuid
        uf = str(uuid.uuid4())
        ug = uf+'.xlsx'
        workbook = xlsxwriter.Workbook(uf+'.xlsx')
        worksheet = workbook.add_worksheet()
        bold = workbook.add_format({'bold':1})
        format = workbook.add_format()
        format.set_font_size(15)
        for a in range(len(xl)):
            for b in range(len(xl[a])):
                if a == 0:
                    xy = bold
                else:
                    xy = format
                worksheet.set_column(a,b,30)
                worksheet.write(a,b, xl[a][b], xy)  
        workbook.close()
    else:
        matl = int(input("\tThen select the Material,\n\t1. Carbon Steel\n\t2. Music Wire\n\t3. Oil Temperd Wire\n\t4. Hard-drawn Spring Wire\n\t5. Stainless-steel Wire\n\t6. Monel Metal\n\t7. Phospor Bronze\n\t8. Brass\n\t..........: "))
        srvice = int(input("\tSelect the type of service where you use,\n\t1. Severe Service\n\t2. Average Service\n\t3. Light Service\n\t..........: "))
        G = MOR[matl]
        t = Shear_Stress[matl][srvice]
        material = mat[matl]
        service = ser[srvice]
        d = (((max(w) * 8 * C) / (math.pi * t)) ** 0.5)
        xx = d
        y = x
        if d <= 12.7:
            for i in range(len(z)):
                 if z[i] > d:
                     d = z[i]
                     print("\n\tResult:..................................................,\n\tFrom SWG %s,the wire diameter is (d) = %.3f mm" %(SWGno[d],d))  
                     break
        else:
            d = ceil(d)
            while(1):
                if d%2 == 0 or d%5 == 0:
                    d = d
                    break
                else:
                    d = +1
                    print("\n\tResult:..................................................,\n\tThe Diamter of wire (d) = %.2f mm" %(d))
        D = C * d
        Do = D + d
        Di = D - d
        n = ceil((dif * G * d)/(8 * y * (C ** 3)))
        n1 = n + no_of_turns[ends]
        maxdif = (dif * max(w))/ x
        if ends == 1:
            xyz = n1+2
            free_length = round(xyz * d + (0.15 * maxdif) + maxdif,3)
        else:
            free_length = round(n1 * d + (0.15 * maxdif) + maxdif,3)
        solid_length = round(d * n1,3)
        pitch = round(free_length/(n1 - 1),3)
        xm = []
        xm.extend(('Helical',load,max(w),dif,C,material,service,nds,G,t,d,n,n1,free_length,solid_length,pitch))
        xl.append(xm)
        for i in range(9):
            if i == 0 :      
                print("\tMean Diameter of Spring Coil (D) = %.2f mm\n\tOuter Diamter of Spring Coil (Do) = %.2f mm\n\tInner Diameter of Spring Coil (Di) = %.2f mm" %(D,Do,Di))
                print("\tFor %s the total No. of Coils (n)= %d\n\tTotal no. of. Active Coils (n1) = %d\n\tMax Compression under the load %.2f N = %.2f mm" %(end[ends],n1,n,max(w),maxdif))
                print("\tFree length of the Spring (Lf) = %.2f mm\n\tSolid Length of the Spring (Ls) = %.2f mm\n\tPitch of the Coil (p) = %.2f mm" %(free_length,solid_length,pitch))
            elif i != matl:
                material = mat[i]
                service = ser[srvice]
                G = MOR[i]
                t = Shear_Stress[i][srvice]
                d = (((max(w) * 8 * C) / (math.pi * t)) ** 0.5)
                y = x
                if d <= 12.7:
                    for k in range(len(z)):
                         if z[k] > d:
                             d = z[k]
                             break
                else:
                    d = ceil(d)
                    while(1):
                        if d%2 == 0 or d%5 == 0:
                            d = d
                            break
                        else:
                            d += 1
                D = C * d
                Do = D + d
                Di = D - d
                n = ceil((dif * G * d)/(8 * y * (C ** 3)))
                n1 = n + no_of_turns[ends]
                maxdif = (dif * max(w))/ x
                if ends == 1:
                    xyz = n1+2
                    free_length = round(xyz * d + (0.15 * maxdif) + maxdif,3)
                else:
                    free_length = round(n1 * d + (0.15 * maxdif) + maxdif,3)
                solid_length = round(d * n1,3)
                pitch = round(free_length/(n1 - 1),3)
                xm = []
                xm.extend(('Helical',load,max(w),dif,C,material,service,nds,G,t,d,n,n1,free_length,solid_length,pitch))
                xl.append(xm)
        d = xx
        D = C * d
        Do = D + d
        Di = D - d
        n = ceil((dif * G * d)/(8 * y * (C ** 3)))
        n1 = n + no_of_turns[ends]
        maxdif = (dif * max(w))/ x
        if ends == 1:
            xyz = n1+2
            free_length = round(xyz * d + (0.15 * maxdif) + maxdif,3)
        else:
            free_length = round(n1 * d + (0.15 * maxdif) + maxdif,3)
        solid_length = (d * n1,3)
        pitch = (free_length/(n1 - 1))
        print("\n\tResult:...............original...................................,\n\tthe wire diameter is (d) = %.3f mm" %d)
        print("\tMean Diameter of Spring Coil (D) = %.2f mm\n\tOuter Diamter of Spring Coil (Do) = %.2f mm\n\tInner Diameter of Spring Coil (Di) = %.2f mm" %(D,Do,Di))
        print("\tFor %s the total No. of Coils (n)= %d\n\tTotal no. of. Active Coils (n1) = %d\n\tMax Compression under the load %.2f N = %.2f mm" %(end[ends],n1,n,max(w),maxdif))
        print("\tFree length of the Spring (Lf) = %.2f mm\n\tSolid Length of the Spring (Ls) = %.2f mm\n\tPitch of the Coil (p) = %.2f mm" %(free_length,solid_length,pitch))
        import xlsxwriter
        import uuid
        uf = str(uuid.uuid4())
        ug = uf+'.xlsx'
        workbook = xlsxwriter.Workbook(uf+'.xlsx')
        worksheet = workbook.add_worksheet()
        bold = workbook.add_format({'bold':1})
        format = workbook.add_format()
        format.set_font_size(15)
        for a in range(len(xl)):
            for b in range(len(xl[a])):
                if a == 0:
                    xy = bold
                else:
                    xy = format
                worksheet.set_column(a,b,30)
                worksheet.write(a,b, xl[a][b], xy)
        workbook.close()
    print("Please check the '%s' file in the following directory"%(ug))
    print(os.getcwd())
    if (input("\nIf u want to open the \"%s\" file automatically then press 's' : " %(ug)) == 's'):
        file = ug
        os.startfile(file)
elif load == 'fatigue':
    xl = [['Type of Spring','Type of Load','Load     (N)','Diflection   (mm)','Spring Constant','Material','Service','Type of Ends','Factor of Safety','Yield Shear Stress    N/mm2','Endurance Shear Stress   (N/mm2)','Modulus of Rigidity     (N/mm2)',
       'Wire Diameter  (mm)','Active Coils','No. of Coils','Free Length    (mm)','Solid Length    (mm)','Pitch     (mm)']]
    from helical_fat import fatigue_load_dia
    fos, yss, ess, G, d = fatigue_load_dia(sorted(w),C)
    y = max(w)
    d = round(d,3)
    if d <= 12.7:
        for i in range(len(z)):
            if z[i] > d:
                d = z[i]
                print("\n\tResult:..................................................,\n\tFrom SWG %s,the wire diameter is (d) = %.3f mm" %(SWGno[d],d))
                break
    else:
        d = ceil(d)
        while(1):
            if d%2 == 0 or d%5 == 0:
                d = d
                break
            else:
                d += 1
                print("\n\tResult:..................................................,\n\tThe Diamter of wire (d) = %.2f mm" %(d))
    D = C * d
    Do = D + d
    Di = D - d
    n = ceil((dif * G * d)/(8 * y * (C ** 3)))
    n1 = n + no_of_turns[ends]
    maxdif = (dif * max(w))/ x
    if ends == 1:
            xyz = n1+2
            free_length = round(xyz * d + (0.15 * maxdif) + maxdif,3)
    else:
            free_length = round(n1 * d + (0.15 * maxdif) + maxdif,3)
    solid_length = round(d * n1,3)
    pitch = round(free_length/(n1 - 1),3)
    xm = []
    xm.extend(('Helical',load,max(w),dif,C,'---------','----------',nds,fos,yss,ess,G,d,n,n1,free_length,solid_length,pitch))
    xl.append(xm)
    print("\tMean Diameter of Spring Coil (D) = %.2f mm\n\tOuter Diamter of Spring Coil (Do) = %.2f mm\n\tInner Diameter of Spring Coil (Di) = %.2f mm" %(D,Do,Di))
    print("\tFor %s the total No. of Active Coils (n)= %d\n\tTotal No. of Coils (n1) = %d\n\tMax Compression under the load %.2f N = %.2f mm" %(end[ends],n,n1,max(w),maxdif))
    print("\tFree length of the Spring (Lf) = %.2f mm\n\tSolid Length of the Spring (Ls) = %.2f mm\n\tPitch of the Coil (p) = %.2f mm" %(free_length,solid_length,pitch))
    import xlsxwriter
    import uuid
    uf = str(uuid.uuid4())
    ug = uf+'.xlsx'
    workbook = xlsxwriter.Workbook(uf+'.xlsx')
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold':1})
    format = workbook.add_format()
    format.set_font_size(15)
    for a in range(len(xl)):
        for b in range(len(xl[a])):
            if a == 0:
                xy = bold
            else:
                xy = format
            worksheet.set_column(a,b,30)
            worksheet.write(a,b, xl[a][b], xy)
    workbook.close()
    print("Please once check the '%s' file in the following directory,"%(ug))
    print(os.getcwd())
    if (input("\nIf u want to open the \"%s\" file automatically then press 's' : " %(ug)) == 's'):
        file = ug
        os.startfile(file)


    
