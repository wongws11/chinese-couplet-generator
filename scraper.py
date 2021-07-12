from bs4 import BeautifulSoup

def writeText (file, output):
    with open(file) as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    
    ctext = soup.find_all("td", {"class": "ctext"})
    fh = open(output, 'w')

    for i in ctext:
        if len(i) > 1:
            continue
        else:
            fh.write(i.getText() + '\n')
    fh.close()
    fp.close()

writeText('lower.html', 'ctext.txt')
writeText('upper.html', 'ctext.txt')