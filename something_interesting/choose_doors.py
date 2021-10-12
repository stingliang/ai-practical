# -*- coding: utf-8 -*-

# @File        : choose_doors.py
# @CreateDate  : 2021-10-12
# @Author      : stingliang
# @Github      : https://github.com/stingliang
# @UpdateTime  : 2021-10-12 17:41

import random


def door_and_prize_sim(switch, loop_num):
    win, total = 0, 0

    for loop in range(loop_num):

        if loop % 1000 is 0:
            print('\rCalculate progress: %.2f%%' % ((loop / loop_num) * 100), end='')

        # game rule
        prize = random.randint(0, 2)
        init_choice = random.randint(0, 2)
        doors = [0, 1, 2]
        doors.remove(prize)

        # if miss
        if init_choice in doors:
            doors.remove(init_choice)

        # open the door without prize
        n = len(doors)
        r = random.randint(0, n - 1)
        open_door = doors[r]

        if switch:
            second_choice = 3 - open_door - init_choice
        else:
            second_choice = init_choice

        total += 1
        if second_choice is prize:
            win += 1

    print('\rCalculate progress: 100.0%')
    return win / total


if __name__ == '__main__':
    rotation_times = 100 * 10000
    print('when switch, the wining rate is: ', door_and_prize_sim(True, rotation_times))
    print('when not switch, the wining rate is: ', door_and_prize_sim(False, rotation_times))
