#!/usr/bin/env python3

import os
import shutil

def main():
    os.chdir('/home/student/mycode/')
    shutil.move('raynor.obj', 'ceph_storage/')
    xname = input('What is the new name for kerrigan.obj? ')
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)


if __name__ == "__main__":
    main()
