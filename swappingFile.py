def swapFileData():
    import os
    import shutil
    source='C:/Users/Kotwal/Documents/White Hat Jr/Python/C98 File Swapper/Pro-c98-master/sample1.txt'
    destination='C:/Users/Kotwal/Documents/White Hat Jr/Python/C98 File Swapper/Pro-c98-master/sample2.txt'
    dest=shutil.copy(source,destination)
    print(os.listdir(path))

swapFileData()