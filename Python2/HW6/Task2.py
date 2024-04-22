def eight_queens(pos):
    for i in range(8):
        for j in range(i+1, 8):
            if pos[i] == pos[j] or pos[i] - i == pos[j] - j or pos[i] + i == pos[j] + j:
                return False
    return True
