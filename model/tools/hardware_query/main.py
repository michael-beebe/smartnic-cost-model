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
        host_mem_bandwidth=None,
        snic_cpu_cores=None,
        snic_clock_frequency=None,
        snic_peak_flops=None,
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

    # Set the number of host cpu cores
    machine.set_host_cpu_cores(machine.query_host_cpu_cores())
    
    # TODO: Set the host clock frequency
    
    # TODO: Set the host peak FLOP/s
    
    # TODO: Set the host mem bandwidth
    
    # TODO: Set the smartnic cpu cores
    
    # TODO: Set the smartnic clock frequency
    
    # TODO: Set the smartnic memory bandwidth
    
    # TODO: Set the pcie bus bandwidth
    
    # TODO: Set the number of pcie lanes
    
    # TODO: Set the interconnect bandwidth
    
    # Print all Machine class attributes
    machine.print_all()
    
    # Exit program
    sys.exit()

# Call main
if __name__ == "__main__":
    main()