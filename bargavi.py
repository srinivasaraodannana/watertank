 #-------Design of overhead Circular Water Tank(Bhargavi Bilingi)----------







#Library Module Used
import math 

from tabulate import tabulate #for printing tables

# from PIL import Image, ImageDraw, ImageFont # for the display images








#Data Given
# volume=125#kilo Lit

# concrete=25#M\u00b30
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



volume=float(input("Enter the volume of the tank in Kilo Litres "))
concrete=float(input("Enter the grade of concrete "))
steel_grade=float(input("Enter the grade of steel "))
inner_radius_circular_wall=float(input("Enter Inner radius of circular wall in mm "))
thickness_wall=float(input("Enter Thickness of wall in mm "))
height_wall=float(input("Enter Height of wall in mm "))
thickness_top_dome=float(input("Enter Thickness of top dome in mm "))
rise_bottom_top_dome=float(input("Enter rise of bottom of top dome in m "))
thickness_bottom_dome=float(input("Enter Thickness of bottom dome in mm "))
rise_bottom_dome=float(input("Enter Rise of bottom of bottom dome "))
b,bottom_ring_beam=map(float,input("Enter Bottom ring beam in mm X mm by giving space ").split())

free_board=float(input("Enter Free board in mm "))
height_staging_above_GL=float(input("Enter Height of staging above G.L in mm "))








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






#Step:-0
print("\n \nStep:-1 Check for Capacity\n")
H=rise_bottom_dome+thickness_bottom_dome
D=2*(inner_radius_circular_wall-(free_board-height_staging_above_GL))

R2=((D**2/(4*H))+H)/2
R2=round(R2,2)
print("Radius of top surface of bottom dome R2 is given by = {0} m".format(R2))
pi = math.pi
V1 = (pi)*((H*H)/3)
V1=V1*(3*R2-H)
V1=round(V1,2)
print("Volume of water displaced by bottom dome = {0} m\u00b3".format(V1))
if thickness_wall<=0.1:
   print("Let us increase the thickness of vertical wall from 100 mm to 150 mm in the lower height. This taper is provided inside the water tank.")
   thickness_wall=150/1000
V= (pi/4)*((2*inner_radius_circular_wall)**2)*(height_wall-thickness_wall)-0.05*0.5*rise_bottom_top_dome*pi*((2*inner_radius_circular_wall)-2/3*0.05)-V1
if V>=volume:
   print("{0} m\u00b3 > {1} m\u00b3".format(V,volume))
   print("So Design is design of required.")
else:
   print("The design are not required for given volume of water.") 


#Step-1 Top Dome
print("\n \nStep-2:-Top Dome\n")
r1=rise_bottom_top_dome+0.0375  #have to look
#print(r1)
d1=2*inner_radius_circular_wall+thickness_wall
#print(d1)
R1=((d1*d1)/(4*r1)+(r1))/2
#print(R1)
Dead_load_top_dome =(thickness_top_dome)*concrete
LL=0.75
TL=Dead_load_top_dome + LL
x1=(d1/(2*R1))
alpha=math.asin(x1)* (180.0 / math.pi)
alpha=round(alpha, 2)
#print(alpha)
if alpha<51.48:
    print('Thus,semi central  angle alpha =' + str(alpha) +'° < 51° and 48"')
    print('Hence, the entire top dome will remain under hoop compression')
else:
    print('Thus,semi central  angle alpha =' + str(alpha) +'° > 51° and 48" ')  
    print('Hence, The entire top dome will not remain under hoop compression')
T1=(TL*R1)/(1+math.cos(alpha*pi/180) )
print("Max Meridional Thrust T1 = {0} kN/m".format(T1))           
mstress=(T1*1000/(1000*thickness_top_dome*1000))
print("Meridional stress = {0} kN/m".format(mstress))
if mstress<5:

    print('since Meridional stress  is less than 5Mpa. it is safe')
else:
    print("It's not safe.")   
print('since max dimension of the container is less than 15 m,provide 0.24% min reinforcement in each direction in the middle of the dome')
steelarea=(0.0024*thickness_top_dome*1000*1000)
print("                       ="+str(steelarea)+"mm\u00b2")
spacing=steelarea/(pi*0.25*8*8)
#print(spacing)
print('\nprovide 8mm bars @250mm c/c radially and circumferentially ')  # Here had to implement functions 



# #Step:-2 (Design of Top Ring Beam)
print("\n \nStep:-3 Design of Top Ring Beam\n")
print("A ring beam is provided at the junction of top dome and the vertical wall to resist hoop tension induced by the top dome. Let its section - 150 mm x 250 mm deep,")
Hooptension=T1*math.cos(alpha*pi/180)*d1*0.5
#print(math.cos(alpha*pi/180))
print("Hoop Stress = "+str(Hooptension)+"kN")
print("Permissible stress in steel = 130 Mpa")
Ast=Hooptension*1000/130
Ast=round(Ast,2)
print(str(Ast)+'mm\u00b3  Area of steel required')
print("Provide 4-12 mm hoops and 8 ties @ 250 mm c/c.")  # Here had to implement functions 
TopRingBeamDia=12
TopRingBeamNo=4

DirectTensileStressConcrete=(Hooptension*1000)/(250*150+8*(TopRingBeamNo*pi*0.25*TopRingBeamDia*TopRingBeamDia))#have to change this Section details
DirectTensileStressConcrete=round(DirectTensileStressConcrete,2)
if (DirectTensileStressConcrete < 1.5):
   print(str(DirectTensileStressConcrete)+"MPa < 1.5MPa")
else:
      print(str(DirectTensileStressConcrete)+"MPa > 1.5MPa") 



#Step:-3 Vertical Wall 
print("\n \nStep:-4  Design of Vertical Wall \n")

print("Dead load due to top dome = 2 π R\u2081 H\u2081 t Ye")
Dead_load_top_dome=2*pi*R1*r1*thickness_top_dome*concrete
Dead_load_top_dome=round(Dead_load_top_dome,2)
#print(Dead_load_top_dome)
LL=46
print("Dead load due to top dome = {0}KN".format(Dead_load_top_dome))
print("Live load on top dome = 46 KN")
Dead_load_top_ring_beam=(thickness_top_dome-height_staging_above_GL)*0.25*concrete*pi*inner_radius_circular_wall*2 
Dead_load_top_ring_beam=round(Dead_load_top_ring_beam,2)
print("Dead load due to top ring beam ={0} KN".format(Dead_load_top_ring_beam))
Dead_load_vertical_wall=inner_radius_circular_wall*2*pi*thickness_bottom_dome*height_wall*concrete
Dead_load_vertical_wall=round(Dead_load_vertical_wall,2)
print("Dead load due to vertical wall ={0} KN".format(Dead_load_vertical_wall))
Dead_load_taper_wall=inner_radius_circular_wall*2*pi*0.5*(thickness_top_dome-height_staging_above_GL)*rise_bottom_top_dome*concrete
Dead_load_taper_wall=round(Dead_load_taper_wall,2)
print("Dead load due to taper in wall={0} KN".format(Dead_load_taper_wall))
Tl=Dead_load_top_dome+LL+Dead_load_top_ring_beam+Dead_load_vertical_wall+Dead_load_taper_wall
Tl=round(Tl,2)
print("Total Load={0} KN".format(Tl))
Tlm=Tl/(pi*inner_radius_circular_wall*2)
Tlm=round(Tlm,2)
print("Total load per m ={0} KN/m".format(Tlm))
compression_stress=Tlm*1000/(1000*free_board*1000)
compression_stress=round(compression_stress,2)   
print("Compressive stress ={0} MPa < 8 MPa".format(compression_stress))
print("Hoop tension at any depth x from top = rwhD/2 ")

mydata = [
  
]
abc=int(height_wall)
for i in range(0,abc+1):
  mydata.append([i,10*i*D/2])
head = ["x, m", "Hoop tension, kN/m "]
print(tabulate(mydata, headers=head, tablefmt="grid"))
Hooptension=10*abc*D/2
At=Hooptension*1000/130
print("Area of steel required to resist hoop tension",At)
HoopSpace=100
print("Provide 12 hoops @ 100 mm c/c.")        #Here have change
Ap=1.13*100000/HoopSpace
print("Area Provided= {0} > {1} mm\u00b2".format(Ap,At))
Tensilestree=Hooptension*1000/(140*1000+8*Ap)
Tensilestree=round(Tensilestree,2)
print("Tensile stress in concrete at 3 m depth = {0}MPa".format(Tensilestree))#have to change based on table

print("{0} < 1.5 Mpa".format(Tensilestree))
print("The hoop steel may be curtailed according to hoop tension at different heights along Puride 0.24 % minimum vertical reinforcement, (= 240 mm\u00b2/m )that is, 8 mm 150 mm c/c")#have to change 

#Step:-4 Bottom Dome
print("\n \n Step:-5 Bottom Dome\n")
print("If the top surface of the bottom dome makes an angle 2alpha at its centre,")
x1=((inner_radius_circular_wall-thickness_bottom_dome)/(R2))
alpha=math.asin(x1)* (180.0 / math.pi)
alpha=round(alpha, 2)
if alpha < 51:
    print("Semi central angle a = {0}° < 51° 48'".format(alpha))
    print("Hence, Entire dome will in hoop compression.") 
else:
    print("Hence, Entire dome not in hoop compression.")    
Dl_bottom_dome=25*thickness_bottom_dome
print("Load due to self weight of bottom dome = {0} kN/m²".format(Dl_bottom_dome))
Load_radial_water_column=1.45*10## Don't know what are these
print("Load due to radial water column (3.05 m-1.6 m) = {0} kN/m".format(Load_radial_water_column))
Load_radial_water_pressure=1.6*10 ## this too
print("Load due to radial water pressure varying for zero at crown to maximum in 1.6 m depth={0} kN/m".format(Load_radial_water_pressure))
alpha=alpha*pi/180
Meridional_thrust=(R2*Dl_bottom_dome)/(1+math.cos(alpha))+(Load_radial_water_column*R2/2)+10*(R2*R2/6)*((1+math.cos(alpha)-2*math.cos(alpha)*math.cos(alpha))/(1+math.cos(alpha)))
T1=round(Meridional_thrust,2)
print("Meridional thrust at edges={0} KN/m".format(T1))
Horizontal_thrust_edges=Meridional_thrust*math.cos(alpha)
Horizontal_thrust_edges=round(Horizontal_thrust_edges,2)
print("Horizontal thrust at edges={0} KN/m".format(Horizontal_thrust_edges))
Compressive_stress=Meridional_thrust*1000/(1000*1000)
Compressive_stress=round(Compressive_stress,2)
print("{0} < 8 MPa".format(Compressive_stress))
print("Provide 0.24 % minimum reinforcement in the bottom dome in each direction")
At=0.0024*100*1000
print("Provide 8 mm bars @ 200 mm c/c radially and circumferentially")#have to update function 



#Step-5:- Design of Bottom ring
print("\n\n Step-6:- Design of Bottom ring\n")
print("Weight at the bottom of wall = {0} KN".format(Tl))
Weight_bottom_dome=2*pi*R2*rise_bottom_dome*thickness_bottom_dome*25
Weight_bottom_dome=round(Weight_bottom_dome,2)
print("Weight at bottom dome = {0} KN".format(Weight_bottom_dome))
weight_water=1275 #don't know what 
print("weight of water = {0} KN".format(weight_water))
Weight_ring_beam = inner_radius_circular_wall*2*bottom_ring_beam*25*pi
Weight_ring_beam=round(Weight_ring_beam,2)
print("Weight of ring beam = {0} KN".format(Weight_ring_beam))
Tw=weight_water+Weight_ring_beam+Weight_bottom_dome+Tl
Tw=round(Tw,2)
print("Total weight = {0} KN".format(Tw))
Weight_unit_length=Tw/(pi*inner_radius_circular_wall*2)
Weight_unit_length=round(Weight_unit_length,2)
print("Weight per unit length = {0} KN/m".format(Weight_unit_length))
print("Let the ring beam be supported on 6-300 mm dia columns")
print("It can be designed as a circular beam in plan supported on six columns")
x=2*Weight_unit_length*inner_radius_circular_wall*inner_radius_circular_wall*pi/3
Sagging_moment_midspan=x*0.045# Have to know 
Sagging_moment_midspan=round(Sagging_moment_midspan,2)
Hogging_moment=x*0.089*-1
Hogging_moment=round(Hogging_moment,2)
torsional_moment=x*0.009
torsional_moment=round(torsional_moment,2)
print("Sagging moment at midspan = {0} KNm".format(Sagging_moment_midspan))
print("Hogging moment at support = {0} KNm".format(Hogging_moment))
print("Maximum torsional moment = {0} KNm ".format(torsional_moment))
shear_force=0.5*Weight_unit_length*inner_radius_circular_wall*2*pi/6-b#have to look
shear_force=round(shear_force,2)
print("Maximum Shear Force at face of column = {0} KN".format(shear_force))
Hoop_tension=T1*math.cos(alpha)*D/2
Hoop_tension=round(Hoop_tension,2)
print("Tension caused by the meridional thrust from the bottom dome = {0} KN".format(Hoop_tension))
print("The ring beam is just the wall and balcony. Thus, part of vertical wall and cy also carry the forces induced in the ring beam. The stiffnesses of wall and balcony are quite high. The ring beam will be designed aa follows:")
e=Hogging_moment*(-1)/Hoop_tension*1000
e=round(e,2)
print(" (i) at the support for a bending moment = {0} kNm and direct tension = {1}".format(Hogging_moment,Hoop_tension))
print("Eccentrycity ={0} mm > 350 mm".format(e))
e2=Sagging_moment_midspan/Hoop_tension*1000
e2=round(e2,2)
print(" (i) at the mid span for a bending moment = {0} kNm and direct tension = {1}".format(Sagging_moment_midspan,Hoop_tension))
print("Eccentrycity ={0} mm > 350 mm".format(e2))
print(" (iii) for a shear force due to {0} kN/m load and twisting moment={1} km 12 from the centre line of the column".format(Weight_unit_length,torsional_moment))
curverd_span=pi*inner_radius_circular_wall*2/6# have to know what is 6
curverd_span=round(curverd_span,2)
curverd_clear_span=curverd_span-0.3 #0.3 ?
curverd_clear_span=round(curverd_clear_span,2)
print("     Curved span c/c=",curverd_span)
print("     Curved clear span ",curverd_clear_span)
print(" (iv) for shear force at the face of the column due to {0} kN/m load".format(Weight_unit_length))
V=Weight_unit_length*curverd_span/2-Weight_unit_length*0.957 # what is 0.957
V=round(V,2)
print("  Shear force at the section of maximum torsional moment",V)
Ve=V+1.6*torsional_moment/b
Ve=round(Ve,2)
if Ve>147:

    print("Equvalent shear force Ve= {0}>147".format(Ve))

print("Hence design the section for bending moment using Eqs. 23.21 and 23.22 and the force of {0} KN. Provide 8-16 mm bars in the ring beam. Also, provide 104-1 legged stirrups @200 mm c/c".format(Ve)) 



# YN=input("Do You Want to see reinforce ment details Press Y/N ")
# if YN=="Y" :
#    image = Image.open('img1.jpeg')
#    draw = ImageDraw.Draw(image)
#    font1 = ImageFont.truetype ("edosz.otf" ,20)
#    points= 0,0
#    string="Hi Bhar This text is Generated from python. If want to change text on Images you can."
#    draw.text(points,string,'red',font=font1)
#    image.show()