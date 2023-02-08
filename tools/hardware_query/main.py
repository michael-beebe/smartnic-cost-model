#!/usr/bin/env python

# Library imports
import sys

# Class imports
from Machine import Machine

# Main function
def main():
    # Instantiate our Machine class
    machine = Machine(
        platform=None,
        host_cpu_cores=None,
        host_clock_frequency=None,
        host_peak_flops=None,
        host_mem_capacity=None,
        host_mem_bandwidth=None,
        snic_cpu_cores=None,
        snic_clock_frequency=None,
        snic_peak_flops=None,
        snic_mem_capacity=None,
        snic_mem_bandwidth=None,
        pcie_bandwidth=None,
        pcie_lanes=None,
        interconnect_bandwidth=None
    )
    
    # Make sure we are on a linux platform, otherwise exit
    machine.set_platform(machine.query_platform())
    if not machine.check_if_linux(machine.get_platform()):
        print("ERROR: Must be on a linux platform!")
        sys.exit(1)
        
    # Set all class attributes at once
    # machine.query_set_all()

    # Set the number of host cpu cores
    machine.set_host_cpu_cores(machine.query_host_cpu_cores())
    
    # Set the host clock frequency
    machine.set_host_clock_frequency(machine.query_host_clock_frequency())
    
    # Set the host peak FLOP/s FIXME:
    machine.set_host_peak_flops(machine.query_host_peak_flops())
    
    # Set host memory capacity
    machine.set_host_mem_capacity(machine.query_host_mem_capacity())
    
    # TODO: Set the host mem bandwidth
    machine.set_host_mem_bandwidth(machine.query_host_mem_bandwidth())
    
    # TODO: Set the smartnic cpu cores
    machine.set_snic_cpu_cores(machine.query_snic_cpu_cores())
    
    # TODO: Set the smartnic clock frequency
    machine.set_snic_clock_frequency(machine.query_snic_clock_frequency())
    
    # TODO: set the smartnic memory capacity
    machine.set_snic_mem_capacity(machine.query_snic_mem_capacity())
    
    # TODO: Set the smartnic memory bandwidth
    machine.set_snic_mem_bandwidth(machine.query_snic_mem_bandwidth())
    
    # TODO: Set the pcie bus bandwidth
    machine.set_pcie_bandwidth(machine.query_pcie_bandwidth())
    
    # TODO: Set the number of pcie lanes
    machine.set_pcie_lanes(machine.query_pcie_lanes())
    
    # TODO: Set the interconnect bandwidth
    machine.set_interconnect_bandwidth(machine.query_interconect_bandwidth())
    
    # Print all Machine class attributes
    machine.print_all()
    
    # TODO: Write to CSV
            
    # Exit program
    sys.exit()

# Call main
if __name__ == "__main__":
    main()