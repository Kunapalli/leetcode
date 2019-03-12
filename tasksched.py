import collections

# https://leetcode.com/problems/task-scheduler/
# Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks.
# Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

# However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing
# different tasks or just be idle.

# You need to return the least number of intervals the CPU will take to finish all the given tasks.

"""
There are two problems, one is min number of intervals and secondly, the actual arrangement. 
We are only solving for the former. We will come to the latter in a bit.

Some things to keep in mind: Beyond what is needed, having more types of tasks is actually a good thing and not relevant 
to the minimum calculation.
What is the worst case behavior? The worst case depends on the most frequent letter (assume a single letter is the most 
frequent, we can extend later) and n.

Consider
[['H', 113], ['J', 106], ['B', 104], ['A', 103], ['G', 102], ['F', 100], ['D', 97], ['C', 95], ['E', 92], ['I', 88]], 
n = 8, total = 1000

We know the most frequent letter is H. And it needs to be separated by 8. We can have

H_________H_________H________.....H 
1         2         3            113
This is the worst case scenario for this. We need (H + 8)*112 + H = 1009 cycles. Since 1009 > 1000, we will 
have 9 idle cycles. But this doesn't explain anything.

For example, where does the 9 come from?

Between any two H's we will have at least 8 other letters. So minimum non-H letters inserted = 8 * 112 = 896
We can also insert 9 letters between every two H's. Then maximum (since we only have 10 letters) non-H letters = 9 * 112 = 1008.
But we only have 1000 - 113 = 887 left and need a minimum of 896. So we need 896 - 887 = 9 idle cycles.

How does the arrangement actually look? can we see the 9 idle cycles?

We have [['H', 113], ['J', 106], ['B', 104], ['A', 103], ['G', 102], ['F', 100], ['D', 97], ['C', 95], ['E', 92], ['I', 88]], 
n = 8, total = 1000

H_________H_________H________.....H 
1         2         3            113
There are a total of 112 intervals (in between the H's). Idea is to keep filling to the end, if letter is over, take the next letter.
 If we reached the end, go back to the beginning.

First insert in the first 106 intervals (from the left) J. We will have 112 - 106 = 6 intervals left to fill. Fill these 6 with next letter B.
We have 104 - 6 = 98 B. Fill the first 98 intervals (from the left) with B. We will have 112 - 98 = 14 intervals left to fill. 
Fill these 14 with next letter A

We have 103 - 14 = 89 A. Fill the first 89 intervals (from the left) with A. We will have 112 - 89 = 23 intervals left to fill. 
Fill these 23 with next letter G

We have 102 - 23 = 79 G. Fill the first 79 intervals (from the left) with G. We will have 112 - 79 = 33 intervals left to fill. 
Fill these 33 with next letter F

We have 100 - 33 = 67 F. Fill the first 67 intervals (from the left) with F. We will have 112 - 67 = 45 intervals left to fill. 
Fill these 45 with next letter D

We have 97 - 45 = 52 D. Fill the first 52 intervals (from the left) with D. We will have 112 - 52 = 60 intervals left to fill. 
Fill these 60 with next letter C

We have 95 - 60 = 35 C. Fill the first 35 intervals (from the left) with C. We will have 112 - 35 = 77 intervals left to fill. 
Fill these 77 with next letter E

We have 92 - 77 = 15 E. Fill the first 15 intervals (from the left) with E. We will have 112 - 15 = 97 intervals left to fill. 
We have 88 I. Fill the 88 with I.

We will have 9 intervals left with only 7 letters each. Fill them with one idle each for a total of 9 idles
A shorter way to get to this is to take 887 % 112 = 103. After distributing 7 characters each into 112 intervals, we have 103 characters 
left which go into the 103 of the 112 intervals leaving 9 intervals with only 7 chars.

Suppose we make n = 9
Then according to the formula in the code, we need 112 * 10 + 1 = 1121 cycles.
In the above example we have 113 H spanning 112 intervals. 103 intervals had 8 letters each. 9 intervals had 7 letters each.
Add one idle to each of the 103 intervals and 2 idles to each of the 9 intervals for a total of 1 * 103 + 2 * 9 = 121 idle cycles.

A quick example for n= 10. We need 112*11 + 1 = 1233.
We need 2 * 103 + 3 * 9 = 206 + 27 = 233 idle cycles.

For all n <= 7, we will use the full 1000 and the arrangement we got above would be valid for all n <= 7 since every interval has at least 7.

specifically, for n = 1,

H_H_H_.......H 
1 2 3      113
We need some other character or idle between these H's. So we (H + 1 idle)*112 + the last H = 225.
This means if we have 225 characters, we can satisfy this. All the remaining 225 - 113 = 112 can come from just one 
character (again this is the worst case).
So we can have H 113, J 112 . Having other types of tasks (as long as count is < 113) does not matter to us.

So in this example, we need a minimum of 112 * 1 = 112 and a maximum possible of 112 * 9 = 1008 [since there are only 10 total chars). 
We still have 1000 - 113 = 887 chars left.
So we will use the full 1000 without idle cycles.

"""

def leastInterval(tasks, N):
    tasks = collections.Counter(tasks)
    task_counts = tasks.values()
    M = max(task_counts)
    Mct = collections.Counter(task_counts).most_common(1)[0][1]
    return max(sum(task_counts), (M - 1) * (N + 1) + Mct)

print(leastInterval(["G","C","A","H","A","G","G","F","G","J","H","C","A","G","E","A","H","E","F","D","B","D","H","H","E","G","F","B","C","G","F","H","J","F","A","C","G","D","I","J","A","G","D","F","B","F","H","I","G","J","G","H","F","E","H","J","C","E","H","F","C","E","F","H","H","I","G","A","G","D","C","B","I","D","B","C","J","I","B","G","C","H","D","I","A","B","A","J","C","E","B","F","B","J","J","D","D","H","I","I","B","A","E","H","J","J","A","J","E","H","G","B","F","C","H","C","B","J","B","A","H","B","D","I","F","A","E","J","H","C","E","G","F","G","B","G","C","G","A","H","E","F","H","F","C","G","B","I","E","B","J","D","B","B","G","C","A","J","B","J","J","F","J","C","A","G","J","E","G","J","C","D","D","A","I","A","J","F","H","J","D","D","D","C","E","D","D","F","B","A","J","D","I","H","B","A","F","E","B","J","A","H","D","E","I","B","H","C","C","C","G","C","B","E","A","G","H","H","A","I","A","B","A","D","A","I","E","C","C","D","A","B","H","D","E","C","A","H","B","I","A","B","E","H","C","B","A","D","H","E","J","B","J","A","B","G","J","J","F","F","H","I","A","H","F","C","H","D","H","C","C","E","I","G","J","H","D","E","I","J","C","C","H","J","C","G","I","E","D","E","H","J","A","H","D","A","B","F","I","F","J","J","H","D","I","C","G","J","C","C","D","B","E","B","E","B","G","B","A","C","F","E","H","B","D","C","H","F","A","I","A","E","J","F","A","E","B","I","G","H","D","B","F","D","B","I","B","E","D","I","D","F","A","E","H","B","I","G","F","D","E","B","E","C","C","C","J","J","C","H","I","B","H","F","H","F","D","J","D","D","H","H","C","D","A","J","D","F","D","G","B","I","F","J","J","C","C","I","F","G","F","C","E","G","E","F","D","A","I","I","H","G","H","H","A","J","D","J","G","F","G","E","E","A","H","B","G","A","J","J","E","I","H","A","G","E","C","D","I","B","E","A","G","A","C","E","B","J","C","B","A","D","J","E","J","I","F","F","C","B","I","H","C","F","B","C","G","D","A","A","B","F","C","D","B","I","I","H","H","J","A","F","J","F","J","F","H","G","F","D","J","G","I","E","B","C","G","I","F","F","J","H","H","G","A","A","J","C","G","F","B","A","A","E","E","A","E","I","G","F","D","B","I","F","A","B","J","F","F","J","B","F","J","F","J","F","I","E","J","H","D","G","G","D","F","G","B","J","F","J","A","J","E","G","H","I","E","G","D","I","B","D","J","A","A","G","A","I","I","A","A","I","I","H","E","C","A","G","I","F","F","C","D","J","J","I","A","A","F","C","J","G","C","C","H","E","A","H","F","B","J","G","I","A","A","H","G","B","E","G","D","I","C","G","J","C","C","I","H","B","D","J","H","B","J","H","B","F","J","E","J","A","G","H","B","E","H","B","F","F","H","E","B","E","G","H","J","G","J","B","H","C","H","A","A","B","E","I","H","B","I","D","J","J","C","D","G","I","J","G","J","D","F","J","E","F","D","E","B","D","B","C","B","B","C","C","I","F","D","E","I","G","G","I","B","H","G","J","A","A","H","I","I","H","A","I","F","C","D","A","C","G","E","G","E","E","H","D","C","G","D","I","A","G","G","D","A","H","H","I","F","E","I","A","D","H","B","B","G","I","C","G","B","I","I","D","F","F","C","C","A","I","E","A","E","J","A","H","C","D","A","C","B","G","H","G","J","G","I","H","B","A","C","H","I","D","D","C","F","G","B","H","E","B","B","H","C","B","G","G","C","F","B","E","J","B","B","I","D","H","D","I","I","A","A","H","G","F","B","J","F","D","E","G","F","A","G","G","D","A","B","B","B","J","A","F","H","H","D","C","J","I","A","H","G","C","J","I","F","J","C","A","E","C","H","J","H","H","F","G","E","A","C","F","J","H","D","G","G","D","D","C","B","H","B","C","E","F","B","D","J","H","J","J","J","A","F","F","D","E","F","C","I","B","H","H","D","E","A","I","A","B","F","G","F","F","I","E","E","G","A","I","D","F","C","H","E","C","G","H","F","F","H","J","H","G","A","E","H","B","G","G","D","D","D","F","I","A","F","F","D","E","H","J","E","D","D","A","J","F","E","E","E","F","I","D","A","F","F","J","E","I","J","D","D","G","A","C","G","G","I","E","G","E","H","E","D","E","J","B","G","I","J","C","H","C","C","A","A","B","C","G","B","D","I","D","E","H","J","J","B","F","E","J","H","H","I","G","B","D"],1))
