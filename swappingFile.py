def swapFileData():
    import os
    import shutil
    source='C:/Users/BrijeshMunyal/Desktop/Python project/sample1.txt'
    destination='C:/Users/BrijeshMunyal/Desktop/sample2.txt'
    dest=shutil.copy(source,destination)
    print(os.listdir(path))

swapFileData()