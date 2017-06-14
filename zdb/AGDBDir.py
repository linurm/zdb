import os
import getpass

print getpass.getuser()

class AGDB:
    addr = {}
    def getAllDir(self):
        f = open('config')
        for i, l in enumerate(f, 1):
            key = l.split('=')[0]
            value = l.split('=')[1].strip("\n").strip('\r')
            if key == "GDB_DIR":
                global gdb_dir
                value = value.replace('Administrator', getpass.getuser())
                gdb_dir = value
            if key == "ADB_DIR":
                global adb_dir
                adb_dir = value
            if key == "GDBSERVER_DIR":
                global gdbserver_dir
                value = value.replace('Administrator', getpass.getuser())
                gdbserver_dir = value
            if key == "PKG_NAME":
                global pkg_name
                pkg_name = value
            if key == "LAUNCH":
                global launch_name
                launch_name = value
            if key == "LIBNAME":
                global lib_name
                lib_name = value
            if key == "PKG_DIR":
                global pkg_dir
                pkg_dir = value
            if key == "APKTOOL_DIR":
                global apktool_dir
                apktool_dir = value
            if key == "DEX2JAR_DIR":
                global dex2jar_dir
                dex2jar_dir = value
            if key == "IDA_FILE_DEVIATION":
                global ida_file_deviation
                ida_file_deviation = value
            if key == "APK_NAME":
                global apk_name
                apk_name = value
            if key == "SMALI_DIR":
                global smali_dir
                smali_dir = value
            if key == "PYTHON_INSTALL_DIR":
                global python_install_dir_name
                python_install_dir_name = value
            if key == "ADD_CLASS_DIRNAME":
                global add_class_dirname
                add_class_dirname = value
            if key == "MODEFY_CLASS_DIRNAME":
                global modefy_class_dirname
                modefy_class_dirname = value
            if key == "MODEFY_CLASS_LIST_FILE":
                global class_list_file
                class_list_file = value
        self.addr['gdb_dir'] = gdb_dir.replace('"','')
        self.addr['adb_dir'] = adb_dir.replace('"','')
        self.addr['gdbserver_dir'] = gdbserver_dir.replace('"','')
        self.addr['pkg_name'] = pkg_name.replace('"','')
        self.addr['launch_name'] = launch_name.replace('"','')
        self.addr['lib_name'] = lib_name.replace('"','')
        self.addr['pkg_dir'] = pkg_dir.replace('"','')
        self.addr['apktool_dir'] = apktool_dir.replace('"','')
        self.addr['dex2jar_dir'] = dex2jar_dir.replace('"','')
        self.addr['apk_name'] = apk_name.replace('"','')
        self.addr['smali_dir'] = smali_dir.replace('"','')
        self.addr['python_install_dir_name'] = python_install_dir_name.replace('"','')
        self.addr['ida_file_deviation'] = ida_file_deviation.replace('"','')
        self.addr['add_class_dirname'] = add_class_dirname.replace('"','')
        self.addr['modefy_class_dirname'] = modefy_class_dirname.replace('"','')
        self.addr['class_list_file'] = class_list_file.replace('"','')
        
        return self.addr
                
##############################################



        
