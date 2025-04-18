#!/usr/bin/env python3

import multiprocessing
import time
import math
from cpu_temp import get_cpu_temperature

def stress_cpu():
    """Function to stress CPU by performing heavy calculations"""
    while True:
        # Perform heavy calculations
        for _ in range(1000000):
            math.sqrt(math.pi * math.pi)

def monitor_temperature(duration, interval=1):
    """Monitor CPU temperature during stress test"""
    print(f"Starting temperature monitoring for {duration} seconds...")
    print("Time (s)\tTemperature (°C)")
    print("-" * 30)
    
    start_time = time.time()
    while time.time() - start_time < duration:
        temp = get_cpu_temperature()
        elapsed = time.time() - start_time
        print(f"{elapsed:.1f}\t\t{temp:.1f}")
        time.sleep(interval)

def main():
    # Get number of CPU cores
    num_cores = multiprocessing.cpu_count()
    print(f"Detected {num_cores} CPU cores")
    
    # Create stress processes
    processes = []
    for _ in range(num_cores):
        p = multiprocessing.Process(target=stress_cpu)
        p.daemon = True
        processes.append(p)
    
    try:
        # Start stress processes
        print("Starting CPU stress test...")
        for p in processes:
            p.start()
        
        # Monitor temperature for 5 minutes
        monitor_temperature(duration=300, interval=2)
        
    except KeyboardInterrupt:
        print("\nStopping stress test...")
    finally:
        # Clean up processes
        for p in processes:
            p.terminate()
        print("Stress test completed.")

if __name__ == "__main__":
    main() 