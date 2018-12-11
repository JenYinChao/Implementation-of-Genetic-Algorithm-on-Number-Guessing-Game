from Functions import *
import copy

def main():
    ans = [1,5,4,3]
    no_parent = 1000; e = 0.1; t = 0.8; m = 0.01 
    parent_dis = []; eval_all = []; eval_top20 = []
    
    for no_p in range(no_parent):
        parent_dis.append(InitDistribution())
            
    for turn in range(500):
        parent_ans = []; parent_eva = []
        for par_dis in parent_dis:
            parent_ans.append(GuessingAnswer(par_dis,method=2))
        for par_ans in parent_ans:
            parent_eva.append(Evaluation(par_ans,ans,weightB=0.2))
        eva_sort = sorted(range(len(parent_eva)), key=lambda k: -parent_eva[k])
        eval_all.append(sum([ parent_eva[i] for i in eva_sort ])/no_parent)
        eval_top20.append(sum([ parent_eva[i] for i in eva_sort[0:round((no_parent*(1-t)))] ])/round((no_parent*(1-t))))
        child_dis = [ parent_dis[i] for i in eva_sort[0:round((no_parent*e))] ]
        parent_choose = [ parent_dis[i] for i in eva_sort[0:round((no_parent*(1-t)))] ]
        child_dis.extend(ChildReproduction(parent_choose, round(no_parent*(1-e)), m))
        parent_dis = copy.deepcopy(child_dis)
    
    import matplotlib.pyplot as plt
    plt.style.use('seaborn-whitegrid')
    plt.title("Average Evaluation Score")
    plt.xlabel("Generations"); plt.ylabel("Evaluation Score")
    plt.plot(range(500),eval_top20,color="red", label="Top 20%")
    plt.plot(range(500),eval_all,color="blue", label="All")
    plt.legend()
    
if __name__ == "__main__":  
    main()
