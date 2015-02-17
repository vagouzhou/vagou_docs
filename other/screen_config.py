#!/usr/bin/python
import sys,os,platform

#
if(platform.system()=="Windows"):
    dir_screenshare_config_dir =  "c:/tmp/screen_share"
else:
    dir_screenshare_config_dir =  "/tmp/screen_share"
dir_screenshare_config_dump = dir_screenshare_config_dir+"/img-dump"
dir_screenshare_config_dump_decoded = dir_screenshare_config_dir+"/img-dump-decoded"
dir_screenshare_config_file = dir_screenshare_config_dir+"/share_config.json"

#
if not os.path.isdir(dir_screenshare_config_dir):
    os.makedirs(dir_screenshare_config_dir)
if not os.path.isdir(dir_screenshare_config_dump_decoded):
    os.makedirs(dir_screenshare_config_dump_decoded)
if not os.path.isdir(dir_screenshare_config_dump):
    os.makedirs(dir_screenshare_config_dump)


share_config_text ="""{
     "dump_raw_data":false,
     "dump_point_raw_data":false,
     "dump_raw_data_ring_size":100,
     "trace_one_by_frames":20,
     "trace_level":4,
     "dummy_point":false,
     "dummy_capture":false,
     "dummy_capture_width":1025,
     "dummy_capture_height":768,
     "dummy_point_sys_pos",false,
     "dummy_enumerator":false,
     "mac_support_display_scale":false,
     "capture_resample_enable":false,
     "capture_resample_width":1920,
     "capture_resample_heigt":1080
 }
"""

#
o_config_file = open(dir_screenshare_config_file, "w+")
o_config_file.write(share_config_text)
o_config_file.close()
