import psutil
import argparse
import configparser
import time
import json


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
    output = Config['common']['output']
    interval = Config['common']['interval']
    if Config.has_option('common', 'log'):
        log_path = Config['common']['log']
    else:
        log_path = './metrics.log'
    conf_parm = [output, interval, log_path]
    return conf_parm


def write_log_text(m1, m2, m3, m4, m5, path, cc):
    '''Write to log txt format'''
    log_file = open(path, 'a')
    str1 = "cpu.user=%s," \
           "cpu.system=%s," \
           "cpu.idle=%s" % (m1['cpu']['cpu.user'],
                            m1['cpu']['cpu.system'],
                            m1['cpu']['cpu.idle'])
    str2 = "mem.total=%s," \
           "mem.used=%s," \
           "mem.available=%s," \
           "mem.free=%s" % (m2['mem']['mem.total'],
                            m2['mem']['mem.used'],
                            m2['mem']['mem.available'],
                            m2['mem']['mem.free'])
    str3 = "swap.total=%s," \
           "swap.used=%s," \
           "swap.free=%s" % (m3['mem_swap']['mem.total'],
                             m3['mem_swap']['mem.used'],
                             m3['mem_swap']['mem.free'])
    str4 = "io.read=%s," \
           "io.write=%s," \
           "io.read_count=%s," \
           "io.write_count=%s," \
           "io.read_time=%s," \
           "io.write_time=%s" % (m4['iostats']['io.disks_read'],
                                 m4['iostats']['io.disks_write'],
                                 m4['iostats']['io.disks_read_count'],
                                 m4['iostats']['io.disks_write_count'],
                                 m4['iostats']['io.disks_read_time'],
                                 m4['iostats']['io.disks_write_time'])
    str5 = "net.bytes_sent=%s," \
           "net.bytes_recv=%s," \
           "net.packets_sent=%s," \
           "net.packets_recv=%s" % (m5['network']['net.bytes_sent'],
                                    m5['network']['net.bytes_recv'],
                                    m5['network']['net.packets_sent'],
                                    m5['network']['net.packets_recv'])
    stroka = "SNAPSHOT %d:%s:%s:%s:%s:%s:%s\n" % (cc,
                                                  str(time.time()),
                                                  str1,
                                                  str2,
                                                  str3,
                                                  str4,
                                                  str5)
    log_file.write(stroka)
    log_file.close()


def write_log_json(m1, m2, m3, m4, m5, path, cc):
    '''Write to log json format'''
    snapshot = {'SNAPSHOT': cc}
    timest = {'time': str(time.time())}
    struct = {}
    struct.update(snapshot)
    struct.update(timest)
    struct.update(m1)
    struct.update(m2)
    struct.update(m3)
    struct.update(m4)
    struct.update(m5)
    with open(path, 'a') as log:
        json.dump(struct, log, indent=4)


def funct_1():
    '''Get CPU metrics'''
    cpu = psutil.cpu_times()
    value_dic = {
        'cpu': {
            'cpu.user': cpu.user,
            'cpu.system': cpu.system,
            'cpu.idle': cpu.idle,
        }
    }
    return value_dic


def funct_2():
    '''Get MEMORY VIRT metrics'''
    mem = psutil.virtual_memory()
    value_dic = {
        'mem': {
            'mem.total': mem.total,
            'mem.available': mem.available,
            'mem.used': mem.used,
            'mem.free': mem.free,
        }
    }
    return value_dic


def funct_3():
    '''Get SWAP metrics'''
    mem = psutil.swap_memory()
    value_dic = {
        'mem_swap': {
            'mem.total': mem.total,
            'mem.used': mem.used,
            'mem.free': mem.free,
        }
    }
    return value_dic


def funct_4():
    '''Get IO metrics'''
    sdiskio = psutil.disk_io_counters()
    value_dic = {
        'iostats': {
            'io.disks_read': sdiskio.read_bytes,
            'io.disks_write': sdiskio.write_bytes,
            'io.disks_read_count': sdiskio.read_count,
            'io.disks_write_count': sdiskio.write_count,
            'io.disks_read_time': sdiskio.read_time,
            'io.disks_write_time': sdiskio.write_time,
        }
    }
    return value_dic


def funct_5():
    '''Get NETWORK metrics'''
    net = psutil.net_io_counters()
    value_dic = {
        'network': {
            'net.bytes_sent': net.bytes_sent,
            'net.bytes_recv': net.bytes_recv,
            'net.packets_sent': net.packets_sent,
            'net.packets_recv': net.packets_recv,
        }
    }
    return value_dic


def body(type_log, path_log, cc):
    '''Main function working into cycle'''
    if type_log == 'text':
        write_log_text(funct_1(),
                       funct_2(),
                       funct_3(),
                       funct_4(),
                       funct_5(),
                       path_log,
                       cc)
    if type_log == 'json':
        write_log_json(funct_1(),
                       funct_2(),
                       funct_3(),
                       funct_4(),
                       funct_5(),
                       path_log,
                       cc)


def main_prog():
    '''Main repeatable actions'''
    Params = get_config(get_path())
    i = 0
    while True:
        i += 1
        body(Params[0], Params[2], i)
        time.sleep(int(Params[1]) * 60)


main_prog()
