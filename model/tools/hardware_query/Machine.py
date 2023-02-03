from sys import platform
import multiprocessing
# from os import system

class Machine:
    '''
    '''
    def __init__(
        self, platform,
        host_cpu_cores, host_clock_frequency, host_peak_flops, host_mem_bandwidth,
        snic_cpu_cores, snic_clock_frequency, snic_mem_bandwidth, pcie_bandwidth,
        pcie_lanes, interconnect_bandwidth
    ):
        self.platform = platform
        self.host_cpu_cores = host_cpu_cores
        self.host_clock_frequency = host_clock_frequency
        self.host_peak_flops = host_peak_flops
        self.host_mem_bandwidth = host_mem_bandwidth
        self.snic_cpu_cores = snic_cpu_cores
        self.snic_clock_frequency = snic_clock_frequency
        self.snic_mem_bandwidth = snic_mem_bandwidth
        self.pcie_bandwidth = pcie_bandwidth
        self.pcie_lanes = pcie_lanes
        self.interonnect_bandwidth = interconnect_bandwidth

        
    def __str__(self):
        return f"{self.platform}"
 
##################################################
#                  Getters
##################################################
    def get_platform(self): return self.platform
    def get_host_cpu_cores(self): return self.host_cpu_cores
    def get_host_clock_frequency(self): return self.host_clock_frequency
    def get_host_peak_flops(self): return self.host_peak_flops
    def get_host_mem_bandwidth(self): return self.host_mem_bandwidth
    def get_snic_cpu_cores(self): return self.snic_cpu_cores
    def get_snic_clock_frequency(self): return self.snic_clock_frequency
    def get_snic_mem_bandwidth(self): return self.snic_mem_bandwidth
    def get_pcie_bandwidth(self): return self.pcie_bandwidth
    def get_pcie_lanes(self): return self.pcie_lanes
    
##################################################
#                  Setters 
##################################################
    def set_platform(self, platform): self.platform = platform
    def set_host_cpu_cores(self, host_cpu_cores): self.host_cpu_cores = host_cpu_cores
    def set_host_clock_frequency(self, host_clock_frequency): self.host_clock_frequency = host_clock_frequency
    def set_host_peak_flops(self, host_peak_flops): self.host_peak_flops = host_peak_flops
    def set_host_mem_bandwidth(self, host_mem_bandwidth): self.host_mem_bandwidth = host_mem_bandwidth
    def set_snic_cpu_cores(self, snic_cpu_cores): self.snic_cpu_cores = snic_cpu_cores
    def set_snic_clock_frequency(self, snic_clock_frequency): self.snic_clock_frequency = snic_clock_frequency
    def set_snic_mem_bandwidth(self, snic_mem_bandwidth): self.snic_mem_bandwidth = snic_mem_bandwidth
    def set_pcie_bandwidth(self, pcie_bandwidth): self.pcie_bandwidth = pcie_bandwidth
    def set_pcie_lanes(self, pcie_lanes): self.pcie_lanes = pcie_lanes

##################################################
#               Helper functions
##################################################
    def print_all(self):
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
    
    def query_platform(self):
        return platform
    
    def query_host_cpu_cores(self):
        '''
        Return the number of CPU cores on the host
        '''
        return multiprocessing.cpu_count()
    
    # def query_host_clock_frequency(self):
    #     return os.system(lscpu | grep "MHz")