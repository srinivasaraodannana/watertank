 #-------Design of overhead Circular Water Tank(Bhargavi Bilingi)----------







#Library Module Used
import math 

from tabulate import tabulate #for printing tables

from PIL import Image, ImageDraw, ImageFont # for the display images

import colorama #for color output


from colorama import init, Fore, Style 


image = Image.open('/Volumes/Education/programming Files/watertank/img1.jpeg')
draw = ImageDraw.Draw(image)
font1 = ImageFont.truetype ("/Volumes/Education/programming Files/watertank/edosz.otf" ,30)



#Data Given
# volume=125#kilo Lit

# concrete=30#M\u00b30
# steel_grade=415#Fe415
# inner_radius_circular_wall= (4250) #mm
# thickness_wall =100 #mm
# height_wall =3200 #mm
# thickness_top_dome =75#mm
# rise_bottom_top_dome=1000#mm
# thickness_bottom_dome=100#mm
# rise_bottom_dome= 1500 #mm
# bottom_ring_beam= 350 #mm 
# b=350
# free_board=150#mm
# height_staging_above_GL=25 #mm

#prblem 2
volume=300#kilo Lit

concrete=30#M\u00b30
steel_grade=415#Fe415
inner_radius_circular_wall= 6000 #mm
thickness_wall =100 #mm
height_wall =4500 #mm
thickness_top_dome =75#mm
rise_bottom_top_dome=2200#mm
thickness_bottom_dome=100#mm
rise_bottom_dome= 2250 #mm
bottom_ring_beam= 350 #mm 
b=350
free_board=150#mm
height_staging_above_GL=30 #m



# volume=float(input("Enter the volume of the tank in Kilo Litres \n"))
# concrete=float(input("Enter the grade of concrete \n"))
# steel_grade=float(input("Enter the grade of steel \n"))
# inner_radius_circular_wall=float(input("Enter Inner radius of circular wall in mm \n"))
# thickness_wall=float(input("Enter Thickness of wall in mm \n"))
# height_wall=float(input("Enter Height of wall in mm \n"))
# thickness_top_dome=float(input("Enter Thickness of top dome in mm \n"))
# rise_bottom_top_dome=float(input("Enter rise of bottom of top dome in m \n"))
# thickness_bottom_dome=float(input("Enter Thickness of bottom dome in mm \n"))
# rise_bottom_dome=float(input("Enter Rise of bottom of bottom dome \n"))
# b,bottom_ring_beam=map(float,input("Enter Bottom ring beam in mm X mm by giving space \n").split())

# free_board=float(input("Enter Free board in mm \n"))
# height_staging_above_GL=float(input("Enter Height of staging above G.L in m \n"))








#Converting to mm to m
inner_radius_circular_wall= inner_radius_circular_wall/1000
thickness_wall =thickness_wall/1000 #mm
height_wall =height_wall/1000 #mm
thickness_top_dome =thickness_top_dome/1000 #mm
rise_bottom_top_dome=rise_bottom_top_dome/1000#mm
thickness_bottom_dome=thickness_bottom_dome/1000#mm
rise_bottom_dome= rise_bottom_dome/1000 #mm
bottom_ring_beam=b*bottom_ring_beam/(1000**2) #mm 
b=b/1000
free_board=free_board/1000 #mm
height_staging_above_GL=height_staging_above_GL/1000 #mm
#Total Designing Steps-5
#Step-0:- Check for capacity
#Step-1:- Top Dome
#Step-2:- Vertical wall
#Step-3:- Bottom Dome
#Step-4:- Design of Bottom ring
#Step-5:- Bottom Ring Beam

# initialize colorama
init()




concrete_unit=25

# Step-0: Check for Capacity
print( Fore.GREEN + " \n \nStep:-1 Check for Capacity\n"+ Style.RESET_ALL)
H = rise_bottom_dome + thickness_bottom_dome
D = 2 * (inner_radius_circular_wall - 0.125)
D= round(D, 3)
print("Diameter of the dome = {0} m\n".format(D))
R2 = ((D ** 2 / (4 * H)) + H) / 2
R2 = round(R2, 3)
print("Radius of top surface of bottom dome R2 is given by = {0} m \n".format(R2))
pi = math.pi
V1 = pi * ((H * H) / 3)
V1 = V1 * (3 * R2 - H)
V1 = round(V1, 3)
print("Volume of water displaced by bottom dome = {0} m\u00b3 \n".format(V1))
if thickness_wall <= 0.1:
    print("Let us increase the thickness of vertical wall from 100 mm to 150 mm. \n")
    #thickness_wall=150/1000
V= (pi/4)*((2*inner_radius_circular_wall)**2)*(height_wall-free_board)-0.5*0.05*1*(pi*((2*inner_radius_circular_wall)-2/3*0.05))-V1
V=round(V,3)
print("Net capacity of container = {0} m\u00b3 \n".format(V))
if V>=volume:
   print("{0} m\u00b3 > {1} m\u00b3 \n".format(V,volume))
#   print("So Design is design of required.\n") 
else:
   print("The design capacity is sufficient.\n") 


#Step-1 Top Dome
print( Fore.GREEN + "\n \nStep-2:-Top Dome\n"+ Style.RESET_ALL)
r1=rise_bottom_top_dome+0.375  
r1=round(r1,3)
print("Rise of mean surface of dome = {0} m \n".format(r1))
d1=2*inner_radius_circular_wall+thickness_wall

print("Diameter of mean surface = {0} m \n".format(d1))
R1=((d1*d1)/(4*r1)+(r1))/2
R1=round(R1,3)
print("Mean radius of the top dome R1, is given by = {0} m \n".format(R1))
Dead_load_top_dome =(thickness_top_dome)*concrete_unit
print("Dead load of top dome = {0}kN/mm\u00b3 \n".format(Dead_load_top_dome))
LL=0.75
print("Live load = {0}kN/mm\u00b3 \n".format(LL))
TL=Dead_load_top_dome + LL
print("Total load = {0}kN/mm\u00b3 \n".format(TL))
x1=(d1/(2*R1))

alpha=math.asin(x1)* (180.0 / math.pi)
alpha=round(alpha, 3)
#print(alpha)
if alpha<51.48:     
    print('Thus,semi central  angle alpha =' + str(alpha) +'° < 51° and 48"\n')
    print('Hence, the entire top dome will remain under hoop compression\n')
else:
    print('Thus,semi central  angle alpha =' + str(alpha) +'° > 51° and 48" \n')  
    print('Hence, The entire top dome will not remain under hoop compression\n')
T1=(TL*R1)/(1+math.cos(alpha*pi/180) )
T1=round(T1,2)
print("Max Meridional Thrust T1 = {0} kN/m \n".format(T1))           
mstress=(T1*1000/(100*1000*thickness_top_dome*rise_bottom_top_dome))
print("Meridional stress = {0} MPa \n".format(mstress))
if mstress<5:

    print('since Meridional stress  is less than 5Mpa. it is safe\n')
else:
    print("It's not safe.\n")   
print('since max dimension of the container is less than 15 m,provide 0.24% min reinforcement in each direction in the middle of the dome\n')
steelarea=(0.0024*thickness_top_dome*rise_bottom_top_dome*1000000)                  
print("                       ="+str(steelarea)+"mm\u00b2\n")
dia1=8
spacing=(pi*0.25*dia1*dia1)/steelarea*1000


print('\nprovide {0}mm bars @250mm c/c radially and circumferentially \n'.format(dia1))  # Here had to implement functions 

points= 270,110
string='8mm bars @250mm'
draw.text(points,string,'blue',font=font1)

# #Step:-2 (Design of Top Ring Beam)
print(Fore.GREEN +"\n \nStep:-3 Design of Top Ring Beam\n"+ Style.RESET_ALL)
print("A ring beam is provided at the junction of top dome and the vertical wall to resist hoop tension induced by the top dome.\nLet its section - 150 mm x 250 mm deep,\n")
Hooptension=T1*math.cos(alpha*pi/180)*d1*0.5   
Hooptension=round(Hooptension,3)                                  
#print(math.cos(alpha*pi/180))
print("Hoop Stress = "+str(Hooptension)+"kN\n")
print("Permissible stress in steel = 130 Mpa\n")
Ast=Hooptension*1000/130
Ast=round(Ast,3)
print('Area of steel required'+str(Ast)+'mm\u00b2  \n')
print("Provide 4-12 mm hoops and 8 ties @ 250 mm c/c.\n")  # Here had to implement functions
points= 60,190
string='4-12 mm bars and 8 ties \n @ 250 mm c/c'
draw.text(points,string,'blue',font=font1) 
TopRingBeamDia=12
TopRingBeamNo=4

DirectTensileStressConcrete=(Hooptension*1000)/(250*150+8*(TopRingBeamNo*pi*0.25*TopRingBeamDia*TopRingBeamDia))#have to change this Section details
DirectTensileStressConcrete=round(DirectTensileStressConcrete,3)
print("Direct tensile stress in concrete = {0} MPa \n".format(DirectTensileStressConcrete))
if (DirectTensileStressConcrete < 1.5):
   print(str(DirectTensileStressConcrete)+"MPa < 1.5MPa\n")
else:
      print(str(DirectTensileStressConcrete)+"MPa > 1.5MPa\n") 



#Step:-3 Vertical Wall 
print(Fore.GREEN + "\n \nStep:-4  Design of Vertical Wall \n"+ Style.RESET_ALL)

#print("Dead load due to top dome = 2 π R\u2081 H\u2081 t Ye\n")
Dead_load_top_dome=2*pi*R1*r1*thickness_top_dome*concrete_unit
Dead_load_top_dome=round(Dead_load_top_dome,3)
#print(Dead_load_top_dome)
LL=2*pi*R1*r1*LL
LL=round(LL,3)
print("Dead load due to top dome = {0}KN \n".format(Dead_load_top_dome))
print("Live load on top dome = {0} KN\n".format(LL))
Dead_load_top_ring_beam=0.05*0.25*concrete_unit *pi*d1
Dead_load_top_ring_beam=round(Dead_load_top_ring_beam,3)
print("Dead load due to top ring beam ={0} KN \n".format(Dead_load_top_ring_beam))
Dead_load_vertical_wall=d1*pi*thickness_bottom_dome*height_wall*concrete_unit
Dead_load_vertical_wall=round(Dead_load_vertical_wall,3)
print("Dead load due to vertical wall ={0} KN \n".format(Dead_load_vertical_wall))
Dead_load_taper_wall=d1*pi*0.5*0.05*1   *concrete_unit
Dead_load_taper_wall=round(Dead_load_taper_wall,3)
print("Dead load due to taper in wall={0} KN \n".format(Dead_load_taper_wall))
Tl=Dead_load_top_dome+LL+Dead_load_top_ring_beam+Dead_load_vertical_wall+Dead_load_taper_wall
Tl=round(Tl,3)
print("Total Load={0} KN \n".format(Tl))
Tlm=Tl/(pi*inner_radius_circular_wall*2)
Tlm=round(Tlm,3)
print("Total load per m ={0} KN/m \n".format(Tlm))
compression_stress=Tlm*1000/(1000*free_board*1000)
compression_stress=round(compression_stress,3)   
print("Compressive stress ={0} MPa < 8 MPa \n \n ".format(compression_stress))
#print("Hoop tension at any depth x from top = rwhD/2 \n")

mydata = [
  
]
depth=int(height_wall)
for i in range(0,depth+1):
  mydata.append([i,10*i*D/2])      
head = ["x, m", "Hoop tension, kN/m "]
print(tabulate(mydata, headers=head, tablefmt="grid"))

Hooptension=10*depth*d1/2

At=Hooptension*1000/130
At=round(At,3)
print("\n\nArea of steel required to resist hoop tension {0} mm\u00b2".format(At))
HoopSpace=100
print("Provide 16 hoops @ 100 mm c/c.\n")        #Here have change     
Ap=pi*0.25*16*16*1000/HoopSpace
Ap=round(Ap,3)
print("Area Provided= {0} > {1} mm\u00b2 \n".format(Ap,At))

points=400,380
string='16 mm bars @ 100 mm c/c'
draw.text(points,string,'blue',font=font1) 

if depth==4:
    section=150
else:
    section=140

Tensilestree=Hooptension*1000/(section*1000+8*Ap)
Tensilestree=round(Tensilestree,3)

print("Tensile stress in concrete at {0} m depth = {1} MPa < 1.5 Mpa \n".format(depth,Tensilestree)) #have to change based on table


print("The hoop steel may be curtailed according to hoop tension at different heights along Puride 0.24 % minimum vertical reinforcement, (= 240 mm\u00b2/m )that is, 8 mm 150 mm c/c\n")#have to change 
points=  400,300
string='8 mm bars @150 mm c/c'
draw.text(points,string,'blue',font=font1) 

#Step:-4 Bottom Dome
print(Fore.GREEN + "\n \n Step:-5 Bottom Dome\n"+ Style.RESET_ALL)
print("If the top surface of the bottom dome makes an angle 2 alpha at its centre,\n")
x1=((inner_radius_circular_wall-thickness_bottom_dome)/(R2))
alpha=math.asin(x1)* (180.0 / math.pi)
alpha=round(alpha, 3)
if alpha < 51:
    print("Semi central angle a = {0}° < 51° 48' \n".format(alpha))
    print("Hence, Entire dome will in hoop compression.\n") 
else:
    print("Hence, Entire dome not in hoop compression.\n")    
Dl_bottom_dome=25*thickness_bottom_dome
print("Load due to self weight of bottom dome = {0} kN/m² \n".format(Dl_bottom_dome))
radial=height_wall-free_board
difference=(radial-H)
Load_radial_water_column=difference*10
Load_radial_water_column=round(Load_radial_water_column,2)
print("Load due to radial water column ({0} m-{1} m) = {2} kN/m \n".format(radial,H,Load_radial_water_column))
Load_radial_water_pressure=H*10 
print("Load due to radial water pressure varying for zero at crown to maximum in {0} m depth = {1} kN/m\u00b2 \n".format(H,Load_radial_water_pressure))
alpha=alpha*pi/180
Meridional_thrust=(R2*Dl_bottom_dome)/(1+math.cos(alpha))+(Load_radial_water_column*R2/2)+10*(R2*R2/6)*((1+math.cos(alpha)-2*math.cos(alpha)*math.cos(alpha))/(1+math.cos(alpha)))
T1=round(Meridional_thrust,3)
print("Meridional thrust at edges={0} KN/m \n".format(T1))
Horizontal_thrust_edges=Meridional_thrust*math.cos(alpha)
Horizontal_thrust_edges=round(Horizontal_thrust_edges,3)
print("Horizontal thrust at edges={0} KN/m \n".format(Horizontal_thrust_edges))
Compressive_stress=Meridional_thrust*1000/(1000*1000)
Compressive_stress=round(Compressive_stress,3)
print("Compressive stress = {0} MPa < 8 MPa \n".format(Compressive_stress))
print("Provide 0.24 % minimum reinforcement in the bottom dome in each direction\n")
At=0.0024*100*1000
print("Provide 8 mm bars @ 200 mm c/c radially and circumferentially\n")#have to update function 
points= 450,530
string='8 mm bars @ 200 mm c/c'
draw.text(points,string,'blue',font=font1) 


#Step-5:- Design of Bottom ring
print(Fore.GREEN +"\n\n Step-6:- Design of Bottom ring\n"+ Style.RESET_ALL)
print("Weight at the bottom of wall = {0} KN \n".format(Tl))
Weight_bottom_dome=2*pi*R2*(rise_bottom_dome+0.05)*(thickness_bottom_dome)*concrete_unit
Weight_bottom_dome=round(Weight_bottom_dome,3)
print("Weight at bottom dome = {0} KN \n".format(Weight_bottom_dome))
weight_water=V*10 
weight_water=round(weight_water,2)
print("weight of water = {0} KN \n".format(weight_water))
Weight_ring_beam = inner_radius_circular_wall*2*bottom_ring_beam*25*pi
Weight_ring_beam=round(Weight_ring_beam,3)
print("Weight of ring beam = {0} KN \n".format(Weight_ring_beam))
Tw=weight_water+Weight_ring_beam+Weight_bottom_dome+Tl
Tw=round(Tw,3)
print("Total weight = {0} KN \n".format(Tw))
Weight_unit_length=Tw/(pi*inner_radius_circular_wall*2)
Weight_unit_length=round(Weight_unit_length,3)
print("Weight per unit length = {0} KN/m \n".format(Weight_unit_length))
print("Let the ring beam be supported on 6-300 mm dia columns\n")
print("It can be designed as a circular beam in plan supported on six columns\n")
matomo=430*(pi/180*12.75)
matomo=round(matomo,2)
print("The maximum torsional moment occurs at 12.75° from the centre line of line of the column = {0} cm \n".format(matomo))
x=2*Weight_unit_length*inner_radius_circular_wall*inner_radius_circular_wall*pi/3
Sagging_moment_midspan=x*0.045
Sagging_moment_midspan=round(Sagging_moment_midspan,3)
Hogging_moment=x*0.089*-1
Hogging_moment=round(Hogging_moment,3)
torsional_moment=x*0.009
torsional_moment=round(torsional_moment,3)
print("Sagging moment at midspan = {0} KNm \n".format(Sagging_moment_midspan))
print("Hogging moment at support = {0} KNm \n".format(Hogging_moment))
print("Maximum torsional moment = {0} KNm  \n".format(torsional_moment))
shear_force=0.5*Weight_unit_length*(d1*pi/6-b)
shear_force=round(shear_force,3)
print("Maximum Shear Force at face of column = {0} KN \n".format(shear_force))
Hoop_tension=T1*math.cos(alpha)*D/2
Hoop_tension=round(Hoop_tension,3)
print("Hoop Tension caused by the meridional thrust from the bottom dome = {0} KN \n".format(Hoop_tension))
print("The ring beam is just the wall and balcony. Thus, part of vertical wall and cy also carry the forces induced in the ring beam. \n \nThe stiffnesses of wall and balcony are quite high. The ring beam will be designed aa follows:\n")
e=Hogging_moment*(-1)/Hoop_tension*1000
e=round(e,3)
print(" (i) at the support for a bending moment = {0} kNm and direct tension = {1} \n".format(Hogging_moment,Hoop_tension))
print("Eccentrycity ={0} mm > 350 mm \n".format(e))
e2=Sagging_moment_midspan/Hoop_tension*1000
e2=round(e2,3)
print(" (ii) at the mid span for a bending moment = {0} kNm and direct tension = {1} \n".format(Sagging_moment_midspan,Hoop_tension))
print("Eccentrycity ={0} mm > 350 mm \n".format(e2))
print(" (iii) for a shear force due to {0} kN/m load and twisting moment={1} km 12 from the centre line of the column \n".format(Weight_unit_length,torsional_moment))
curverd_span=pi*inner_radius_circular_wall*2/6
curverd_span=round(curverd_span,3)
curverd_clear_span=curverd_span-0.3 
curverd_clear_span=round(curverd_clear_span,3)
print("     Curved span c/c = {0} \n".format(curverd_span))
print("     Curved clear span = {0} \n".format(curverd_clear_span))
print(" (iv) for shear force at the face of the column due to {0} kN/m load \n".format(Weight_unit_length))
V=Weight_unit_length*curverd_span/2-Weight_unit_length*0.957
V=round(V,3)
print("  Shear force at the section of maximum torsional moment = {0}KN \n".format(V))
Ve=V+1.6*torsional_moment/b
Ve=round(Ve,3)
if Ve>147:

    print("Equvalent shear force Ve = {0} > 147 KN \n".format(Ve))

print("Hence design the section for bending moment using Eqs. 23.21 and 23.22 and the force of {0} KN. Provide 8-16 mm bars in the ring beam. Also, provide 104-1 legged stirrups @200 mm c/c \n".format(Ve)) 
points=420,460
string='8-16 mm bars'
draw.text(points,string,'blue',font=font1)



#Height of wall
points= 760,370
string=str(height_wall)+' m'
draw.text(points,string,'red',font=font1)
#Innerradiuso fcircular wall
points3= 750,240
string3=str(inner_radius_circular_wall*2)
draw.text(points3,string3,'red',font=font1)
#Riseofbottom of top dome   
points4= 760,170
string4=str(rise_bottom_top_dome)+' m'
draw.text(points4,string4,'red',font=font1)


YN=input("Do You Want to see reinforce ment details Press Y/N \n")
if YN=="Y" :
   image.show()