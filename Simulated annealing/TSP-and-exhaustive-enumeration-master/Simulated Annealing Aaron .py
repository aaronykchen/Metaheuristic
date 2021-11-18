"""
Simulated Annealing for TSP:
the several nodes city and exhaustive enumeration
By @Aaron YuKu Chen

"""
import pandas as pd
import numpy as np
import random
import math

num_of_city = 8


# Generate the random cities locations
def initial_cityLocation():
    zero_distance = np.zeros((num_of_city, num_of_city), dtype=np.int)
    for i in range(num_of_city):
        for j in range(num_of_city):
            if i < j:
                temp_dis = random.randint(10, 90)
                zero_distance[i][j], zero_distance[j][i] = temp_dis, temp_dis
    return zero_distance


cities_Location = initial_cityLocation()  # generate the initial cities locations
print(cities_Location)

###############################################################################################################
# the exhaustive enumeration
sum_temp = 1
for i in range(1, num_of_city):
    sum_temp *= i
print("Number of EXPECT Solutions: ", sum_temp)

the_shortest_distance = 1000
the_count_time = 0
the_shortest_path = []
for leg_01 in range(1, num_of_city):
    the_path_leg01 = [0]
    # print("in this round, the shortest distance: ", the_shortest_distance)
    distance_part01 = cities_Location[0][leg_01]
    # print('distance part01: ', distance_part01)
    the_path_leg01.append(leg_01)
    for leg_02 in range(1, num_of_city):
        the_path_leg02 = [0, leg_01]
        # print("in this round, the shortest distance: ", the_shortest_distance)
        if leg_02 < leg_01:
            distance_part02 = distance_part01 + cities_Location[leg_01][leg_02]
        elif leg_02 > leg_01:
            distance_part02 = distance_part01 + cities_Location[leg_01][leg_02]
        else:
            continue
        the_path_leg02.append(leg_02)
        # print('distance part02: ', distance_part02)
        for leg_03 in range(1, num_of_city):
            the_path_leg03 = [0, leg_01, leg_02]
            if leg_03 < leg_02 and leg_03 != leg_01:
                distance_part03 = distance_part02 + cities_Location[leg_02][leg_03]
            elif leg_03 > leg_02 and leg_03 != leg_01:
                distance_part03 = distance_part02 + cities_Location[leg_02][leg_03]
            else:
                continue
            the_path_leg03.append(leg_03)
            # print('NO.3:',distance_part03)
            for leg_04 in range(1, num_of_city):
                the_path_leg04 = [0, leg_01, leg_02, leg_03]
                if leg_04 < leg_03 and leg_04 != leg_01 and leg_04 != leg_02:
                    distance_part04 = distance_part03 + cities_Location[leg_03][leg_04]
                elif leg_04 > leg_03 and leg_04 != leg_01 and leg_04 != leg_02:
                    distance_part04 = distance_part03 + cities_Location[leg_03][leg_04]
                else:
                    continue
                the_path_leg04.append(leg_04)
                # print('NO.4__:', distance_part04)
                for leg_05 in range(1, num_of_city):
                    the_path_leg05 = [0, leg_01, leg_02, leg_03, leg_04]
                    if leg_05 < leg_04 and leg_05 != leg_01 and leg_05 != leg_02 and leg_05 != leg_03:
                        distance_part05 = distance_part04 + cities_Location[leg_04][leg_05]
                    elif leg_05 > leg_04 and leg_05 != leg_01 and leg_05 != leg_02 and leg_05 != leg_03:
                        distance_part05 = distance_part04 + cities_Location[leg_04][leg_05]
                    else:
                        continue
                    the_path_leg05.append(leg_05)
                    # print("NO.5:  ", distance_part05)
                    for leg_06 in range(1, num_of_city):
                        the_path_leg06 = [0, leg_01, leg_02, leg_03, leg_04, leg_05]
                        if leg_06 < leg_05 and leg_06 != leg_01 and leg_06 != leg_02 and leg_06 != leg_03 and leg_06 != leg_04:
                            distance_part06 = distance_part05 + cities_Location[leg_05][leg_06]
                        elif leg_06 > leg_05 and leg_06 != leg_01 and leg_06 != leg_02 and leg_06 != leg_03 and leg_06 != leg_04:
                            distance_part06 = distance_part05 + cities_Location[leg_05][leg_06]
                        else:
                            continue
                        the_path_leg06.append(leg_06)
                        # print('NO.6: ', distance_part06)
                        for leg_07 in range(1, num_of_city):
                            the_path_leg07 = [0, leg_01, leg_02, leg_03, leg_04, leg_05, leg_06]
                            if leg_07 < leg_06 and leg_07 != leg_01 and leg_07 != leg_02 and leg_07 != leg_03 and leg_07 != leg_04 and leg_07 != leg_05:
                                distance_part07 = distance_part06 + cities_Location[leg_06][leg_07]
                            elif leg_07 > leg_06 and leg_07 != leg_01 and leg_07 != leg_02 and leg_07 != leg_03 and leg_07 != leg_04 and leg_07 != leg_05:
                                distance_part07 = distance_part06 + cities_Location[leg_06][leg_07]
                            else:
                                continue
                            the_path_leg07.append(leg_07)
                            # print("NO.7: ", distance_part07)
                            for leg_08 in range(num_of_city):
                                the_path_leg08 = [0, leg_01, leg_02, leg_03, leg_04, leg_05, leg_06, leg_07]
                                if leg_08 != leg_07 and leg_08 != leg_06 and leg_08 != leg_05 and leg_08 != leg_04 and leg_08 != leg_03 and leg_08 != leg_02 and leg_08 != leg_01:
                                    distance_part08 = distance_part07 + cities_Location[leg_07][0]
                                else:
                                    continue
                                the_path_leg08.append(leg_08)
                                the_total_path = [x + 1 for x in the_path_leg08]
                                # print('Path: ', the_total_path, ' and their distance: ', distance_part08)
                                the_count_time += 1
                                if distance_part08 < the_shortest_distance:
                                    the_shortest_distance = distance_part08
                                    the_shortest_path = the_total_path

# print('Real count time: ', the_count_time)
print('Shortest Path: ', the_shortest_path, 'and their distance: ', the_shortest_distance)
#################################################################################################################
