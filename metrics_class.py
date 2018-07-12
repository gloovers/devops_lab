import psutil
import argparse
import configparser
import time
import json


class CPU:
    """CPU metrics"""
    def __init__(self):
        self.cpu_user = 0
        self.cpu_system = 0
        self.cpu_idle = 0
        self.get_metrics()

    def get_metrics(self):
        '''Get CPU metrics'''
        cpu = psutil.cpu_times()
        self.cpu_user = cpu.user
        self.cpu_system = cpu.system
        self.cpu_idle = cpu.idle


class MEM:
    """MEM metrics"""
    def __init__(self):
        self.mem_total = 0
        self.mem_available = 0
        self.mem_used = 0
        self.mem_free = 0
        self.get_metrics()

    def get_metrics(self):
        '''Get MEMORY VIRT metrics'''
        mem = psutil.virtual_memory()
        self.mem_total = mem.total
        self.mem_available = mem.available
        self.mem_used = mem.used
        self.mem_free = mem.free


class MEM_SWAP:
    """MEM-SWAP metrics"""
    def __init__(self):
        self.swap_total = 0
        self.swap_used = 0
        self.swap_free = 0
        self.get_metrics()

    def get_metrics(self):
        """Get SWAP metrics"""
        mem = psutil.swap_memory()
        self.swap_total = mem.total
        self.swap_used = mem.used
        self.swap_free = mem.free


class IO:
    """IO metrics"""
    def __init__(self):
        self.read = 0
        self.write = 0
        self.read_count = 0
        self.write_count = 0
        self.read_time = 0
        self.write_time = 0
        self.get_metrics()

    def get_metrics(self):
        """Get IO metrics"""
        io = psutil.disk_io_counters()
        self.read = io.read_bytes
        self.write = io.write_bytes
        self.read_count = io.read_count
        self.write_count = io.write_count
        self.read_time = io.read_time
        self.write_time = io.write_time


class NETWORK:
    """Network metrics"""
    def __init__(self):
        self.bytes_sent = 0
        self.bytes_recv = 0
        self.packets_sent = 0
        self.packets_recv = 0
        self.get_metrics()

    def get_metrics(self):
        """Get NETWORK metrics"""
        net = psutil.net_io_counters()
        self.bytes_sent = net.bytes_sent
        self.bytes_recv = net.bytes_recv
        self.packets_sent = net.packets_sent
        self.packets_recv = net.packets_recv


def get_path():
    '''Process path to config file.'''
    parser = argparse.ArgumentParser(description='Process path.')
    parser.add_argument('--path', "-p",
                        type=str, default='./config',
                        help='Path to Config file')
    args = parser.parse_args()
    path_conf = args.path
    return path_conf


def get_config(path_):
    '''Get config parameters'''
    Config = configparser.ConfigParser()
    Config.read(path_)
    if Config.has_option('common', 'output'):
        output = Config['common']['output']
    else:
        output = 'json'
    if Config.has_option('common', 'interval'):
        interval = Config['common']['interval']
    else:
        interval = '5'
    if Config.has_option('common', 'log'):
        log_path = Config['common']['log']
    else:
        log_path = './metrics.log'
    conf_parm = [output, interval, log_path]
    return conf_parm


def write_log_text(m1, m2, m3, m4, m5, path, cc):
    '''Write to log txt format'''
    log_file = open(path, 'a')
    s1 = "cpu.user={0}," \
         "cpu.system={1}," \
         "cpu.idle={2}".format(m1.cpu_user,
                               m1.cpu_system,
                               m1.cpu_idle)
    s2 = "mem.total={0}," \
         "mem.used={1}," \
         "mem.available={2}," \
         "mem.free={3}".format(m2.mem_total,
                               m2.mem_used,
                               m2.mem_available,
                               m2.mem_free)
    s3 = "swap.total={0}," \
         "swap.used={1}," \
         "swap.free={2}".format(m3.swap_total,
                                m3.swap_used,
                                m3.swap_free)
    s4 = "io.read={0}," \
         "io.write={1}," \
         "io.read_count={2}," \
         "io.write_count={3}," \
         "io.read_time={4}," \
         "io.write_time={5}".format(m4.read,
                                    m4.write,
                                    m4.read_count,
                                    m4.write_count,
                                    m4.read_time,
                                    m4.write_time)
    s5 = "net.bytes_sent={0}," \
         "net.bytes_recv={1}," \
         "net.packets_sent={2}," \
         "net.packets_recv={3}".format(m5.bytes_sent,
                                       m5.bytes_recv,
                                       m5.packets_sent,
                                       m5.packets_recv)
    stroka = "SNAPSHOT {0}:{1}:{2}:{3}:{4}:{5}:{6}\n".format(cc,
                                                             str(time.time()),
                                                             s1,
                                                             s2,
                                                             s3,
                                                             s4,
                                                             s5)
    log_file.write(stroka)
    log_file.close()


def write_log_json(m1, m2, m3, m4, m5, path, cc):
    '''Write to log json format'''
    snapshot = {'SNAPSHOT': str(cc)}
    timest = {'timestamp': str(time.time())}
    struct = {}
    struct.update(snapshot)
    struct.update(timest)
    cpu = {"CPU": m1.__dict__}
    struct.update(cpu)
    mem = {"MEMORY": m2.__dict__}
    struct.update(mem)
    swap = {"SWAP": m3.__dict__}
    struct.update(swap)
    io = {"DISC_IO": m4.__dict__}
    struct.update(io)
    net = {"NETWORK": m5.__dict__}
    struct.update(net)
    with open(path, 'a') as log:
        json.dump(struct, log, indent=2)


def main_prog():
    """Main repeatable actions"""
    Params = get_config(get_path())
    i = 0
    while True:
        i += 1
        cpu_snap = CPU()
        mem_snap = MEM()
        swap_snap = MEM_SWAP()
        io_snap = IO()
        net_snap = NETWORK()

        if Params[0] == 'text':
            write_log_text(cpu_snap,
                           mem_snap,
                           swap_snap,
                           io_snap,
                           net_snap,
                           Params[2],
                           i)
        if Params[0] == 'json':
            write_log_json(cpu_snap,
                           mem_snap,
                           swap_snap,
                           io_snap,
                           net_snap,
                           Params[2],
                           i)

        del cpu_snap
        del mem_snap
        del swap_snap
        del io_snap
        del net_snap
        time.sleep(int(Params[1]) * 60)


main_prog()
