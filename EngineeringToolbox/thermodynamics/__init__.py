from subprocess import Popen, PIPE
import urllib.request
import os

# Get installed version number
process = Popen(['pip', 'freeze'], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()
output = stdout.decode("utf8")
installed_version = output[output.index("EngineeringToolbox")+len("EngineeringToolbox")+2:output.index("EngineeringToolbox")+len("EngineeringToolbox")+7]

# Get most current release version number
fp = urllib.request.urlopen("https://github.com/jhphillips1029/EngineeringToolbox/tags")
mybytes = fp.read()
mystr = mybytes.decode("utf8")
fp.close()
phrase = mystr[mystr.index('commit-title')+20:mystr.index('commit-title')+20+100]
curr_release = phrase[phrase.index(">")+3:phrase.index("\n",phrase.index(">")+5)].strip()

# Debug check
#print("Installed:\t{}\nAvailable:\t{}".format(installed_version,curr_release))

# Convert
inst = 0
curr = 0
for num_i,num_c in zip(installed_version.split("."),curr_release.split(".")):
    inst += int(num_i)*10**(len(installed_version.split("."))-installed_version.split(".").index(num_i)-1)
    curr += int(num_c)*10**(len(curr_release.split("."))-curr_release.split(".").index(num_c)-1)
    
# Exit if up to date or better
if curr <= inst:
    
    # Debug check
    #print("You're up to date!")
    pass
    
else:
    # Get webpage data for list of table files
    fp = urllib.request.urlopen("https://github.com/jhphillips1029/EngineeringToolbox/tree/master/EngineeringToolbox/thermodynamics/data_tables")
    mybytes = fp.read()
    webpage = mybytes.decode("utf8")
    fp.close()

    # Generate list of table files
    links = []
    i_old = webpage.index('rowheader')+10
    i_new = webpage.index('rowheader',i_old)
    while i_new > 0:
        substr = webpage[i_new:i_new+600]
        link = substr[substr.index("href")+6:substr.index('"',substr.index("href")+6)]
        links.append(link)
        i_old = i_new+10
        try:
            i_new = webpage.index('rowheader',i_old)
        except:
            break

    # Get location for tables folder
    download_to = __file__.replace("__init__.py","") + "data_tables/"

    # If folder does not already exist, create it
    if not os.path.exists(download_to):
        os.makedirs(download_to)

    for link in links:
        name = link[len('/jhphillips1029/EngineeringToolbox/blob/master/EngineeringToolbox/thermodynamics/data_tables/'):]

        # Debug check
        #print("Downloading {} to {}".format(name,download_to))

        urllib.request.urlretrieve('https://raw.githubusercontent.com/jhphillips1029/EngineeringToolbox/master/EngineeringToolbox/thermodynamics/data_tables/'+name,download_to+name)
