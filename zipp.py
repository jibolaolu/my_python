import zipfile
import shutil
f = open('fileone.txt', 'w+')
f.write("This is just for text One")
f.close()

w = open('filetwo.txt', 'w+')
w.write("This is just for text Two")
w.close()

#Zipping File
comp_file = zipfile.ZipFile('comp_file.zip', 'w')
comp_file.write('fileone.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('filetwo.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

#Unzipping File
extr_obj = zipfile.ZipFile('comp_file.zip', 'r')
extr_obj.extractall('extracted_content')

#Zipping an entire folder
dir_to_zip = " C:\\Users\\oluwaseun\\PycharmProjects\\python_Tutorials\\extracted_content"
output_filename = 'example'
shutil.make_archive(output_filename,'zip', dir_to_zip)