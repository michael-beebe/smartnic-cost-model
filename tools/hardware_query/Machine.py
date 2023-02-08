# Library imports
from sys import platform
import psutil
from pypapi import papi_high, papi_low
from pypapi import events as papi_events
import time
import numpy as np

##########################################################
#                     Machine class
##########################################################
class Machine:
    '''
    Machine class for storing all hardware features
    '''
    def __init__(
        self, platform,
        host_cpu_cores, host_clock_frequency, host_peak_flops, host_mem_capacity, host_mem_bandwidth,
        snic_cpu_cores, snic_clock_frequency, snic_peak_flops, snic_mem_capacity, snic_mem_bandwidth,
        pcie_bandwidth, pcie_lanes, interconnect_bandwidth
    ):
        self.platform = platform
        self.host_cpu_cores = host_cpu_cores
        self.host_clock_frequency = host_clock_frequency
        self.host_peak_flops = host_peak_flops
        self.host_mem_capacity = host_mem_capacity
        self.host_mem_bandwidth = host_mem_bandwidth
        self.snic_cpu_cores = snic_cpu_cores
        self.snic_clock_frequency = snic_clock_frequency
        self.snic_peak_flops = snic_peak_flops
        self.snic_mem_capacity = snic_mem_capacity
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
    def get_host_mem_capacity(self): return self.host_mem_capacity
    def get_host_mem_bandwidth(self): return self.host_mem_bandwidth
    def get_snic_cpu_cores(self): return self.snic_cpu_cores
    def get_snic_clock_frequency(self): return self.snic_clock_frequency
    def get_snic_peak_flops(self): return self.snic_peak_flops
    def get_snic_mem_capacity(self): return self.snic_mem_capacity
    def get_snic_mem_bandwidth(self): return self.snic_mem_bandwidth
    def get_pcie_bandwidth(self): return self.pcie_bandwidth
    def get_pcie_lanes(self): return self.pcie_lanes
    def get_interconnect_bandwidth(self): return self.interonnect_bandwidth
    
#=====================================================
#  Setters
#=====================================================
    def set_platform(self, platform): self.platform = platform
    def set_host_cpu_cores(self, host_cpu_cores): self.host_cpu_cores = host_cpu_cores
    def set_host_clock_frequency(self, host_clock_frequency): self.host_clock_frequency = host_clock_frequency
    def set_host_peak_flops(self, host_peak_flops):self.host_peak_flops = host_peak_flops
    def set_host_mem_capacity(self, host_mem_capacity): self.host_mem_capacity = host_mem_capacity
    def set_host_mem_bandwidth(self, host_mem_bandwidth): self.host_mem_bandwidth = host_mem_bandwidth
    def set_snic_cpu_cores(self, snic_cpu_cores): self.snic_cpu_cores = snic_cpu_cores
    def set_snic_clock_frequency(self, snic_clock_frequency): self.snic_clock_frequency = snic_clock_frequency
    def set_snic_peak_flops(self, snic_peak_flops): self.snic_peak_flops = snic_peak_flops
    def set_snic_mem_capacity(self, snic_mem_capacity): self.snic_mem_capacity = snic_mem_capacity
    def set_snic_mem_bandwidth(self, snic_mem_bandwidth): self.snic_mem_bandwidth = snic_mem_bandwidth
    def set_pcie_bandwidth(self, pcie_bandwidth): self.pcie_bandwidth = pcie_bandwidth
    def set_pcie_lanes(self, pcie_lanes): self.pcie_lanes = pcie_lanes
    def set_interconnect_bandwidth(self, interconnect_bandwidth): self.interonnect_bandwidth = interconnect_bandwidth
    
#=====================================================
#  Functions for querying the Machine class attributes
#=====================================================
# All Features at once
    def query_set_all(self):
        '''
        Run all query and set functions at once
        '''
        self.set_host_cpu_cores(self.query_host_cpu_cores())
        self.set_host_clock_frequency(self.query_host_clock_frequency())
        self.set_host_peak_flops(self.query_host_peak_flops())
        self.set_host_mem_capacity(self.query_host_mem_capacity())
        self.set_host_mem_bandwidth(self.query_host_mem_bandwidth())
        
        self.set_snic_cpu_cores(self.query_snic_cpu_cores())
        self.set_snic_clock_frequency(self.query_snic_clock_frequency())
        self.set_snic_peak_flops(self.query_snic_peak_flops())
        self.set_snic_mem_capacity(self.query_snic_mem_capacity())
        self.set_snic_mem_bandwidth(self.query_snic_mem_bandwidth())
        
        self.set_pcie_bandwidth(self.query_pcie_bandwidth())
        self.set_pcie_lanes(self.query_pcie_lanes())
        self.set_interconnect_bandwidth(self.query_interconect_bandwidth())
 
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
        return psutil.cpu_count()
    
    def query_host_clock_frequency(self):
        '''
        Return host clock frequency
        '''
        return psutil.cpu_freq().current
                
    def query_host_peak_flops(self):
        '''
        Return the peak FLOP/s of the host CPU
        FIXME:
        '''
        # TODO: CALCULATE FLOPS
        a = [0.0] * 1000000
        b = [2.0] * 1000000
        c = [1.0] * 1000000
        scalar = 2.0
        start_time = time.time()
        for i in range (1000000):
            a[i] = b[i] + scalar * c[i]
        end_time = time.time()
        flops = 2 * 1000000
        gigaflops = flops / 10**9
        megaflops = flops / 10**6
        elapsed_time = end_time - start_time
        return megaflops / elapsed_time
        
        # TODO: CALCULATE FLOPS
        # start_time = time.time()
        # a = np.ones((1000, 1000))
        # b = np.ones((1000, 1000))
        # c = np.dot(a, b)
        # end_time = time.time()
        # flops = 2 * (1000 ** 3)
        # # megaflops = flops / 10**6
        # megaflops = 1.0E-06 * flops
        # elapsed_time = end_time - start_time
        # return megaflops / elapsed_time
            
        # TODO: USE PAPI TO CALCULATE FLOP/s
        # papi_high.start_counters([
        #     papi_events.PAPI_FP_OPS,
        #     papi_events.PAPI_TOT_CYC
        # ])
        # # papi_high.flops()
        # a = [1.0] * 1000000
        # b = [2.0] * 1000000
        # c = [1.0] * 1000000
        # for i in range(1000000):
        #     # result = result + (i * 0.1)
        #     a[i] = b[i] + i * c[i]
        # # result = papi_high.flops()
        # results = papi_high.read_counters()
        # papi_high.stop_counters()
        # return results[0]
        
        # TODO: USE PAPI TO CALCULATE FLOP/s
        # papi_low.library_init()
        # evs = papi_low.create_eventset()
        # papi_low.add_event(evs, papi_events.PAPI_FP_OPS)

        # a = [1.0] * 1000000
        # b = [2.0] * 1000000
        # c = [1.0] * 1000000
        # papi_low.start(evs)
        # for i in range(1000000):
        #     # result = result + (i * 0.1)
        #     a[i] = b[i] + i * c[i]
        # result = papi_low.stop(evs)
        # papi_low.cleanup_eventset(evs)
        # papi_low.destroy_eventset(evs)
        
        # return result
            
    
    def query_host_mem_capacity(self):
        '''
        Return the memory capacity on the host
        '''
        mem_capacity_in_bytes = psutil.virtual_memory().total
        mem_capacity_in_gigabytes = mem_capacity_in_bytes / 1024 / 1024 / 1024
        return mem_capacity_in_gigabytes
        
    def query_host_mem_bandwidth(self):
        '''
        Return the host CPU's memory bandwidth    
        TODO:
        '''
        # FIXME:
        a = np.ones(10000000, dtype=np.float32)
        b = np.zeros_like(a)
        
        # a = [0.0] * 1000000
        # b = [2.0] * 1000000
        # c = [1.0] * 1000000
        
        # a = np.ones(10000000, dtype=np.float64)
        # b = np.ones(10000000, dtype=np.float64)
        # c = np.ones(10000000, dtype=np.float64)
        
        # scalar = 2.0
        
        start_time = time.time()
        for i in range(100):
            np.copyto(b, a)
            
        # for i in range (1000000):
            # a[i] = b[i] + scalar * c[i]
             
        end_time = time.time()
        bytes_transferred = 2 * a.nbytes
        # bytes_transferred = 24 * 1000000
        megabytes_transferred = bytes_transferred / (1024**2)
        elapsed_time = end_time - start_time
        return megabytes_transferred / elapsed_time
        
        
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
    
    def query_snic_mem_capacity(self):
        '''
        Return the memory capcity on the SmartNIC
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
        return f"Machine({self.platform},{self.host_clock_frequency})"

    def print_all(self):
        '''
        Print all attributes of the Machine class
        '''
        print(
            "------------------------------------------------------------\n"
            f"Platform:\t\t\t\t{self.get_platform()}\n"
            "------------------------------------------------------------\n"
            f"Host CPU Cores:\t\t\t\t{self.get_host_cpu_cores()}\n"
            f"Host Clock Frequency (MHz):\t\t{self.get_host_clock_frequency()}\n"
            f"Host Estimated MFLOP/s:\t\t\t{self.get_host_peak_flops()}\n"
            f"Host Memory Capacity (GBs):\t\t{self.get_host_mem_capacity()}\n"
            f"Host Memory Bandwidth (MB/s):\t\t{self.get_host_mem_bandwidth()}\n\n" 
            f"SmartNIC CPU Cores:\t\t\t{self.get_snic_cpu_cores()}\n"
            f"SmartNIC Clock Frequency:\t\t{self.get_snic_clock_frequency()}\n"
            f"SmartNIC Estimated MFLOP/s:\t\t{self.get_snic_peak_flops()}\n"
            f"SmartNIC Memory Capacity:\t\t{self.get_snic_mem_capacity()}\n"
            f"SmartNIC Memory Bandwidth (MB/s):\t{self.get_snic_mem_bandwidth()}\n\n"
            f"PCIe Bandwidth:\t\t\t\t{self.get_pcie_bandwidth()}\n"
            f"PCIe Lanes:\t\t\t\t{self.get_pcie_lanes()}\n"
            f"Fabric Interconnect Bandwidth:\t\t{self.get_interconnect_bandwidth()}\n"
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