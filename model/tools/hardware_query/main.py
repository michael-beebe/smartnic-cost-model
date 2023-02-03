#!/usr/bin/env python

# Library Imports
import sys

# Class Imports
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
    
    # Set the host clock frequency

    
    # Print all Machine class attributes
    machine.print_all()


if __name__ == "__main__":
    main()