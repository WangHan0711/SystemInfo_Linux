# -*- coding: utf-8 -*-
import SystemInfo


print("System Start Time : %ss" % SystemInfo.get_start_time())
print("System Now Time : %s" % SystemInfo.get_now_time())
print("CPU Used Percent : %.1f%%" % SystemInfo.get_cpu_used_percent())
# print("CPU free Percent : %.1f%%" % SystemInfo.get_cpu_free_percent())
print("CPU free Percent No Blocking : %.1f%%" % SystemInfo.get_cpu_free_percent_no_blocking())
print("Memory Used Percent : %.1f%%" % SystemInfo.get_mem_used_percent())
print("Memory free Percent : %.1f%%" % SystemInfo.get_mem_free_percent())
print("Disk free : %dB === %dKB === %dMB === %dGB" % (SystemInfo.get_disk_free(), SystemInfo.get_disk_free()/1024,
                                                      SystemInfo.get_disk_free()/1024/1024,
                                                      SystemInfo.get_disk_free()/1024/1024/1024))
print("Disk used : %dB === %dKB === %dMB === %dGB" % (SystemInfo.get_disk_used(), SystemInfo.get_disk_used()/1024,
                                                      SystemInfo.get_disk_used()/1024/1024,
                                                      SystemInfo.get_disk_used()/1024/1024/1024))
print("Disk free percent : %.1f%%" % SystemInfo.get_disk_free_percent())
print("Disk used percent : %.1f%%" % SystemInfo.get_disk_used_percent())
print("ipaddr : %s\nnetmask : %s\ngateway : %s\n" % (SystemInfo.get_ip_info()))
# print("Set Time Status : %d" % SystemInfo.set_now_time(2019, 5, 4, 12, 50, 54))
# print("System Now Time : %s" % SystemInfo.get_now_time())
# print("Set Time Status : %d" % SystemInfo.set_now_time(2019, 5, 14, 14, 10, 54))
# print("System Now Time : %s" % SystemInfo.get_now_time())
# SystemInfo.set_ip_info('10.255.88.83', '255.255.248.0', '10.255.95.254')
