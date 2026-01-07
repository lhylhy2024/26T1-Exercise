import re

s = "<tr><td>美元</td><td>100</td><td>691.38</td><td>691.38</td><td>688.42</td><td>682.76</td></tr>"

m = re.search(r"<tr>",s)
n = re.search(r"</tr>",s)
s = s[m.end():n.start()]
while s!="":
    m = re.search(r"<td>",s)
    n = re.search(r"</td>",s)
    t = s[m.end():n.start()]
    print(t)
    s = s[n.end():]