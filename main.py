from time import sleep
import os

count=1

def update():
    if 'a.txt' in os.listdir():
        os.system('rename a.txt b.txt')  #Renames file
    elif 'b.txt' in os.listdir():
        os.system('rename b.txt a.txt')  #Renames file
    else:
        listdir=os.listdir()
        for list in listdir:
            if list != '.git':
                os.system('del '+ list)
        os.system('type nul > a.txt')


def pull(repo,url):
    if os.path.exists(repo)==False:
        os.system('git clone ' + url)
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, ''+repo)
    os.chdir(filename)

def push():
    global count
    os.system('cd')
    os.system('git add . && git commit -m "commit ' + str(count) + '"')
    os.system('git push origin main')
    count+=1

def main():
    repo= "commits"
    url = "git@github.com:marcos-inja/commits.git"
    comm= 10
    pull(repo,url)
    for i in range(0,comm):
        update()
        push()


if __name__=='__main__':
    main()