import getpass
import os
import platform
import socket
import uuid
import winreg as _winreg


def GetOsName():
    '''操作系统名称'''
    keyPath = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion"
    each_key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, keyPath, 0, _winreg.KEY_READ)
    OsName, REG_SZ = _winreg.QueryValueEx(each_key, "ProductName")
    return OsName


def GetOsVersion():
    '''操作系统版本'''
    keyPath = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion"
    each_key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, keyPath, 0, _winreg.KEY_READ)
    OsVersion, REG_SZ = _winreg.QueryValueEx(each_key, "CurrentVersion")
    return OsVersion


def GetOsModel():
    '''操作系统型号'''
    keyPath = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion"
    each_key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, keyPath, 0, _winreg.KEY_READ)
    OsModel, REG_SZ = _winreg.QueryValueEx(each_key, "EditionID")
    return OsModel


def get_architecture():
    '''获取操作系统的位数'''
    return platform.architecture()


def get_machine():
    '''计算机类型'''
    return platform.machine()


def get_node():
    '''计算机的网络名称'''
    return platform.node()


def get_processor():
    '''计算机处理器信息'''
    return platform.processor()


def get_system():
    '''获取操作系统类型'''
    return platform.system()


def get_TotalInfo():
    '''汇总信息'''
    return platform.uname()


def get_localDataPath():
    '''当前用户路径'''
    return os.path.expanduser('~')


def get_UserName():
    '''当前用户名'''
    return getpass.getuser()


def get_ComputerName1():
    '''获取机器名称'''
    return platform.node()()


def get_ComputerName():
    '''获取机器名称'''
    return socket.gethostname()


def get_AddressIp():
    '''获取本机IP'''
    return socket.gethostbyname(get_ComputerName())


def get_Mac():
    '''获取MAC地址'''
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ':'.join(mac[e:e + 2].upper() for e in range(0, 11, 2))


def show_os_all_info():
    '''打印os的全部信息'''
    print('操作系统的位数 : [{}]'.format(get_architecture()))
    print('计算机类型 : [{}]'.format(get_machine()))
    print('计算机的网络名称 : [{}]'.format(get_node()))
    print('计算机处理器信息 : [{}]'.format(get_processor()))
    print('操作系统类型 : [{}]'.format(get_system()))
    print('汇总信息 : [{}]'.format(get_TotalInfo()))
    print('当前用户路径: [{}]'.format(get_localDataPath()))
    print('当前用户名: [{}]'.format(get_UserName()))
    print('机器名称: [{}]'.format(get_ComputerName()))
    print('机器IP: [{}]'.format(get_AddressIp()))
    print('MAC地址: [{}]'.format(get_Mac()))


show_os_all_info()
print(GetOsModel(), GetOsVersion(), GetOsName())