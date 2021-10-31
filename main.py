class Deadline:
    def __init__(self, data=[], n_lessons=None):
        self.n_lessons = n_lessons
        self.data = list()
        self.add(data)

    def sort(self):
        self.data.sort(key=val_sort, reverse=True)

    def add(self, data=False):
        if (data):
            if (isinstance(data, list)):
                self.data += data
            else:
                self.data.append(data)
    def set_ls(self, ls):
        self.n_lessons = ls

    def get_sum(self, last=False):
        s = 0
        new = []
        cont = True
        for key, val in enumerate(self.data):
            if (key>=self.n_lessons):
                cont = False

            if (cont):
                s += val.value
                val.days_left -= key
            else:
                new.append(val)
                val.days_left -= self.n_lessons
                if (last):
                    val.days_left = -1
        return s, new


class Task:
    def __init__(self, value, days_left):
        self.value = value
        self.days_left = days_left

def ksp_input():
    n = int(input())
    inp = []
    for i in range(n):
        i = input().split()
        i = [int(j) for j in i]
        inp.append(Task(i[0], i[1]))
    return inp

def file_input():
    inp = []
    x = False
    with open("input") as file:
        for line in file:
            if (x):
                i = line.split()
                i = [int(j) for j in i]
                inp.append(Task(i[0], i[1]))
            x = True
    return inp
def rework_to_nodes(inp=[]):
    data = []
    x = -1
    for val in inp:
        if (val.days_left==x):
            data[-1].add(val)
        else:
            data.append(Deadline(val))
            x = val.days_left
    return data

def sort(obj):
    return obj.days_left

def val_sort(obj):
    return obj.value

def file_output(inp, s):
    with open("output", "w") as file:
        file.write(str(s)+"\n")
        for i in inp:
            file.write(str(i.days_left)+"\n")
def set_max_les(inp):
    for key, deadline in enumerate(inp):
        if(key+1==len(inp)):
            deadline.set_ls(1)
        else:
            x = deadline.data[0].days_left - inp[key+1].data[0].days_left
            deadline.set_ls(x)
inp = [Task(9, 1), Task(3, 0), Task(8, 2), Task(7, 1), Task(2, 2)]
inp = file_input()
new_inp = sorted(inp, key=sort, reverse=True)
deadlines = rework_to_nodes(new_inp)
set_max_les(deadlines)
s = 0
b = False
length = len(deadlines)
last = False
for key, deadline in enumerate(deadlines):
    if (key+1==length):
        last = True
    deadline.add(b)
    deadline.sort()
    a, b = deadline.get_sum(last)
    s += a
file_output(inp, s)







