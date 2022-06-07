people_list = ["Your momma","Your pops","Your friend","Your auntie","Your cousin","Your grandma","Your grandpa","Your grandson","Your sister","Your brother"]
comp_list = ["is sorchin hot","is packin","is hella thick","is fine","is a hottie","is a cutie pie","is a chick magnet","got me sweating","got me lickin my lips","got a small waist, pretty face, wit a big bank"]
import random
num_people = random.randrange(0,len(people_list))
num_comp = random.randrange(0,len(comp_list))

print(people_list[num_people]+" "+comp_list[num_comp])
