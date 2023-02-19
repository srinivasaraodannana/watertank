 #-------Design of overhead Circular Water Tank(Bhargavi Bilingi)----------
#Library Module Used
import math 




#Data Given
volume=125#kilo Lit
concrete=25#M30
steel_grade=415#Fe415
inner_radius_circular_wall= (4250)/1000 #mm
thickness_wall =100/1000 #mm
height_wall =3200/1000 #mm
thickness_top_dome =75/1000 #mm
rise_bottom_top_dome=1000/1000#mm
thickness_bottom_dome=100/1000#mm
rise_bottom_dome= 1500/1000 #mm
bottom_ring_beam= 350*350/(1000**2) #mm 
b=350/1000
free_board=150/1000 #mm
height_staging_above_GL=25/1000 #mm




#Total Designing Steps-5
#Step-0:- Check for capacity
#Step-1:- Top Dome
#Step-2:- Vertical wall
#Step-3:- Bottom Dome
#Step-4:- Design of Bottom ring
#Step-5:- Bottom Ring Beam






#Step:-0
H=rise_bottom_dome+thickness_bottom_dome
D=2*(inner_radius_circular_wall-(free_board-height_staging_above_GL))

R2=((D**2/(4*H))+H)/2
print(R2)
pi = math.pi
V1 = (pi)*((H*H)/3)
V1=V1*(3*R2-H)
print("Volume of water displaced by bottom dome",V1)
print("Let us increase the thickness of vertical wall from 100 mm to 150 mm in the lower height. This taper is provided inside the water tank.")
if thickness_wall<=0.1:
   thickness_wall=150/1000
V= (pi/4)*((2*inner_radius_circular_wall)**2)*(height_wall-thickness_wall)-0.05*0.5*rise_bottom_top_dome*pi*((2*inner_radius_circular_wall)-2/3*0.05)-V1
if V>=volume:
 print("{0} m3 > {1} m3".format(V,volume))
else:
   print("The dimensions are not suficient for given volume of water") 


#Step-1 Top Dome
print("Step-2:-Top Dome")
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
   print('Thus,semi central  angle alpha =' + str(alpha) +'<51degree and 48minutes')
   print('The entire top dome will remain under hoop compression')
else:
    print('Thus,semi central  angle alpha =' + str(alpha) +'>51degree and 48minutes')  
    print('The entire top dome will not remain under hoop compression')
T1=(TL*R1)/(1+math.cos(alpha*pi/180) )
print("Max Meridional Thrust T1",T1)           
mstress=(T1*1000/(1000*thickness_top_dome*1000))
print("Meridional stress =",mstress)
if mstress<5:

   print('since Meridional stress  is less than 5Mpa. it is safe')
else:
   print("It's not safe.")   
print('since max dimension of the container is less than 15 m,provide 0.24% min reinforcement in each direction in the middle of the dome')
steelarea=(0.0024*thickness_top_dome*1000*1000)
print(str(steelarea)+"mm2")
spacing=steelarea/(pi*0.25*8*8)
print(spacing)
print('provide 8mm bars @250mm c/c radially and circumferentially ')



