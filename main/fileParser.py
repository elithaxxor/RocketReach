from datetime import datetime
import os


class fileParser:
    def __init__(self, filename):
        self.filename = filename

    def addToList(self, href_loc):
        try:
            count = 0
            print("[+] Adding to List")
            with open(href_loc) as f:
                for href in open(href_loc):
                    print("[!] Adding to List")
                  #  count += 1
                    website_list = f.readlines(count)
                    print(f"[!] website list {website_list}")
                    index = 0
                    for iterate in website_list:
                        count += 1
                        if index <= count:
                            print(f'[SYS]** ADDED {iterate}')
                            website_list.append(iterate)
                            index += 1
                        break
                    print(f'[!] Found {count} items in .txt')
                    print(f'[!] Wrote {website_list} .')

                    break
        except Exception as e:
            print(f'[ERROR] addToList {str(e)}')

    ## This function reads the data from a file
    def read_file(filename):
        print(f'[+] Reading File: {filename}')

        if os.path.isfile(filename):
            with open(filename, 'r') as f:
                data = f.read()
        return data


    ## This function writes the data to a file
    def write_file(filename, data):
        if os.path.isfile(filename):
            with open(filename, 'a') as f:
                f.write('\n' + data)
        else:
            with open(filename, 'w') as f:
                f.write(data)


class autostart:
    def __init__(self, filename):
        self.filename = filename

    def print_time(self):
        print("[+] printing timestamp")

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        data = "[!] Current Time = " + current_time
        return data


    def makeFile(self):
        print("[+] Making File")
        fileParser.write_file('hrefdata.txt', autostart.print_time(self))
        pwd00 = input('Enter the file name to write to (.txt): ')
        write_file=(pwd00, '')
        print("[+]" 'File Created')


## RUN THE PROGRA WITH PRINT TIME CLASS APPENDED, SO YOU HAVE A DATE-TIME STAMP
#autostart.run_writeFile().print_time("hrefdata.txt")


print(f'.TXT SCANNER --> progfram')
website_list = []
count = 0
hrefdata = 'hrefdata.txt'
cwd = os.getcwd()
href_loc = str(cwd) + f'/{hrefdata}'
href_str = f'[SYSTEM]** Dump The Text Data To: [{href_loc}] ** [SYSTEM]'
print(href_str)


href_file = "hrefdata.txt"
path = os.getcwd()

# autostart.print_time('hrefdata.txt')
# autostart.makeFile('hrefdata.txt')

# fileParser.write_file('hrefdata.txt', autostart.print_time('hrefdata.txt'))
fileParser.addToList(href_file, href_loc)
print("href loc: ", path, href_loc)
print("[!] website list " + f'{website_list}')
print("[!] count " + f'website_list.count()')