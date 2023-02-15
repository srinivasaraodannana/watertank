 #-------Design of overhead Circular Water Tank(Bhargavi Bilingi)----------
#Library Module Used
import math 




#Data Given
volume=4.5#Lakhs Lit
concrete=30#M30
steel_grade=415#Fe415


inner_radius_circular_wall= 4250/1000 #mm
thickness_wall =100/1000 #mm
height_wall =3200/1000 #mm
thickness_top_dome =75/1000 #mm
rise_bottom_top_dome=1000/1000#mm
thickness_bottom_dome=100/1000#mm
rise_bottom_dome= 1500/1000 #mm
bottom_ring_beam= 350*350/(1000**2) #mm 
free_board=150/1000 #mm
height_staging_above_GL=25/1000 #mm




#Total Designing Steps-5
#Step-0:- Check for capacity
#Step-1:- Top Dome
#Step-2:- Vertical wall
#Step-3:- Bottom Dome
#Step-4:- Base Slab
#Step-5:- Bottom Ring Beam






#Step:-0
H=1.6# have to know what is this
D=2*(inner_radius_circular_wall-(free_board-height_staging_above_GL))
print(D)
R2=((D**2/(4*H))+H)/2
pi = math.pi
V1 = (pi)*((H*H)/3)
V1=V1*(3*R2-H)
print("Volume of water displaced by bottom dome",V1)
print("Let us increase the thickness of vertical wall from 100 mm to 150 mm in the lower height. This taper is provided inside the water tank.")
if thickness_wall<=0.1:
   thickness_wall=150/1000
V= (pi/4)*((2*inner_radius_circular_wall)**2)*(height_wall-free_board)-0.05*0.5*rise_bottom_top_dome*pi*((2*inner_radius_circular_wall)-2/3*0.05)-V1
print("{0} m3 > 125 m3".format(V))


#Step-1 Top Dome
r1=rise_bottom_top_dome+0.0375
d1=2*R2+0.10
R1=(d1*d1)/(8*r1)+(r1/2)
Dead_load_top_dome =(thickness_top_dome)*25
LL=0.75
TL=Dead_load_top_dome + LL
x1=(d1/(2*R1))
alpha=math.asin(x1)* (180.0 / math.pi)
alpha=round(alpha, 2)
print(alpha)
print('Thus,semi central  angle alpha =' + str(alpha) +'<51degree and 48minutes')
print('\nThe entire top dome will remain under hoop compression')
T1=(TL*R1/2)/(1+math.cos(alpha) )
print(T1)           
mstress=(T1*1000/(1000*thickness_top_dome*1000))
print(mstress)
print('since mstress is less than 5Mpa. it is safe')
print('since max dimension of the container is less than 15 m,provide 0.24% min reinforcement in each direction in the middle of the dome')
steelarea=(0.0024*thickness_top_dome*1000*1000)
print(str(steelarea)+"mm2")
print('provide 8mm bars @250mm c/c radially and circumferentially ')




# #Step:-2 (Design of Top Ring Beam)
print("A ring beam is provided at the junction of top dome and the vertical wall to resist hoop tension induced by the top dome. Let its section - 150 mm x 250 mm deep,")
Hooptension=T1*math.cos(alpha)*D*0.5
print(str(Hooptension)+"kN")
print("Permissible stress in steel = 130 Mpa")
Ast=Hooptension*1000/130
print(str(Ast)+'Area of steel required')
print("Provide 4-12 mm hoops and 8 ties @ 250 mm c/c.")
DirectTensileStressConcrete=(Hooptension*1000)/(250*150+8*(4*113))#have to change this
print(str(DirectTensileStressConcrete)+"<1.5MPa")


#Step:-3 Vertical Wall 
print("Dead load due to top dome = 2 R H Ye")
H1=1.0375
R1=R1/2
Dead_load_top_dome=2*pi*R1*H1*thickness_top_dome*25
LL=46
print("Dead load due to top dome",Dead_load_top_dome)
print(" Live load on top dome = 46 KN")
Dead_load_top_ring_beam=(thickness_top_dome-height_staging_above_GL)*0.25*25*pi*inner_radius_circular_wall*2 #have to change
print("Dead load due to top ring beam =",Dead_load_top_ring_beam)
Dead_load_vertical_wall=inner_radius_circular_wall*2*pi*thickness_bottom_dome*height_wall*25
print("Dead load due to vertical wall =",Dead_load_vertical_wall)
Dead_load_taper_wall=inner_radius_circular_wall*2*pi*0.5*(thickness_top_dome-height_staging_above_GL)*rise_bottom_top_dome*25
print("Dead load due to taper in wall=",Dead_load_taper_wall)
Tl=Dead_load_top_dome+LL+Dead_load_top_ring_beam+Dead_load_vertical_wall+Dead_load_taper_wall
print("Total Load=",Tl)
Tlm=Tl/(pi*inner_radius_circular_wall*2)
print("Total load per m =",Tlm)
compression_stress=Tlm*1000/(1000*free_board*1000)
print("Compressive stress ={0}< 8 MPa".format(compression_stress))
print(" Hoop tension at any depth x from top = rwhD/2 ")
##--------------------------------------------------------HAve to draw a table here
Hooptension=10*3*D/2
print("At 3m =",Hooptension)
At=Hooptension*1000/130
print("Area of steel required to resist hoop tension",At)
print("Provide 12 hoops @ 100 mm c/c.")
Ap=1.13*1000/100
print("Area Provided={0}>981mm2".format(Ap))
print("Tensile stress in concrete at 3 m depth")
Tensilestree=Hooptension*1000/(140*1000+8*Ap)
print("{0} < 1.5 Mpa".format(Tensilestree))
print("The hoop deel may be curtailed according to hoop tension at different heights along Puride 0.24 % minimum vertical reinforcement, (= 240 mm2/m )that is, 8 mm 150 mm c/c")

#Step:-4 Bottom Dome
print("If the top surface of the bottom dome makes an angle 2 a at its centre,")










     
