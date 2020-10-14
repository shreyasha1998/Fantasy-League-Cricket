import sqlite3
db=sqlite3.connect("Fantasy.db")
cur=db.cursor()
cur.execute("SELECT * FROM match;")
rec=cur.fetchall()

for i in rec:
    nm= i[0]
    runs = i[1]
    balls = i[2]
    four = i[3]
    six = i[4]
    bwl = i[5]
    given = i[7]
    wkt = i[8]
    catch = i[9]
    stump = i[10]
    ro = i[11]


    batscore=int(runs/2)
    if batscore>=50:
        batscore+=5
    if batscore>=100:
        batscore+=10
    if runs>0:
        sr=runs*100/balls
    if sr>=80 and sr<100:
        batscore+=2
    if sr>=100:
        batscore+=4
    batscore=batscore+four
    batscore=batscore+2*six
    bowlscore=wkt*10
    if wkt>=3:
        bowlscore=bowlscore+5
    if wkt>=5:
        bowlscore=bowlscore+10
    if bwl>0:
        
        er=given/bwl

        if er<=2:
            bowlscore=bowlscore+10
        
        if er>2 and er<=3.5:
             bowlscore=bowlscore+7
       
        if er>3.5 and er<=4.5:
            bowlscore=bowlscore+4
        
    fieldscore = 10*catch + 10*stump + 10*ro
    print(batscore,bowlscore,fieldscore)

    total = batscore + bowlscore + fieldscore
    
  
    try:
        print(total)
        cur.execute("UPDATE match SET Points='"+str(total)+"' WHERE Player='"+nm+"';")
        
        print ("one record added successfully")
    except:
        print ("error in operation")
        db.rollback()
    batscore=0
    bowlscore = 0
    total =0
db.commit()
db.close()

