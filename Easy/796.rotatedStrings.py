class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and (s+s).find(goal) != -1
        # verifica se possui mesmo tamanho, e verifica se a substring goal esta contida dentro s+s