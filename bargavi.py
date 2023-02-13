#-------Design of overhead Circular Water Tank(Bhargavi Bilingi----------
#Library Module Used
import math 



#Data Given
volume=4.5#Lakhs Lit
concrete=30#M30
steel_grade=415#Fe415



inner_radius_circular_wall= 4250 #mm
thickness_wall =100 #mm
height_wall =3200 #mm
thickness_top_dome =75 #mm
rise_bottom_top_dome=1000#mm
thickness_bottom_dome=100#mm
rise_bottom_bottom_dome= 1500 #mm
bottom_ring_beam= 350 #mm 
free_board=150 #mm
height_staging_above_GL=25 #mm




#Total Designing Steps-5
#Step-1:- Top Dome
#Step-2:- Top Ring Beam
#Step-3:- Tank Wall
#Step-4:- Base Slab
#Step-5:- Bottom Ring Beam

#Step-1 
diameter = 12 #Assume diameter in m
tank_height = (volume*100 * 4 )/ (math.pi * (diameter**2) ) 
print("Height of Tank = ",tank_height)



#Step:-2 (Design of Top Dome)
W=1.5+0.1*concrete #assume thickness=100mm, LL=1.5



     