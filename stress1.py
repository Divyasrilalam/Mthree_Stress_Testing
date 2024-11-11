import os
import subprocess
import logging

def memory_stress_test():
    print("Starting Memory Stress Test...")
    os.system("stress-ng --vm 1 --vm-bytes 80% -t 60s ")
    print("Memory Stress Test Completed.")

def disk_stress_test():
    print("Starting Disk Stress Test...")
    os.system("stress-ng --iomix 4 --iomix-bytes 90% --timeout 100s ")
    print("Disk Stress Test Completed.")

def network_stress_test():
    print("Starting Network Stress Test...")
    result = subprocess.run(['iperf3', '-c', '192.168.1.7', '-t', '30'], capture_output=True, text=True)
    print(result.stdout)
    print("Network Stress Test Completed.")

def cpu_stress_test():
    print("Starting CPU Stress Test...")
    os.system("stress-ng --cpu 4 --cpu-load 80 -t 60s")
    print("CPU Stress Test Completed.")

def main():
    test_type = os.getenv('STRESS_TEST_TYPE', 'network')  # Default to memory test
    if test_type == 'memory':
        memory_stress_test()
    elif test_type == 'disk':
        disk_stress_test()
    elif test_type == 'network':
        network_stress_test()
    elif test_type == 'cpu':
        cpu_stress_test()
    else:
        print(f"Invalid test type: {test_type}. Exiting...")

if __name__ == "__main__":
    main()