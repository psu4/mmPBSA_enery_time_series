"""
# AMBER MMP(G)BSA Energy Terms Post Processing: MM-PBSA Energy Plot

# Written by Pin-Chih Su and Cheng-Chieh Tsai. Last modified on Nov 13,2015

# Tested in python 2.7.6, scipy-0.13.3, matplotlib.pyplot-1.3.1, and Linux Redhat 5.0/Windows 7
"""
import matplotlib.pyplot as plt

import pylab 

import os

import sys, getopt

def main(argv):
    
    inputfile = ''
   
    outputfile = ''

    plottitle = ''

    frame_number = ''
   
    try:
       
        opts, args = getopt.getopt(argv,"hi:o:t:f:",["ifile=","ofile=","title=","fnumber"])
      
    except getopt.GetoptError:
       
        print 'python mmPBSA_energy_plot.py -i <inputfile> -o <outputfile> -t <plottitle> -f <frame_number>'
      
        sys.exit(2)
      
    for opt, arg in opts:
       
        if opt == '-h':
          
            print '\n'+'(1) Usage: python mmPBSA_energy_plot.py -i <inputfile> -o <outputfile> -t <plot title> -f <frame_number>'

            print '\n'+'(2) python mmPBSA_energy_plot.py -i input.csv -o output -t title -f 2400 (the frame number in the input.csv is 2,400)'

            print '\n'+'(3) Output plots are jpg files'
            
            print '\n'+'(3) Please make sure you have python, scipy, matplotlib installed'
            
            print '\n'+'(4) Tested in python 2.7.6, matplotlib.pyplot-1.3.1, and Linux Redhat 5.0/Windows 7'

            print '\n'+'(5) Written by Dr.Pin-Chih Su and Cheng-Chieh Tsai'

            print '\n'+'(6) If you use this script, please cite: Journal of Computational Chemistry, 2015, 36,1859-1873'

            print '\n'+'(7) More details are available at https://sites.google.com/site/2015pcsu/data-science/mmpbsa'

            sys.exit()
         
        elif opt in ("-i", "--ifile"):
          
            inputfile = arg
         
        elif opt in ("-o", "--ofile"):
          
            outputfile = arg

        elif opt in ("-t", "--title"):
          
            plottitle = arg

        elif opt in ("-f", "--fnumber"):
          
            frame_number = arg
        
    filenames=open(inputfile,'r')

#Parameter Area
    VDWAALS=[]
    EEL=[]
    EPB=[]
    ENPOLAR=[]
    EDISPER=[]
    DELTAGAS=[]
    DELTASOLV=[]
    DELTATOTAL=[]

    fig = plt.figure()
    ax = fig.add_axes([0.13, 0.26, 0.8, 0.65]) # a list of [left, bottom, width, height] values in 0-1 relative figure coordinates
                                                   # More details can be seen here: http://matplotlib.org/users/transforms_tutorial.html#axes-coordinates 
    plt.ylabel("Energy (kcal/mol)", fontsize=20)
    plt.xlabel("MD Frames", fontsize=20)
    plt.title(plottitle, fontsize=13)

    file=open(inputfile,'r')
    
    line=file.readlines()
    
    for a in line:

        if 'DELTA Energy Terms' in a:
        
            tick=2
        
            while tick < int(frame_number)+1:
                    
                VDWAALS.append(line[line.index(a)+tick].split(',')[1])
                EEL.append(line[line.index(a)+tick].split(',')[2])
                EPB.append(line[line.index(a)+tick].split(',')[3])
                ENPOLAR.append(line[line.index(a)+tick].split(',')[4])
                #EDISPER.append(line[line.index(a)+tick].split(',')[5])
                #DELTAGAS.append(line[line.index(a)+tick].split(',')[6])
                DELTASOLV.append(line[line.index(a)+tick].split(',')[7])
                DELTATOTAL.append(line[line.index(a)+tick].split(',')[8])
                tick=tick+1

    line1, =ax.plot(VDWAALS,'k-')# Change your style here: {one letter color code}{line style "-" means "lines", "o" means "dot","*" means "*"} 
                                 #  More details are here: http://matplotlib.org/api/colors_api.html  
    line2, =ax.plot(EEL,'g-')
    line3, =ax.plot(EPB,'r-')
    line4, =ax.plot(ENPOLAR,'c-')
    #line5, =plt.plot(EDISPER, 'm^-')
    #line6, =plt.plot(DELTAGAS, '+-')
    line7, =ax.plot(DELTASOLV,'-')
    line8, =ax.plot(DELTATOTAL, 'y-')
    ax.legend([line1,line2,line3,line4,line7,line8], ['dGvdw','dGelec','dGPB','dGnonpolar','dGsolv','dGbind'],bbox_to_anchor=[0.5,-0.26],loc='center',ncol=3,fontsize=20)#,fancybox=True
    
    mng = plt.get_current_fig_manager()
    mng.resize(*mng.window.maxsize())
    plt.savefig(outputfile+".jpg",dpi=80)
    plt.clf()
    plt.close()

if __name__ == "__main__":
    
   main(sys.argv[1:])


