import sys
import os
import glob
from bs4 import BeautifulSoup, SoupStrainer

def walklevel(some_dir, level=1):
    some_dir = some_dir.rstrip(os.path.sep)
    assert os.path.isdir(some_dir)
    num_sep = some_dir.count(os.path.sep)
    for root, dirs, files in os.walk(some_dir):
        yield root, dirs, files
        num_sep_this = root.count(os.path.sep)
        if num_sep + level <= num_sep_this:
            del dirs[:]


save_in_MM = True # "False" if you want to save txt in the same folder. "True" if you want to save in separate folder below
MM = "C:\\Mangas\\Texts\\"

# total arguments
n = len(sys.argv)
print("Total arguments passed:", n-1)


for i in range(1, n):
    
    if not os.path.isdir(sys.argv[i]):
        print(os.path.split(sys.argv[i])[1], "is not a path")
        continue
    
    print("Processing: ", os.path.split(sys.argv[i])[1])
    
    os.chdir(sys.argv[i])

    sPath = os.path.split(sys.argv[i])[1] + '.txt'
    
    if save_in_MM:
        sPath = MM + os.path.split(sys.argv[i])[1] + '.txt'

    try:
        with open(sPath, 'w', encoding="utf8") as f:

            for root, dirs, files in walklevel(sys.argv[i]):
                
                for name in files:
                    if not ".html" in name:
                        continue
                    
                    if ".mobile." in name:
                        continue
                        
                    p = os.path.join(root, name)
                    
                    page=open(p, encoding="utf8")
                    soup = BeautifulSoup(page.read(), "html.parser", parse_only=SoupStrainer(class_="textBox"))
                    
                    mtexts=soup.find_all("div", class_="textBox")
                    
                    for t in mtexts:
                        tp = t.find_all("p")
                        for ps in tp:
                            f.write(ps.text)
                        
                        f.write('\n')
                        
                        
    except FileNotFoundError:
        print("Error in open txt")
