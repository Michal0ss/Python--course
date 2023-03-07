# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's  creation and modification times)

import shutil

oryginal = r'C:\\Users\\smiec\\PycharmProjects\\course12h\\File handaling\\test.txt'
target = r'C:\\Users\\smiec\\PycharmProjects\\course12h\\File handaling\\asd.txt'
shutil.copy2(oryginal, target)  # source,destination
