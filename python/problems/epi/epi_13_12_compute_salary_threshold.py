def find_salary_cap(target, salaries):
    salaries.sort()
    nsum = 0
    l = len(salaries)
    for i, val in enumerate(salaries):
        if nsum + (l - i) * val >= target:
            return (target - nsum) / (l - i)
        nsum += val

    return -1.0


target = 210
salaries = [90, 30, 100, 40, 20]
print(find_salary_cap(target, salaries))
