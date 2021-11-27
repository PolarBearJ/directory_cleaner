def scan_directory(mypath):
    from os import walk

    files = []
    for (dirpath, dirnames, filenames) in walk(mypath):
        files.extend(filenames)
        break
    return files

def contains_label(files, labels):
    for l in labels.keys():
        label_arr = []
        for f in files:
            if l in f:
                label_arr.append(f)
        labels[l] = label_arr
    return labels

def move_files(labels, movedir, baesdir):
    import os
    import shutil

    #Check if directory exists
    ne = "/NE"
    spcom = "/SPCOM"
    for l in labels.keys():
        if l == "223":
            tempdir =movedir + spcom + l
        else:
            tempdir =movedir + ne + l
        # Create Directory if not already exists
        if not os.path.exists(tempdir):
            os.makedirs(tempdir)
        for file in labels[l]:
            shutil.move(basedir + "/" + file,tempdir + "/" + file)

if __name__ == '__main__':
    movedir = "/Users/YOURNAME/Desktop/Past Assignments"
    basedir = "/Users/YOURNAME/Downloads"
    labels_classes = {"215": [],
                      "216": [],
                      "222": [],
                      "241": [],
                      "223": []
                      }
    labels_labs = {
        "216L": [],
        "222L": [],
        "241L": [],
        "220L": []
    }
    files = scan_directory(basedir)
    labels = contains_label(files, labels_labs)
    move_files(labels, movedir, basedir)
    print("Files Moved:")
    for file in labels.values():
        if len(file) > 0:
            print(file)
    files = scan_directory(basedir)
    labels = contains_label(files, labels_classes)
    move_files(labels, movedir, basedir)
    for file in labels.values():
        if len(file) > 0:
            print(file)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
