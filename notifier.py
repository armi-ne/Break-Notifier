import time
import winsound
from datetime import datetime
from win10toast import ToastNotifier

toaster = ToastNotifier()
counter = 0

# Input and setting values to use later on for time & counter
wait_time_input = int(input("Time interval (in seconds) between rests: "))
rest_time = int(input("Duration of rest time (in seconds): "))
super_time = int(input("Duration of super rest time (in seconds, happens every hour): "))
wait_time = wait_time_input - rest_time
wait_time_super = wait_time_input - super_time
counter_number_to_check = int(60/(wait_time/60))
overall_breaks = 0
normal_breaks = 0
super_breaks = 0
time_spent_on_breaks = 0
launched_time = datetime.now()

def data_presenter(overall_breaks_counter, normal_breaks, super_breaks, time_spent_on_breaks, launched_time):
    print("\n")
    print("I was launched on: " + str(launched_time) + ".")
    print("So far, you've had {0} minute(s) and {1} seconds worth of breaks.".format(str((time_spent_on_breaks//60)), str((time_spent_on_breaks%60))))
    print("You've had a total of {0} break(s), of which {1} were/was regular and {2} were/was super.".format(str(overall_breaks_counter), str(normal_breaks), str(super_breaks)))


def counter_checker(counter_number):
    if counter_number == counter_number_to_check:
        answer = "Yes"
        return answer
    else:
        answer = "No"
        return answer

while True:
    counter += 1
    check = counter_checker(counter)
    if check == "Yes": # Super Wait
        winsound.PlaySound('C:/Users/Armi-ne/Dropbox/Coding/Coding Projects/Python/Break Notifier/alert.wav', winsound.SND_FILENAME)
        toaster.show_toast(title = "Super Break time!", msg = "Stop looking at screen for {0} second(s)!" .format(super_time))
        time.sleep(super_time)
        winsound.PlaySound('C:/Users/Armi-ne/Dropbox/Coding/Coding Projects/Python/Break Notifier/alert.wav', winsound.SND_FILENAME)
        overall_breaks += 1
        super_breaks += 1
        time_spent_on_breaks += super_time
        data_presenter(overall_breaks, normal_breaks, super_breaks, time_spent_on_breaks, launched_time)
        time.sleep(wait_time_super)
        counter = 0
    elif check == "No": # Short Wait
        winsound.PlaySound('C:/Users/Armi-ne/Dropbox/Coding/Coding Projects/Python/Break Notifier/alert.wav', winsound.SND_FILENAME)
        toaster.show_toast(title = "Break time!", msg = "Close your eyes for {0} second(s)!" .format(rest_time))
        time.sleep(rest_time)
        winsound.PlaySound('C:/Users/Armi-ne/Dropbox/Coding/Coding Projects/Python/Break Notifier/alert.wav', winsound.SND_FILENAME)
        overall_breaks += 1
        normal_breaks += 1
        time_spent_on_breaks += rest_time
        data_presenter(overall_breaks, normal_breaks, super_breaks, time_spent_on_breaks, launched_time)
        time.sleep(wait_time)
    else:
        print("Pleb")
