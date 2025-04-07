#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
sumgray=0
sum=0
pixcel=6
pixcel2=pixcel*pixcel
shine=0
while(True):
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (640,480))
    rows, cols, channels = resized_frame.shape
    gray =cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)
    moji=''
    for y in range(int(rows/pixcel)):
        for x in range(int(cols/pixcel)):
            for i in range(pixcel):
                for j in range(pixcel):
                    sumgray+=int(gray[y*pixcel+i,x*pixcel+j])
            shine=sumgray/pixcel2   
            if int(shine)<25:
                moji+='　'
            elif int(shine)<50:
                moji+='. '
            elif int(shine)<75:
                moji+='。'
            elif int(shine)<100:
                moji+='◻︎ '
            elif int(shine)<125:
                moji+='王'
            elif int(shine)<150:
                moji+='風'
            elif int(shine)<175:
                moji+='𡈁'
            elif int(shine)<200:
                moji+='鬱'
            elif int(shine)<225:
                moji+='🔲'
            else:
                moji+='⬜️'
            sumgray=0
        moji+='\n'
    print(moji)    
    cv2.imshow('frame', gray)
    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break # 'ESC' key is pressed
cv2.destroyAllWindows()