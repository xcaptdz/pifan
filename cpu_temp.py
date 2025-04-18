#!/usr/bin/env python3

def get_cpu_temperature():
    try:
        with open('/sys/class/thermal/thermal_zone0/temp', 'r') as f:
            temp = float(f.read().strip()) / 1000.0
            return temp
    except Exception as e:
        print(f"Error reading CPU temperature: {e}")
        return None

if __name__ == "__main__":
    temp = get_cpu_temperature()
    if temp is not None:
        print(f"CPU Temperature: {temp:.1f}°C") 