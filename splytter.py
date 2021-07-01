# It splits, I dunno what more to say

from typing import Counter

# Okay I know this should probably be a class...
def build(income):
    budget = []
    item = ""
    share = 0
    sharesum = 0
    while  item != "done":
        print("item:")
        item = input()
        if item == "done":
            continue
        print("income share:")
        share = round(float(input()),2)
        sharesum += share
        if sharesum > 1:
            print("shares exceed income, " + item + " not added.")
            sharesum -= share
            continue
        budget.append([item, share, round(income * share, 2), round(income *
         share, 2)])
    budget.append(["misc", round(1-sharesum,2), round(income * (1-sharesum),2),
     round(income * (1-sharesum),2)])
    return budget

def printBudget(income, budget):
    print('income: ', income)
    county = 0
    for i in budget:
        print (county, ": ", i[0], ': ', i[2])
        county += 1

def reBudget(cash, boi):
    income = cash
    budget = boi
    pSum = 0.00
    for i in budget:
        if i[3] > 0:
            pSum += i[1]
        else:
            i[1]=0
    for i in budget:
        i[1] = round(float(i[1])/pSum, 5)
        if i[3] >= 0:
            i[2] = round(float(i[1])*income, 2)
    return budget

def reAllocate(cash, boi):
    income = cash
    budget = boi
    pSum = 0.00
    for i in budget:
        if i[2] > 0:
            pSum += i[1]
        else:
            i[1]=0
    for i in budget:
        i[2] = round((float(i[1])/pSum)*income, 2)
    return budget
'''
In budget, 0 is name, 1 is share, 2 is remaining funds and 3 is remaining
 relative to first allocation
'''
def spend():
    print("income:")
    income = float(input())
    budget = build(income)
    printBudget(income, budget)
    purchase = 0
    while purchase != -1:
        print("Item Code:")
        purchase = int(input())
        print("Amount:")
        amount = float(input())
        if amount > income:
            print('Decline.')
            continue
        income -= amount
        if amount > float(budget[purchase][2]):
            budget[purchase][3] -= amount
            if budget[purchase][3] >= 0:
                budget[purchase][2] = 0
                budget = reAllocate(income, budget)
            else:
                budget[purchase][2] -= amount
                budget = reBudget(income, budget)
        else:
            budget[purchase][2] = round(float(budget[purchase][2]) 
                -amount, 2)
            budget[purchase][3] = round(float(budget[purchase][2]) 
                -amount, 2)
        printBudget(income, budget)



spend()