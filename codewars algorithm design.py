# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 16:29:36 2022

@author: 91838
"""
# TODO: create the User class
# it must support rank, progress, and the inc_progress(rank) method
class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0
        self.progresscount=[]
        
    def getrank(self,li,currank):
        rank_list2=[-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8] 
        summ=sum(li)
        ind=rank_list2.index(currank)
       
            
            
        while  summ>=100:  #checking a condition if index crosses len of ranklist
           # if ind <=len(rank_list2)-1:
                
                ind=ind+1
             #  if ind >len(rank_list2)-1:
                   
                summ=summ-100
        print(ind,summ,"tt")      
        if summ<100 and ind >len(rank_list2)-1:
            return 0,0,8
        if summ<100 and ind == len(rank_list2)-1:
            return 0,[0],rank_list2[ind]
        if summ<100 and ind < len(rank_list2)-1:
             return summ,[summ],rank_list2[ind]
            #if ind >=len(rank_list2)-1:
                   #  return 0,[0],8
    def getpoints(self,activityrank):
        rank_list=[-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8]
        if self.rank == activityrank:  # getting points wen currank =act rank
            self.progresscount.append(3)   
            r=self.getrank(self.progresscount,self.rank)# checking if after appending the point the sum of progress became bigger than 100 or not
            return r
            
            
            
            
        if self.rank >activityrank : # getting points wen activity rank is lesser than current rank
            d=len(rank_list[rank_list.index(activityrank):rank_list.index(self.rank)]) #findind the d of algorithm 
            if d==1:
                self.progresscount.append(1)   
                r=self.getrank(self.progresscount,self.rank)# checking if after appending the point the sum of progress became bigger than 100 or not
                return r
            if d>=2:
                return self.progress,self.progresscount,self.user_rank
        if self.rank<activityrank :  #getting point wen activity rank is greater than current rank
            d=len(rank_list[rank_list.index(self.rank):rank_list.index(activityrank)])
            q=10*d*d
            self.progresscount.append(q)
            r=self.getrank(self.progresscount,self.rank)  #checking that after appending did progress became >100 or less
            return r
        
                
            
        
            
            
            
        
        
        

    def inc_progress(self, activityrank):
        
        if activityrank <-8:
            raise ValueError
        if activityrank >8:
            raise ValueError
        if activityrank ==0:
            raise ValueError
        s=self.getpoints(activityrank)
        self.progress,self.progresscount,self.rank=s
           
        



