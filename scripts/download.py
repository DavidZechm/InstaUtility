import instaloader
import os
import shutil
import csv
import random

ig = instaloader.Instaloader()


#max number to download
down_cap = 2
dst= 'downloads'
ctaUsr="user"

#import name list from names.csv
names = []

with open('data/names.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        names.append(row[0])

def customCta():
    res=""
    custom_db=[
    ["What ", "Such ", "Isn't this ", "Have you ever seen such "],
    ["an amazing ", "an awesome ", "a sick ", "a cool ", "a freakish ", "a tremendous ", "a breathtaking "],
    ["setup! ", "workstation! ", "desk! "],
    ["😍", "🥰", "🤯", "😳", "🙏", "👌"]
    ]

    for i in range(len(custom_db)):
        r=random.randint(0,len(custom_db[i])-1)
        res+=str(custom_db[i][r])
    return(res)


def captionThis(p,i):
            f= open(str(i)+".txt","w+")
            f.write(customCta()+"\n.\n")
            for i in range(2):
                f.write("Go Follow @" + str(ctaUsr) + " 💚🙌🏻\n")
            for i in range(3):
                f.write(".\n" )
            f.write("📸 by: @"+str(names[p]))
            f.close()

def download():
    for p in range(len(names)):
        posts = instaloader.Profile.from_username(ig.context, names[p]).get_posts()
        i=1
        if os.path.isdir(str(dst)+"/"+str(names[p]))==False:
            os.mkdir(str(names[p]))
        else:
            shutil.rmtree(os.path.join(dst, names[p]))
            os.mkdir(str(names[p]))
        for post in posts:
            if i<= down_cap:
                ig.download_pic(str(i), post.url, post.date)
                ig.save_caption(str(i), post.date, "")
                captionThis(p,i)
                shutil.move(str(i)+".jpg", names[p])
                shutil.move(str(i)+".txt", names[p])
                i+=1
        shutil.move(names[p], dst)


download()