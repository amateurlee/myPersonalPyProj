# -*- coding: utf-8 -*-
# !/usr/bin/python
import commands, os

OUT_FOLDER = "/Users/mjli/MyDoc/宝宝/视频MP4/碰碰狐mp4/"
IN_FOLDER = "/Users/mjli/MyDoc/宝宝/视频MP4/tiger/"
file_name_profix = "碰碰狐_"
file_name_suffix = ".ts"
ts_total_number = 0


def isTsFolder(fileList):
    ts_count = 0
    for file in fileList:
        if file.endswith("ts"):
            ts_count += 1
            if ts_count >= 2:
                return True
    if ts_count == 0:
        return False


def mergeTsFiles(parents, files):
    global ts_total_number
    filesStr = ""
    for file in files:
        if file.endswith("ts"):
            out_file = "{}{}{}{}".format(OUT_FOLDER, file_name_profix, ts_total_number, file_name_suffix)
            filesStr = "{filesStr} {parents}/{currentFile}".format(filesStr=filesStr, parents=parents, currentFile=file)
    cmd = "cat {file} > {outfile}".format(file=filesStr, outfile=out_file)
    ts_total_number += 1
    commands.getoutput(cmd)
    return cmd


if __name__ == "__main__":
    for parents, dirnames, files in os.walk(IN_FOLDER):
        if isTsFolder(files):
            print mergeTsFiles(parents, files)
