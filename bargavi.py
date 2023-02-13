#-------Design of overhead Circular Water Tank(Bhargavi Bilingi----------
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
bottom_ring_beam= 350/1000 #mm 
free_board=150/1000 #mm
height_staging_above_GL=25/1000 #mm




#Total Designing Steps-5
#Step-0:- Check for capacity
#Step-1:- Top Dome
#Step-2:- Top Ring Beam
#Step-3:- Tank Wall
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


# #Step-1 




# #Step:-2 (Design of Top Dome)
# W=1.5+0.1*concrete #assume thickness=100mm, LL=1.5



     