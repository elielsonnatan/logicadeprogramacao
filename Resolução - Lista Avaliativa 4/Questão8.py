S = [1, 2, [3, 4, [5, 6, [7, 8, [9, [0]]]]]]

print("A lista S possui", len(S), "elementos.")

S[2][2][2][2][1] = 17

print("\nA lista S alterada é:", S)