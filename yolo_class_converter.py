##Yolo dataset class converter. Replace classes of a yolo dataset format (.txt files) with new classes (numbers: 0,1, etc).

import os
path = ''#path to folder with txt files in yolo format

class_substitute = '1' #Class we want to replace to
classes_to_replace = [] #If empty, it will replace all classes. Pass as string(s).

for filename in os.listdir(path):
    if '.txt' in filename:
        new_dict = []
        with open(path + filename, "r+") as f:
            #data = f.readlines()
            lines = [line.rstrip('\n') for line in f]
            for line in lines:
                if len(classes_to_replace) == 0:
                    new_dict.append(class_substitute + line[1:])
                elif line[0] in classes_to_replace:
                    new_dict.append(class_substitute + line[1:])
                else:
                    new_dict.append(line)                
            f.seek(0)
            for new_line in new_dict:
                f.write(new_line + "\n")
            f.truncate()
