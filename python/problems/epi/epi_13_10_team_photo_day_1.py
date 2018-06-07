def valid_placement_exists(team1, team2):
    for i, j in zip(sorted(team1), sorted(team2)):
        print(i, j)
        if i > j:
            return False
    return True


team1 = [1, 2, 3, 4, 5]
team2 = [4, 3, 3, 1, 6]
print(valid_placement_exists(team1, team2))
