
'''
Adam Becker
1620
12/09/2024
'''
'''
These are the loads and axle locations for the given loads.
Assumed x axis location is positive to the right with 0 being
the start of the span and the end of the span being span_length.
Loads start at 0 and progress to the left simuluating a train
that is about to enter a bridge span from left and progress right.
'''
alt_load = (100, 100, 100, 100)
alt_loc = (0, -5, -11, -16)

e10_axleLoc = (-0.001, -8.001, -13.001, -18.001, -23.001, -32.001, -37.001, -43.001, -48.001, -56.001, -64.001, -69.001, -74.001, -79.001, -88.001, -93.001, -99.001, -104.001, -111.001, -115.001, -119.001, -123.001, -127.001, -131.001, -135.001, -139.001, -143.001, -147.001, -151.001, -155.001, -159.001, -163.001, -167.001, -171.001, -175.001, -179.001, -183.001, -187.001, -191.001, -195.001, -199.001, -203.001, -207.001, -211.001, -215.001, -219.001, -223.001, -227.001, -231.001, -235.001, -239.001, -243.001, -247.001, -251.001, -255.001, -259.001, -263.001, -267.001, -271.001, -275.001, -279.001, -283.001, -287.001, -291.001, -295.001, -299.001, -303.001, -307.001, -311.001, -315.001, -319.001, -323.001, -327.001, -331.001, -335.001, -339.001, -343.001, -347.001, -351.001, -355.001, -359.001, -363.001, -367.001, -371.001, -375.001, -379.001, -383.001, -387.001, -391.001, -395.001, -399.001, -403.001, -407.001, -411.001, -415.001, -419.001, -423.001, -427.001, -431.001, -435.001, -439.001, -443.001, -447.001, -451.001, -455.001, -459.001, -463.001, -467.001, -471.001, -475.001, -479.001, -483.001, -487.001, -491.001, -495.001, -499.001, -503.001, -507.001, -511.001, -515.001, -519.001, -523.001, -527.001, -531.001, -535.001, -539.001, -543.001, -547.001, -551.001, -555.001, -559.001, -563.001, -567.001, -572.001, -578.001, -585.001, -593.001, -602.001)
e10_ld =  (5, 10, 10, 10, 10, 6.5, 6.5, 6.5, 6.5, 5, 10, 10, 10, 10, 6.5, 6.5, 6.5, 6.5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4)
e5_ld = (2.5, 5, 5, 5, 5, 3.25, 3.25, 3.25, 3.25, 2.5, 5, 5, 5, 5, 3.25, 3.25, 3.25, 3.25, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2)
e80_ld = (40, 80, 80, 80, 80, 52, 52, 52, 52, 40, 80, 80, 80, 80, 52, 52, 52, 52, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32)
e40_ld = (20, 40, 40, 40, 40, 26, 26, 26, 26, 20, 40, 40, 40, 40, 26, 26, 26, 26, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16)

UP286a_axleLoc = (0, -5.8333, -26.3749, -32.2082, -38.8748, -44.7081, -65.2497, -71.083, -77.7496, -83.5829, -104.1245, -109.9578, -116.6244, -122.4577, -142.9993, -148.8326, -155.4992, -161.3325, -181.8741, -187.7074, -194.374, -200.2073, -220.7489, -226.5822, -233.2488, -239.0821, -259.6237, -265.457, -272.1236, -277.9569, -298.4985, -304.3318, -310.9984, -316.8317, -337.3733, -343.2066, -349.8732, -355.7065, -376.2481, -382.0814, -388.748, -394.5813, -415.1229, -420.9562, -427.6228, -433.4561, -453.9977, -459.831, -466.4976, -472.3309, -492.8725, -498.7058, -505.3724, -511.2057, -531.7473, -537.5806, -544.2472, -550.0805, -570.6221, -576.4554, -583.122, -588.9553, -609.4969, -615.3302)
UP286a_ld =  (71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5, 71.5)

UP268a_ld = (67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67)
UP268a_axleLoc = (0, -5.833, -23.938, -29.771, -36.438, -42.271, -60.375, -66.208, -72.875, -78.708, -96.813, -102.646, -109.313, -115.146, -133.25, -139.083, -145.75, -151.583, -169.688, -175.521, -182.188, -188.021, -206.125, -211.958, -218.625, -224.458, -242.563, -248.396, -255.063, -260.896, -279, -284.833, -291.5, -297.333, -315.438, -321.271, -327.938, -333.771, -351.875, -357.708, -364.375, -370.208, -388.313, -394.146, -400.813, -406.646, -424.75, -430.583, -437.25, -443.083, -461.188, -467.021, -473.688, -479.521, -497.625, -503.458, -510.125, -515.958, -534.063, -539.896, -546.563, -552.396, -570.5, -576.333)

UP315a_ld = (78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8, 78.8)
UP315a_axleLoc = (0, -5.833, -30.313, -36.146, -42.813, -48.646, -73.125, -78.958, -85.625, -91.458, -115.938, -121.771, -128.438, -134.271, -158.75, -164.583, -171.25, -177.083, -201.563, -207.396, -214.063, -219.896, -244.375, -250.208, -256.875, -262.708, -287.188, -293.021, -299.688, -305.521, -330, -335.833, -342.5, -348.333, -372.813, -378.646, -385.313, -391.146, -415.625, -421.458, -428.125, -433.958, -458.438, -464.271, -470.938, -476.771, -501.25, -507.083, -513.75, -519.583, -544.063, -549.896, -556.563, -562.396, -586.875, -592.708, -599.375, -605.208, -629.688, -635.521, -642.188, -648.021, -672.5, -678.333)

def span_results(load, spacing, l):
    '''
    This program runs the ll_span_reaction definition for sections of the span
    from the start (0%) to midspan (50%) with increments of 5% of the span length.
    :param load: This is the selected load being analyzed.
    :param spacing: This is the axle location of the design load.
    :param l: l represents the span length
    :return: a full list of shear and moment results for all sections of interest on the span
    '''
    beam_results = []
    for s in range(0, 51, 5):
        x = (s * 0.01) * l
        beam_results.append(ll_span_reactions(load,spacing,l,x))
    return beam_results

def ll_span_reactions(axle_loads, axle_spacing, l, x):
    '''
    This definition determines the full shear and moment history of a single location on a span
    do to a train crossing it.  It checks the train axle location and impact to the section of
    interest in 3" increments across the span.  After the train has ran completely, it returns
    the max shear and moment it experienced from the entire train.
    :param axle_loads: This is the selected load being analyzed.
    :param axle_spacing: This is the axle location of the design load.
    :param l: Span length.
    :param x: This is the location along the span where shear and moment is being analyzed.
    :return: Max shear and moment at the section of interest from the entire train.
    '''
    axle_loc = list(axle_spacing)
    shift_increment = 0.25 #feet.  This is how much the train moves in every iteration.
    train_shift = shift_increment

    moment_list = []  #initialize the moment list with zero inputs
    shear_list = []     #initialize the shear list with zero inputs
    while train_shift <= (l + 100):
        '''
        This moves the load for a distance of the span length + 100' which is enough to get the train
        engines across the span in the e load configuration.
        '''
        for m in range(len(axle_loc)):
            '''shifts entire load over on the span by amount = train_shift'''
            axle_loc[m] = axle_spacing[m] + train_shift

        shear = 0.0
        moment = 0.0

        for i in range(len(axle_spacing)):
            '''determines if the axle is on the bridge and then determines the shear and moment from
            the load if the axle is on the span.
            
            Acronyms follow diagram 8 as shown in the AISC Steel Construction Manual 15th Edition,
            shear and moment diagrams - SIMPLE BEAM - CONCENTRATED LOAD AT ANY POINT
            '''

            if axle_loc[i] > l:  #true if the axle is off the bridge to the right.  Goes to next axle.
                continue
            elif axle_loc[i] <= 0:   #true if axle is off the bridge to the left.  Breaks out since all other axles will also be off the bridge.
                break
            else:
                a = axle_loc[i]
                b = l - a
                r1 = axle_loads[i] * b / l
                r2 = axle_loads[i] * a / l
                if x <= a:  #executes if the section of interest is to the left of the load
                    shear_sect_loc = r1
                    moment_sect_loc = axle_loads[i] * b * x / l
                else:  #executes if the section of interest is to the right of the load
                    shear_sect_loc = r2
                    moment_sect_loc = r2 * (l - x)

                shear += shear_sect_loc  #increments the shear by the amount generated by the load
                moment += moment_sect_loc #increments the moment by the amount generated by the load

        moment_list.append(round(moment,3))  #appends the total moment to the moment list for that specific load location
        shear_list.append(round(shear,3))  #appends the total shear to the shear list for that specific load location

        train_shift += shift_increment  #increases the train shift by 3 more inches

    beam_results = [round(x,3), max(shear_list), max(moment_list)]  #creates a list of the beam location and the max shear and moment

    return beam_results #returns the location of interest and the max shear and moment


def main():
    '''
    This section was used for initial testing of the program.
    :return:
    '''
    pass

if __name__ == '__main__':
    main()