from email.utils import formatdate
import uuid
import os

rssfile = "social.rss"
wrkrssfile = "tmpsocial.rss"
lastbuilddate = str("<lastBuildDate>" + formatdate(localtime="True") + "</lastBuildDate>\n\n")

title = input("Entry title? ")
description = input("Entry body? ")
pubdate = str("<pubdate>" + formatdate(localtime="True") + "</pubdate>\n")
guid = str("<guid>" + str(uuid.uuid4()) + "</guid>\n")
title = str("<title>" + title + "</title>\n")
description = str("<description><![CDATA[" + description + "]]></description>\n")
item = str("<item>\n" + title + pubdate + link + description + guid + "</item>\n")

wrkFile = open(rssfile, 'r')

wrkoutFile = open(wrkrssfile, 'w')

for line in wrkFile:
    if "lastBuildDate" in line:
        wrkoutFile.write(f"{lastbuilddate}")
        wrkoutFile.write(f"{item}")
    else:
        wrkoutFile.write(f"{line}")

os.remove('social.rss')
os.rename('tmpsocial.rss', 'social.rss')
