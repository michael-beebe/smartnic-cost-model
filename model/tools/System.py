class System:
    """
    
    """
    def __init__(
        self, platform, host_cpu_cores, host_clock_frequency, host_peak_flops,
        host_mem_bandwidth, snic_cpu_cores, snic_clock_frequency,
        snic_mem_bandwidth, pcie_bandwidth, pcie_lanes, interconnect_bandwidth
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
        
        
    def check_if_linux(platform):
        if platform == "linux" or platform == "linux2":
            return True
        else:
            return False
        