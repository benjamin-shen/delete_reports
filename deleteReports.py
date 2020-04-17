#!/usr/bin/python3

import pyautogui
import time
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

reports = "reports.txt"
deleted = "deleted.txt"
manual = "manual.txt"

def searchNext():
    f = open(reports, "r")
    content = f.read()
    f.close()
    allReports = content.strip("\n").split("\n")
    f = open(deleted, "r")
    content = f.read()
    f.close()
    deletedReports = content.strip("\n").split("\n")
    for reportName in allReports:
        if not (reportName in deletedReports):
            pyautogui.typewrite(reportName)
            return reportName
    raise Exception

def refresh():
    refreshed = pyautogui.locateOnScreen('refreshed.png')
    if refreshed == None:
        refresh = pyautogui.locateOnScreen('refresh.png')
        if refresh == None:
            bookmark = pyautogui.locateOnScreen('bookmark.png')
            if bookmark == None:
                return False
            else:
                pyautogui.click(bookmark[0]+bookmark[2]/2, bookmark[1]+bookmark[3]/2, duration=0.25)
                time.sleep(3)
        else:
            pyautogui.click(refresh[0]+refresh[2]/2, refresh[1]+refresh[3]/2, duration=0.25)
            time.sleep(2)
    return True

def searchReport():
    searchbar = pyautogui.locateOnScreen('searchbar.png')
    if searchbar == None:
        time.sleep(5)
        searchbar = pyautogui.locateOnScreen('searchbar.png')
        if searchbar == None:
            return ""
    pyautogui.click(searchbar[0]+searchbar[2]/2, searchbar[1]+searchbar[3]/2, duration=0.25)
    reportName = searchNext()
    print('"' + reportName + '"')
    pyautogui.typewrite(['enter'])
    time.sleep(1)
    return reportName

def deleteReport(reportName):
    # print(pyautogui.position())
    pyautogui.click(225,444, duration=0.25)
    error1 = pyautogui.locateOnScreen('error1.png')
    if (error1 != None):
        return False;
    pyautogui.click(225,428, duration=0.25)
    error1 = pyautogui.locateOnScreen('error1.png')
    if (error1 != None):
        return False
    pyautogui.click(225,412, duration=0.25)
    error1 = pyautogui.locateOnScreen('error1.png')
    if (error1 != None):
        return False
    time.sleep(3)
    pyautogui.click(1857,298, duration=0.25)
    time.sleep(2)
    delete = pyautogui.locateOnScreen('delete.png')
    if delete == None:
        time.sleep(5)
        delete = pyautogui.locateOnScreen('delete.png')
        if delete == None:
            time.sleep(5)
            delete = pyautogui.locateOnScreen('delete.png')
            if delete == None:
                return False
    pyautogui.click(delete[0]+delete[2]/2, delete[1]+delete[3]/2, duration=0.25)
    time.sleep(2)
    confirm = pyautogui.locateOnScreen('confirm.png')
    if confirm == None:
        time.sleep(5)
        confirm = pyautogui.locateOnScreen('confirm.png')
        if confirm == None:
            time.sleep(5)
            confirm = pyautogui.locateOnScreen('confirm.png')
            if confirm == None:
                return False
    pyautogui.click(confirm[0]+confirm[2]/2, confirm[1]+confirm[3]/2, duration=0.25)
    error2 = pyautogui.locateOnScreen('error2.png')
    if (error2 != None):
        return False
    f = open(deleted, "a")
    f.write(reportName + "\n")
    f.close()
    return True

def main():
    try:
        time.sleep(2) # time to get window in focus
        # for i in range(1):
        while True:
            if refresh():
                report = searchReport()
                if report != "":
                    if not deleteReport(report):
                        print("Report not deleted.")
                        f = open(manual, "a")
                        f.write(report + "\n")
                        f.close()
                        f = open(deleted, "a")
                        f.write(report + "\n")
                        f.close()
                else:
                    print("Report not found.")
                    f = open(manual, "a")
                    f.write(report + "\n")
                    f.close()
                    f = open(deleted, "a")
                    f.write(report + "\n")
                    f.close()
            else:
                print("Refresh unsuccessful.")
                return
    except pyautogui.FailSafeException:
        print("FailSafe activated.")

if __name__ == "__main__":
    print('Drag to top left corner to exit program.')
    main()
