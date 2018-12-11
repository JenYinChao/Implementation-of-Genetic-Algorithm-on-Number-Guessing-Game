import random as rd

def InitDistribution():
    x_list = []
    for i in range(4):
        x = rd.sample(range(0,100),10)
        for pro_dig in x:
            x_list.append(round(pro_dig/sum(x)*100,2))
    return x_list

def GA_MultiCheck(GA):
    if GA[0] in GA[1:] or GA[1] in GA[2:] or GA[2] in GA[3:] or GA[3] in GA[4:]:
        return True
    else:
        return False

def GuessingAnswer(x_list,method=1):
    GA_Mul = True;
    while GA_Mul:
        GA = []
        for sec in range(4):
            digit_dist = x_list[0+sec*10:(sec+1)*10]
            if method==1:
                rd_dist = rd.random()*100; dist_sum = 0; digit_tag = -1
                while dist_sum < rd_dist and digit_tag<9:
                    digit_tag += 1
                    dist_sum += digit_dist[digit_tag]
            else:
                if len([x for x in digit_dist if x>50])>0:
                    digit_tag = digit_dist.index([x for x in digit_dist if x>50][0])
                else:
                    rd_dist = rd.random()*100; dist_sum = 0; digit_tag = -1
                    while dist_sum < rd_dist and digit_tag<9:
                        digit_tag += 1
                        dist_sum += digit_dist[digit_tag]
            GA.append(digit_tag)
        GA_Mul = GA_MultiCheck(GA)
    return GA

def Evaluation(ans,guess,weightB=0.5):
    credit = 0
    for i in range(4):
        if guess[i] == ans[i]:
            credit += 1
        elif guess[i] in ans:
            credit += weightB
    return credit
    
def ChildDistScale(child_dis):
    return [round(e/sum(child_dis)*100,2) for e in child_dis]

def CrossOver(par_dis):
    child_dis = []
    for j in range(4):
        child_dis_ind = []
        dist_index_1 = rd.sample(range(10),5)
        for i in range(10):
            if i in dist_index_1:
                child_dis_ind.append(par_dis[0][i+10*j])
            else:
                child_dis_ind.append(par_dis[1][i+10*j])
        child_dis.extend(ChildDistScale(child_dis_ind))
    return child_dis

def Mutation(child_dis,m):
    mut_list = rd.sample(range(len(child_dis)),round(len(child_dis)*m))
    for i in mut_list:
        child_dis[i] = InitDistribution()
    return child_dis

def ChildReproduction(par_dis,child_num,m):
    child_dis = []
    for i in range(child_num):
        child_dis.append(CrossOver(rd.sample(par_dis,2)))
    child_dis = Mutation(child_dis,m)
    return child_dis
    