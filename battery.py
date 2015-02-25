#!/usr/bin/env python3

power_supply_dir = "/sys/class/power_supply/"
adapter_dir = "ADP1/"
adapter_status_file = "online"
battery_dir = "BAT1/"
battery_charge_file = "charge_now"
battery_charge_full_file = "charge_full"

def main():
    charge_now = int(open(power_supply_dir + battery_dir + battery_charge_file).read())
    charge_full = int(open(power_supply_dir + battery_dir + battery_charge_full_file).read())
    percentage = (charge_now / charge_full * 100)
    f = open(power_supply_dir + adapter_dir + adapter_status_file);
    i = int(f.read())
    if i == 1:
        print("C%3.0f%%" % percentage)
    else:
        print("B%3.0f%%" % percentage)

main()
