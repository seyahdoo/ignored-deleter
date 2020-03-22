
import os
import subprocess
from gitignore_parser import parse_gitignore

folder = "S:/"
#folder = "T:/TERASAD/CODES/Meteor"
#folder = "C:/CODE_SEGMANT"

subfolders = [f.path for f in os.scandir(folder) if f.is_dir()]


def crawl(path):
    subfolders = [f.path for f in os.scandir(path) if f.is_dir()]
    #print(subfolders)
    for s in subfolders:
        deleteignored(s)
        crawl(s)


def deleteignored(path):
    for f in os.scandir(path):
        if f.name == ".gitignore":
            print("ignore found")
            print(f.path)
            # matches = parse_gitignore(f.path)
            # deleterecursive(matches, f.path)
            for ff in os.scandir(path):
                if ff.name == ".git":
                    print("git folder found")
                    subprocess.call(["git", "clean", "-dfX"])
                    return

            os.chdir(path)
            subprocess.call(["git", "init"])
            subprocess.call(["git", "clean", "-dfX"])
    return

# def deleterecursive(matches, path):
#     subfolders = [ff.path for ff in os.scandir(path) if ff.is_dir()]
#     for s in subfolders:
#         if matches(s):
#             os.remove(s)
#         else:
#             deleterecursive(matches, s)
#     subfiles = [ff.path for ff in os.scandir(path) if ff.is_file()]
#     for s in subfiles:
#         if matches(s):
#             os.remove(s)


crawl(folder)
