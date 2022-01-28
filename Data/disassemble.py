import sys
import os
import os.path as osp
from time import time

def Disassemble(ApkPath, OutDir):
    '''
    To disassemble Dex bytecode in a given Apk file into smali code.
    Java version: "11.0.11" 2021-04-20
    baksmali tool was downloaded on: https://bitbucket.org/JesusFreke/smali/downloads/
    '''
    # os.system("java -jar {} disassemble {} -o {}".format(osp.join(os.getcwd(), 'baksmali-2.5.2.jar'), ApkPath, OutDir)) 
    os.system("java -jar {} disassemble {} -o {}".format(osp.join(sys.path[0], 'baksmali-2.5.2.jar'), ApkPath, OutDir)) 

if __name__ == "__main__":
    ApkPath = '/home/tiezhu/tmp/0009CFD8D8E01AA2B5CD9F3BFD5D75E52FE3DFBC82D5C6ABEE3E72A4E64564C7.apk'
    OutDir  = '/home/tiezhu/softwares/smali/test'
    time_start = time()
    Disassemble(ApkPath=ApkPath, OutDir=OutDir)
    print("Time cost: ", time()-time_start)
