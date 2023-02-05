# Library imports
from sys import platform
import multiprocessing
# from os import system

##########################################################
#                     Machine class
##########################################################
class Machine:
    '''
    Machine class for storing all hardware features
    '''
    def __init__(
        self, platform,
        host_cpu_cores, host_clock_frequency, host_peak_flops, host_mem_bandwidth,
        snic_cpu_cores, snic_clock_frequency, snic_peak_flops, snic_mem_bandwidth,
        pcie_bandwidth, pcie_lanes, interconnect_bandwidth
    ):
        self.platform = platform
        self.host_cpu_cores = host_cpu_cores
        self.host_clock_frequency = host_clock_frequency
        self.host_peak_flops = host_peak_flops
        self.host_mem_bandwidth = host_mem_bandwidth
        self.snic_cpu_cores = snic_cpu_cores
        self.snic_clock_frequency = snic_clock_frequency
        self.snic_peak_flops = snic_peak_flops
        self.snic_mem_bandwidth = snic_mem_bandwidth
        self.pcie_bandwidth = pcie_bandwidth
        self.pcie_lanes = pcie_lanes
        self.interonnect_bandwidth = interconnect_bandwidth
 
#=====================================================
#  Getters
#=====================================================   
    def get_platform(self): return self.platform
    def get_host_cpu_cores(self): return self.host_cpu_cores
    def get_host_clock_frequency(self): return self.host_clock_frequency
    def get_host_peak_flops(self): return self.host_peak_flops
    def get_host_mem_bandwidth(self): return self.host_mem_bandwidth
    def get_snic_cpu_cores(self): return self.snic_cpu_cores
    def get_snic_clock_frequency(self): return self.snic_clock_frequency
    def get_snic_peak_flops(self): return self.snic_peak_flops
    def get_snic_mem_bandwidth(self): return self.snic_mem_bandwidth
    def get_pcie_bandwidth(self): return self.pcie_bandwidth
    def get_pcie_lanes(self): return self.pcie_lanes
    
#=====================================================
#  Setters
#=====================================================
    def set_platform(self, platform): self.platform = platform
    def set_host_cpu_cores(self, host_cpu_cores): self.host_cpu_cores = host_cpu_cores
    def set_host_clock_frequency(self, host_clock_frequency): self.host_clock_frequency = host_clock_frequency
    def set_host_peak_flops(self, host_peak_flops):self.host_peak_flops = host_peak_flops
    def set_host_mem_bandwidth(self, host_mem_bandwidth): self.host_mem_bandwidth = host_mem_bandwidth
    def set_snic_cpu_cores(self, snic_cpu_cores): self.snic_cpu_cores = snic_cpu_cores
    def set_snic_clock_frequency(self, snic_clock_frequency): self.snic_clock_frequency = snic_clock_frequency
    def set_snic_peak_flops(self, snic_peak_flops): self.snic_peak_flops = snic_peak_flops
    def set_snic_mem_bandwidth(self, snic_mem_bandwidth): self.snic_mem_bandwidth = snic_mem_bandwidth
    def set_pcie_bandwidth(self, pcie_bandwidth): self.pcie_bandwidth = pcie_bandwidth
    def set_pcie_lanes(self, pcie_lanes): self.pcie_lanes = pcie_lanes
    
#=====================================================
#  Functions for querying the Machine class attributes
#=====================================================
# Platform
    def query_platform(self):
        '''
        Return the platform OS
        '''
        return platform
    
# Host features    
    def query_host_cpu_cores(self):
        '''
        Return the number of CPU cores on the host
        '''
        return multiprocessing.cpu_count()
    
    def query_host_clock_frequency(self):
        '''
        Return host clock frequency
        TODO:
        '''
        
    def query_host_peak_flops(self):
        '''
        Return the peak FLOP/s of the host CPU
        TODO:
        '''
        
    def query_host_mem_bandwidth(self):
        '''
        Return the host CPU's memory bandwidth    
        TODO:
        '''
        
# SmartNIC features
    def query_snic_cpu_cores(self):
        '''
        Return the number of CPU cores on the SmartNIC
        TODO:
        '''
        
    def query_snic_clock_frequency(self):
        '''
        Return the clock of frequency of the SmartNIC
        TODO:
        '''
        
    def query_snic_peak_flops(self):
        '''
        Return the peak FLOP/s of the SmartNIC's CPU
        TODO:
        '''
           
    def query_snic_mem_bandwidth(self):
        '''
        Return the memory bandwidth of the SmartNIC's CPU
        TODO:
        '''
          
# PCIe bus and interconnect
    def query_pcie_bandwidth(self):
        '''
        Return the PCIe bus bandwidth
        TODO:
        '''
        
    def query_pcie_lanes(self):
        '''
        Return the number of PCIe lanes
        TODO:
        '''
          
    def query_interconect_bandwidth(self):
        '''
        Return the interconnect bandwidth
        TODO:
        '''
        
#=====================================================
#  Helper functions
#=====================================================
    def __str__(self):
        '''
        Return the following attributes as a string:
            - platform
        '''
        # TODO: complete this
        return f"{self.platform}"

    def print_all(self):
        '''
        Print all attributes of the Machine class
        '''
        print(
            "------------------------------------------------------------\n"
            f"Platform:\t\t\t{self.get_platform()}\n"
            "------------------------------------------------------------\n"
            f"Host CPU Cores:\t\t\t{self.get_host_cpu_cores()}\n"
            f"Host Clock Frequency:\t\t{self.get_host_clock_frequency()}\n"
            f"Host Peak FLOP/s:\t\t{self.get_host_peak_flops()}\n"
            f"Host Memory Bandwidth:\t\t{self.get_host_mem_bandwidth()}\n\n" 
            f"SmartNIC CPU Cores:\t\t{self.get_snic_cpu_cores()}\n"
            f"SmartNIC Clock Frequency:\t{self.get_snic_clock_frequency()}\n"
            f"SmartNIC Peak FLOP/s:\t{self.get_snic_peak_flops()}\n"
            f"SmartNIC Memory Bandeidth:\t{self.get_snic_mem_bandwidth()}\n\n"
            f"PCIe Bandwidth:\t\t\t{self.get_pcie_bandwidth()}\n"
            f"PCIe Lanes:\t\t\t{self.get_pcie_lanes()}\n"
            "------------------------------------------------------------\n"
        )
    
    def check_if_linux(self, platform):
        '''
        Return true if the system is running linux, false if otherwise
        '''
        if platform == "linux" or platform == "linux2":
            return True
        else:
            return False