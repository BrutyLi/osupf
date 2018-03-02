import psutil
import datetime,os
import signal

'''CPU
    内存
    磁盘
    忘了
    系统信息
    用户信息
    进程管理'''


KB=1024
MB=pow(1024,2)
GB=pow(1024,3)

def cpuInfo():
    pcpu=psutil.cpu_count()
    vcpu=psutil.cpu_count(logical=False)
    ucpu=str(psutil.cpu_percent(interval=1))+"%"
    print(ucpu)
    return [pcpu,vcpu,ucpu]
def memInfo():
    mem=psutil.virtual_memory()
    mtotal=round(mem.total/MB,2)
    muse=round(mem.used/MB,2)
    mfree=round(mem.free/MB,2)
    return [mtotal,muse,mfree]
def diskInfo():
    '''{分区:[挂载目录，文件系统],}'''
    part={}
    for par in psutil.disk_partitions():
        part[par[0]]=[par[1],par[2]]
def ioInfo():
    read_count=psutil.disk_io_counters()[0]
    write_count = psutil.disk_io_counters()[1]
    read_bytes= psutil.disk_io_counters()[2]/pow(1024,2)
    write_bytes = psutil.disk_io_counters()[3]/pow(1024,2)
    return [read_count,write_count,read_bytes,write_bytes]
def bootInfo():
    boot_time=datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    return boot_time
def userInfo():
    ulist=[]
    huser=psutil.users()
    for x in range(len(huser)):
        ulist.append(huser[x][0])
        print(huser[x])
    return ulist
def netInfo():
    net_conn=psutil.net_connections(kind='inet4')
    net_io=psutil.net_io_counters()
    net_addr=psutil.net_if_addrs()
    net_stats=psutil.net_if_stats()
    return [net_addr,net_io,net_conn,net_stats]
def proInfo():
    proList=[]
    for proc in psutil.process_iter():
        try:
            pinfo=proc.as_dict(attrs=['pid','name','username'])
        except psutil.NoSuchProcess:
            pass
        else:
            proList.append(pinfo)
    return proList
def find_procs_by_name(name):
    "Return a list of processes matching 'name'."
    ls = []
    for p in psutil.process_iter(attrs=["name", "exe", "cmdline"]):
        if name == p.info['name'] or \
                p.info['exe'] and os.path.basename(p.info['exe']) == name or \
                p.info['cmdline'] and p.info['cmdline'][0] == name:
            ls.append(p)
    print(ls)
    return ls
def kill_proc_tree(pid, sig=signal.SIGTERM, include_parent=True,
                   timeout=None, on_terminate=None):
    """Kill a process tree (including grandchildren) with signal
    "sig" and return a (gone, still_alive) tuple.
    "on_terminate", if specified, is a callabck function which is
    called as soon as a child terminates.
    """
    if pid == os.getpid():
        raise RuntimeError("I refuse to kill myself")
    parent = psutil.Process(pid)
    children = parent.children(recursive=True)
    if include_parent:
        children.append(parent)
    for p in children:
        p.send_signal(sig)
    gone, alive = psutil.wait_procs(children, timeout=timeout,
                                    callback=on_terminate)
    print(gone,alive)
    return (gone, alive)
