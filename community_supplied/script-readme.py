import re
import os
import os.path

current_folder_path, current_folder_name = os.path.split(os.getcwd())

#heading = ("# HealthBot %s KPI rules and playbooks"%current_folder_name)
#sub_heading = ("## %s playbooks"%current_folder_name)
heading = ("# HealthBot EVPN KPI rules and playbooks")
sub_heading = ("## EVPN VXLAN playbooks")

with open("README.md", "w") as ofile:
    ofile.write(heading + "\n")
    ofile.write("\n")
    ofile.write(sub_heading + "\n")

for fname in os.listdir('.'):
    if os.path.isfile(fname) and fname.endswith('.playbook'):
        f = open(fname)
        pbfilename = ("\t\t> Playbook file name: " + f.name)
        ofile = open("README.md", "a")
        pbcomment = pbcomment1 = pbname = pbdescription =  pbsynopsis = ""
    
        for line in f:
            comments = re.search('^ {1}\* ', line)
            if comments:
                a= line.strip()
                pbcomment1 = ("\t\t" + a.strip(';|{|\*'))
                pbcomment = pbcomment + "\n" + pbcomment1
            pb = re.search('^ {4}playbook', line)
            if pb:
                a= line.strip()
                pbname = ("### Playbook name:" + a.strip(';|{|playbook'))
            synop = re.search('^ {8}synopsis', line)
            if synop:
                a= line.strip()
                pbsynopsis = ("\t\t> Synopsis:" + a.strip(';|{|synopsis'))
            desc = re.search('^ {8}description', line)
            if desc:
                a= line.strip()
                pbdescription = ("\t\t> Description:" + a.strip(';|{|description')) 
                    
        ofile.write(pbname + "\n")
        ofile.write(pbdescription + "\n")
        ofile.write(pbsynopsis + "\n")
        ofile.write(pbfilename + "\n")
        pbcomment = ("\t\t> Detals:"+pbcomment)
        ofile.write(pbcomment + "\n")
        ofile = open("README.md", "r")
        ofile.close()
        f.close()
        
#rule_heading = ("## %s rules"%current_folder_name)
rule_heading = ("## EVPN VXLAN rules")
with open("README.md", "a") as ofile:
    ofile.write("\n")
    ofile.write(rule_heading + "\n")
    ofile.write("\n")
    
for fname in os.listdir('.'):
    if os.path.isfile(fname) and fname.endswith('.rule'):
        f = open(fname)
        rulefilename = ("\t\t> Rule file name: " + f.name)
        ofile = open("README.md", "a")
        rulecomment = rulecomment1 = ""
        ruledescription = rulesynopsis = ""
        product = product1 = ""
        platform = platform1 = ""
        junosrelease = junosrelease = ""
        helperfile = hbversion = ""
        for line in f:
            comments = re.search('^ {1}\* ', line)
            if comments:
                a= line.strip()
                rulecomment1 = ("\t\t" + a.strip(';|{|\*'))
                rulecomment = rulecomment + "\n" + rulecomment1
            rule = re.search('^ {8}rule', line)
            if rule:
                a= line.strip()
                rulename = ("### Rule name:" + a.strip(';|{|rule'))
            synop = re.search('^ {12}synopsis', line)
            if synop:
                a= line.strip()
                rulesynopsis = ("\t\t> Synopsis:" + a.strip(';|{|synopsis'))
            desc = re.search('^ {12}description', line)
            if desc:
                a= line.strip()
                ruledescription = ("\t\t> Description:" + a.strip(';|{|description'))
            prod = re.search('^ {28}products', line)
            if prod:
                a= line.strip()
                product1 = ("\t\t> Supported products:" + a.strip(';|{|products'))
                product = product + "\n" + product1
            platforms = re.search('^ {36}platform', line)
            rel = re.search('^ {32}releases', line)
            if rel:
                a= line.strip()
                junosrelease1 = ("\t\t\t> Minimum supported junos release:" + a.strip(';|{|releases'))
                junosrelease = junosrelease + "\n" + junosrelease1
            platforms = re.search('^ {36}platform', line)
            if platforms:
                a= line.strip()
                platform1 = ("\t\t\t> Supported platforms:" + a.strip('platform'))
                platform = platform + "\n" + platform1
            helpers = re.search('^ {20}list-of-files', line)
            if helpers:
                a= line.strip()
                helperfile = ("\t\t> Helper files:" + a.strip('list-of-files'))
            hbver = re.search('^ {16}supported-healthbot-version', line)
            if hbver:
                a= line.strip()
                hbversion = ("\t\t> Supported healthbot version:" + a.strip(';|{|supported-healthbot-version'))
        ofile.write(rulename + "\n")
        ofile.write(ruledescription + "\n")
        ofile.write(rulesynopsis + "\n")
        ofile.write(rulefilename + "\n")
        ofile.write(product + "\n")
        ofile.write(platform + "\n")
        ofile.write(helperfile + "\n")
        ofile.write(hbversion + "\n")
        rulecomment = ("\t\t> Detals:"+rulecomment)
        ofile.write(rulecomment + "\n")
        ofile = open("README.md", "r")
        print(ofile.read())
        ofile.close()
        f.close()

