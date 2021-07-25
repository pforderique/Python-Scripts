from os import listdir, rename
from os.path import isfile, join
import shutil



EXAMS_FOLDER = "C:/Users/fabri/OneDrive/Desktop/Orderique/MIT Spring 2021/6.006/"


onlyfiles = [f for f in listdir(EXAMS_FOLDER) if isfile(join(EXAMS_FOLDER, f))]

for f in onlyfiles:
    if "quiz1" in f: destination = EXAMS_FOLDER+"QUIZ1/"
    elif "quiz2" in f: destination = EXAMS_FOLDER+"QUIZ2/"
    elif "quiz3" in f: destination = EXAMS_FOLDER+"QUIZ3/"
    else: destination = EXAMS_FOLDER+"FINALS/"

    origin = EXAMS_FOLDER + f
    destination += f

    # shutil.move('/Users/billy/d1/xfile.txt', '/Users/billy/d2/xfile.txt')
    rename(origin, destination)
    print("move", f, f"from {origin} to", destination)

# print(onlyfiles)
