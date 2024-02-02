def solve(head,legs):
    num_chicken=0
    num_rabbits=0
    for i in range(head + 1):
        num_chicken=i 
        num_rabbits=head-i
        if((num_chicken*2) + (num_rabbits*4) == legs):
            break

    print(f"chicks = {num_chicken} ")
    print(f"rabbits = {num_rabbits} ") 
solve(35, 94)
    