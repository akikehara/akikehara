from vpython import *
#GlowScript 3.2 VPython
from vpython import *
from math import *
from random import *
import scipy.special as sp_s

##1 setup buttons
##2 place atoms and assign quantities to those atoms
#3 place springs
##4 give some ground state energy (i.e. momentum)
#  even before add quanta, will vibrate b/c momentum will 
#  cause pos to change and thus there to be a force.
#5 now link in the quanta information to update momentum
#6 finally, determine the entropy and make some plots

# Constants
N_A = 6.022e23# [mol^-1] Avagadro's number\n",
hbar = 1.05e-34# [kg m^2 /s] Planck's reduced constant\n",
kb = 1.38e-23# [J/K] Boltzmann constant\n",
l = 5e-10# length of spring [m]  (separation of atoms)\n",
dt = 1e-14# [s] Time step\n",
t = 0# [s] Initial time\n",
N = 3# number of oscillators in each atom\n",
    
    # Create Al atom\n",
Al = sphere(color=color.blue, radius=143e-12, pos=vec(-l,0,0))
    
    #2 Do the same for Pb, put it a \"+l\", think about how the radius migth differ from Al.\n",
Pb = sphere(color=color.orange, radius =202e-12, pos=vec(l,0,0))
   
    
    ##########################################################################################
    # Button 1 - Add one quanta to each atom in a random direction\n",
def click1(evt):
    global Al_dq, Pb_dq
    i = randint(0,2)
    Al_dq[i] = 1
    Pb_dq[i] = 1
        
    # Button 2 - Add 5 Al quanta to each atom in a random direction\n",
def click2(evt):
    global Al_dE, Pb_dE, Al_dq, Pb_dq
    i = randint(0,2)
    Al_dq[i] = 5
    Pb_dq[i] = (5*Al_dE/Pb_dE) # This should be the lowest integer energy for Pb above 5Al quanta\n",
    
    ##########################################################################################\n",
    
Al_k = 2*16. # [N/m] Al effective spring constant\n",
Pb_k = 2*5. # [N/m] Pb effective spring constant\n",
    
    # Define energy of one quantum and mass of each atom\n",
    #  Note that I have assigned the mass as a property of the atom\n",
    #  rather than a separate variable (Al.m vs Al_m).  That is a matter\n",
    #  of taste/style.  Ideally you'd do one or the other and stick with it\n",
    #  instead of mixing.\n",
Al_m = 26.98/(N_A*1000.) #Mass of one Al atom\n",
Al_dE = hbar * sqrt(Al_k/Al_m) #Energy of one Al quantum\n",

Pb_m = 207.2/(N_A*1000.) #Mass of one Pb atom\n",
Pb_dE = hbar * sqrt(Pb_k/Pb_m) #Energy of one Pb quantum\n",
    
Al_spring = []
    #  y spring at -l in x, start spring distance l from mass\n",
    #  N.B.  That is an \"ell\" and not a \"one\"\n",
Al_spring.append(helix(pos=vec(0,0,0), axis=vec(-l,0,0), radius=0.5e-10))
    #3 And for the other 5 springs\n",
Al_spring.append(helix(pos=vec(-2*l,0,0), axis=vec(l,0,0), radius=0.5e-10))
Al_spring.append(helix(pos=vec(-l,l,0), axis=vec(0,-l,0), radius=0.5e-10))
Al_spring.append(helix(pos=vec(-l,-l,0), axis=vec(0,l,0), radius=0.5e-10))
Al_spring.append(helix(pos=vec(-l,0,l), axis=vec(0,0,-l), radius=0.5e-10))
Al_spring.append(helix(pos=vec(-l,0,-l), axis=vec(0,0,l), radius=0.5e-10))
   
    #3 And for Pb\n", 
Pb_spring =[]
Pb_spring.append(helix(pos=vec(0,0,0), axis=vec(-l,0,0), radius=0.5e-10))
    #3 And for the other 5 springs\n",
Pb_spring.append(helix(pos=vec(2*l,0,0), axis=vec(l,0,0), radius=0.5e-10))
Pb_spring.append(helix(pos=vec(l,l,0), axis=vec(0,-l,0), radius=0.5e-10))
Pb_spring.append(helix(pos=vec(l,-l,0), axis=vec(0,l,0), radius=0.5e-10))
Pb_spring.append(helix(pos=vec(l,0,l), axis=vec(0,0,-l), radius=0.5e-10))
Pb_spring.append(helix(pos=vec(l,0,-l), axis=vec(0,0,l), radius=0.5e-10))
#3 You might add some walls too!
walls = []
walls.append(box(pos=vec(0,0,-l),size = vec(4*l, 2*l,.01*l)))
walls.append(box(pos=vec(-2*l,0,0),size =vec(.01*l,2*l,2*l)))
walls.append(box(pos=vec(2*l,0,0),size = vec(.01*l,2*l,2*l)))
walls.append(box(pos=vec(0,l,0),size = vec(4*l,.01*l,2*l)))
walls.append(box(pos=vec(0,-l,0),size= vec(4*l,.01*l,2*l)))
walls.append(box(pos=vec(0,0,0),size=vec(.01*l,2*l,2*l)))
             
# Make buttons\n",
b1 = button(text='Single Quanta', bind=click1)
scene.append_to_caption
b2 = button(text='5 Al quanta', bind=click2)
scene.append_to_caption # Button for energy of 5 (Al) quanta\n",\
    
    # Initial quanta\n",
Al_quanta = vector(0,0,0) #none in each direction\n",
Al_dq = [0,0,0] #how many to add for this click\n",
    
    #1 Same for Pb\n",
Pb_quanta = vector(0,0,0)
Pb_dq = [0,0,0]
    
    # Labels\n",
Al_label = label(pos=vec(-l,1.2*l,0), text='Quanta in Al: '+str(Al_quanta), border=1)
Pb_label = label(pos=vec(l,-1.2*l,0), text='Quanta in Pb: '+str(Pb_quanta), border=1)
    
    # Initial energies (ground state)\n",
Al_energy = .5 * Al_dE * vec(1,1,1)  #One half of the ground state energy (for each oscillator)\n"
Pb_energy = .5 * Pb_dE * vec(1,1,1)
    
    # Initial momenta\n",
Al.p = vec(sqrt(2 * Al_m * Al_energy.x),sqrt(2*Al_m*Al_energy.y),sqrt(2*Al_m*Al_energy.z)) 
Pb.p = sqrt(2 * Pb_m * Pb_energy.x) * vec(1,1,1)
    
    # Initialize plot\n",
g1 = graph(width=1000, xmin=0, xmax=3e-18, ymin=0, ymax=12e-22, title='Entropy vs. Energy', xtitle='Energy (J)', ytitle='Entropy (J/K)')  #think about what good values for xmin, xmax, ymin, ymax would be\n",
Al_plot = gcurve(graph=g1, color=color.blue)
Pb_plot = gcurve(graph=g1, color=color.yellow)


while True:
    sleep(1/100.)
    #rate(100)
        # Reset forces to 0\n",
    Al.F = vector(0,0,0)
    Pb.F = vector(0,0,0)
        
        # Calculate new force on each atom\n",
            #  Determine force from -kx where x is diff b/w new and old position\n",
            #  Remeber that the tethered end of the spring is the side away from the atom\n",
        #  and that there is no force for the spring at its \"rest\" lenth (l)\n",
        #  You want the total vector force due to all the springs.\n",
        #  This is probably the trickiest step\n",
        
    for i in range(6):
        a = (Al.pos-Al_spring[i].pos)
        b = (Pb.pos-Pb_spring[i].pos)
        Al.F = Al.F + (-Al_k) * (mag(a)-l) * norm(a)
        Pb.F = Pb.F + (-Pb_k) *(mag(b)-l) * norm(b)
        
        # Update momentum of atoms\n",
    Al.p = Al.p + Al.F * dt
    Pb.p = Pb.p + Pb.F * dt
    
        # Update position of atoms\n",
    Al.pos = Al.pos + (Al.p / Al_m) * dt
    Pb.pos = Pb.pos + (Pb.p / Pb_m) * dt 
    
        # Update spring axes (length of springs)\n",
        #   Careful to move the correct end of each spring.n\n",
        
    for i in range(6):
        Al_spring[i].axis = Al.pos - Al_spring[i].pos
        Pb_spring[i].axis = Pb.pos - Pb_spring[i].pos
        
            
        # Check to see if button has been pressed\n",
    if Al_dq != [0,0,0]:
            # Update quanta\n",
        Al_quanta += vec(Al_dq[0],Al_dq[1],Al_dq[2])
        Pb_quanta += vec(Pb_dq[0],Pb_dq[1],Pb_dq[2])
            # To see if step 1 is working.  Can take this out in Step 2\n",
            # Note that this isn't a tally of the total quanta, just\n",
            # an indication of what oscillator the last one was placed.\n",
        print(Al_dq)
            # Update energy\n",
        Al_energy = Al_energy + Al_quanta * Al_dE
        Pb_energy = Pb_energy + Pb_quanta * Pb_dE
            # Update momentum\n",
#         Al.p = Al.p + Al.F * dt
#         Pb.p = Pb.p + Pb.F * dt
            # Update labels\n",
        Al_label.text = 'Quanta in Al: '+str(Al_quanta)
        Pb_label.text = 'Quanta in Pb: '+str(Pb_quanta)
            # Calculate number of microstates in each atom
        n = N + Al_quanta.x + Al_quanta.y + Al_quanta.z -1
        Al_Omega = combin(n, Al_quanta.x) #think about what \"n\" and \"r\" should be.  See Section 12.7
        Pb_Omega = combin((N + (Pb_quanta.x + Pb_quanta.y + Pb_quanta.z) - 1), Al_quanta.x)
            # Calculate entropy
        Al_S = kb * log(Al_Omega)
        Pb_S = kb * log(Pb_Omega)
        
    
            # Plot entropy as a function of energy\n",
        Al_plot.plot(pos=((Al_energy.x +Al_energy.y+Al_energy.z),Al_S)) #Now plot entropy vs energy (Note that you can't sum vector components)
            #6 and for Pb
        Pb_plot.plot(pos=((Pb_energy.x + Pb_energy.y + Pb_energy.z),Pb_S))
            # Reset dq
        Al_dq = [0,0,0]
        Pb_dq = [0,0,0]