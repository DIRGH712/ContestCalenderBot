import ClointFusion as cf
import time
import os

def Contest_calender(password="",username=""):
    #this function has all functionality to download from website
    cf.launch_website_h("https://www.google.com/")
    time.sleep(2)
    cf.browser_navigate_h("https://www.hackerrank.com/dashboard")
    time.sleep(2)
    cf.browser_mouse_click_h("log in")
    try:
        cf.browser_write_h(username,"Your username or email")
        time.sleep(1)
        cf.browser_write_h(password,"Your password")
        time.sleep(2)
        cf.browser_mouse_click_h("log in")
        time.sleep(1)
    except Exception as e:
        print("user not found " + str(e))
    
    #click 
    cf.browser_mouse_click_h("Contest Calendar")
    cf.browser_wait_until_h("Programming Contest Calendar")
    # cf.browser_refresh_page_h()
    cf.browser_mouse_click_h("Download Calendar")
    time.sleep(11)
    cf.browser_quit_h()

#the next line will make sure to delete old files so we can get latest news about contests
cf.folder_delete_all_files("C:/Users/patel/Downloads",file_extension_without_dot='ics')

password_file = open("password.txt", "r")
password = password_file.read()
Contest_calender(password,"pateldirgh@gmail.com",)

#from here its everything about opening download file
users_choice = cf.gui_get_consent_from_user('open downloaded file ?')

#asks user to open/not open download file
if users_choice == "Yes":
    filepath_path = cf.gui_get_any_file_from_user("HackerRank_Calendar","ics")
    filepath_path = filepath_path.replace("/","\\")
    os.startfile(filepath_path)
else:
    print("your file is downloaded. Open from downloads if you want to know about contest timings")



