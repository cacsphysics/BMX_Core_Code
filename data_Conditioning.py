#Created by Carlos A. Cartagena-Sanchez
import numpy as np
import BMX
import matplotlib.pylab as plt
"""
    
"""
def Magnetic_Field_Plot(pos, shot):
    ###################################################################################################
    """ Currently I am trying to look at the data. I have some concerns on how I viewed the data
        previously. """
    ###################################################################################################

    data_Path = '04232019/'
    pico = BMX.which_Pico(pos)
    indicator = BMX.which_File(pos, shot)
    filename = data_Path + '04232019pico' + str(pico) + '/20190423-(' + indicator + ').npy'

    """
    my_Dict_1 = {'Time_B': timeB_Sec, 'Bz': Bz, 'Bt': Bt}
    """
    my_Data = np.load(filename)
    time = my_Data.item().get('Time_B')
    Bz = my_Data.item().get('Bz')

    fig = plt.figure()
    gs = fig.add_gridspec(1,1)
    fig.suptitle('Shot ' + str(shot) + ' || Position ' + str(pos) + ': 04232019scripts.py')
    
    ax = fig.add_subplot(gs[0,0])
    ax.plot(time*1e6, Bz)
    plt.show(block = True)

    return None

def Magnetic_Field_Plots(pos):
    ###################################################################################################
    """ Currently I am trying to look at the data. I have some concerns on how I viewed the data
        previously. """
    ###################################################################################################

    data_Path = '04232019/'
    pico = BMX.which_Pico(pos)
    fig = plt.figure()
    gs = fig.add_gridspec(1,1)
    fig.suptitle('Position ' + str(pos) + ': 04232019scripts.py')
    ax = fig.add_subplot(gs[0,0])
    for shot in range(1,18):
        if (shot != 9):
            indicator = BMX.which_File(pos, shot)
            filename = data_Path + '04232019pico' + str(pico) + '/20190423-(' + indicator + ').npy'
            """
            my_Dict_1 = {'Time_B': timeB_Sec, 'Bz': Bz, 'Bt': Bt}
            """
            my_Data = np.load(filename)
            time = my_Data.item().get('Time_B')
            Bz = my_Data.item().get('Bz')
            if (shot == 1):
                avg_Bz = Bz
            else:
                avg_Bz += Bz
            
            ax.plot(time*1e6, Bz, alpha = 0.5)
    ax.plot(time*1e6, avg_Bz/16, color = 'black', linewidth = 2)
    plt.show(block = True)

    return None

def Bdot_Plot():
    
    filename = '04232019/04232019pico3/20190423-0001 (1).txt'
    #pico_List = [1,2,3,4]
    starting_Index = 2000
    mean_Cutoff = 400
    
    time, Bz_1dot, Bt_1dot, Bz_2dot, Bt_2dot =  BMX.BMX_Bdot_ZT_PM(filename, starting_Index, mean_Cutoff, max_Range = 1, ending_Index = -1)

    fig = plt.figure()
    gs = fig.add_gridspec(2,2)
    fig.suptitle('Shot 1 || Pico 3: 04232019scripts.py')
    
    ax1 = fig.add_subplot(gs[0,0])
    ax1.plot(time*1e6, Bz_1dot)

    ax2 = fig.add_subplot(gs[0,1])
    ax2.plot(time*1e6, Bt_1dot)

    ax3 = fig.add_subplot(gs[1,0])
    ax3.plot(time*1e6, Bz_2dot)
    #plt.setp(ax1.get_xticklabels(), visible=False)
    
    ax4 = fig.add_subplot(gs[1,1])
    ax4.plot(time*1e6, Bt_2dot)
    #plt.setp(ax2.get_xticklabels(), visible=False)
    
    gs.tight_layout(fig)
    plt.show(block = True)

    return None

def linear_Funct(array, m, b):
    ###################################################################################################
    """ The simple line equation. """
    ###################################################################################################
    y = m*array + b

    return y

def voltage_Plot(shot_Max = 17):
    ###################################################################################################
    """ This way I can visually inspect the voltages. I found shot 9 is no good. """
    ###################################################################################################
    for i in range(1,shot_Max + 1):
        print(i)
        filename = '04232019/04232019pico4/20190423-0001 (' + str(i) + ').txt'
        #pico_List = [1,2,3,4]
        starting_Index = 2000
        mean_Cutoff = 400
        
        time, Bz_13dot, Bt_13dot, current, voltage =  BMX.BMX_Bdot_ZT_PM(filename, starting_Index, mean_Cutoff, max_Range = 1, ending_Index = -1)

        plt.figure()
        plt.plot(time*1e6, -voltage*1e3)
        plt.ylim([-3000,5000])
        title = 'Voltage S' + str(i)
        plt.title(title)
        plt.grid()
        plt.savefig('Figures/Voltage/' + title + '.png')
        plt.close
        
    return None

def which_Indictor(pico_Num, shot_Num):
    ##############################################################################################
    """ The function creates the indicator for the general window_Scan """
    ##############################################################################################    
    if (pico_Num == 1):
        indicator_1 = '(Pos1S' + str(shot_Num) + ')'
        indicator_2 = '(Pos3S' + str(shot_Num) + ')'
    elif (pico_Num == 2):
        indicator_1 = '(Pos5S' + str(shot_Num) + ')'
        indicator_2 = '(Pos7S' + str(shot_Num) + ')'
    elif (pico_Num == 3):
        indicator_1 = '(Pos9S' + str(shot_Num) + ')'
        indicator_2 = '(Pos11S' + str(shot_Num) + ')'
    elif (pico_Num == 4):
        indicator_1 = '(Pos13S' + str(shot_Num) + ')'
        indicator_2 = '(Volt_Cur' + str(shot_Num) + ')'
    else:
        print('The pico number should be 1, 2, 3, or 4.')
    
    return indicator_1, indicator_2

def load_n_Save():
    ###################################################################################################
    """ I want to run the load script and save the data for quicker return. """
    ###################################################################################################

    shot_Max = 17
    pico_List = [1, 2, 3, 4]
    starting_Index = 2000
    mean_Cutoff = 400

    for pico in pico_List:
        data_Path = '04232019/04232019pico' + str(pico) + '/'
        for shot in range(1,shot_Max + 1):
            filename = data_Path + '20190423-0001 (' + str(shot) + ').txt'
            timeB_Sec, Bz, Bt, Bz_prime, Bt_prime = BMX.BMX_Magnetic_Field_ZT_PM(filename,
                                        starting_Index = starting_Index, mean_Cutoff = mean_Cutoff,
                                        max_Range = 1)

            ###################################################################################################
            """ I am applying my polarity correction. This is based on visual inspection of the magntic field 
                data. I will add some notes on this online. This is also specific to this data set. """
            ###################################################################################################
            if (pico == 1):
    
                Bz *= -1
                Bt *= -1
    
            elif (pico == 2):
    
                Bt_prime *= -1
    
            elif(pico == 4):
                
                Bz *= -1

            else:
                
                pass

            print('Saving shot: ' + str(shot) + ' and pico: ' + str(pico))
            indicator1, indicator2 = which_Indictor(pico_Num = pico, shot_Num = shot)
            savefile1 = data_Path + '20190423-(' + indicator1 + ')'
            savefile2 = data_Path + '20190423-(' + indicator2 + ')'
            B_mag = np.sqrt(Bz**2 + Bt**2)
            B_mag_prime = np.sqrt(Bz_prime**2 + Bt_prime**2)
            my_Dict_1 = {'Time_B': timeB_Sec, 'Bz': Bz, 'Bt': Bt, 'Bmag': B_mag}
            my_Dict_2 = {'Time_B': timeB_Sec, 'Bz': Bz_prime, 'Bt': Bt_prime, 'Bmag': B_mag_prime}
            np.save(savefile1, my_Dict_1)
            np.save(savefile2, my_Dict_2)

    return None

###################################################################################################
""" Functions above this division """
###################################################################################################
load_n_Save()
#Magnetic_Field_Plots(pos = 7)
#Bdot_Plot()