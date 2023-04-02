class Game:
    def __init__(self, init_field = [0], tmp_field = [0], n = 1, m = 1, cycles = 10):
        self.field = init_field
        self.cycles = cycles
        self.iteration = 0
        self.scope_field = tmp_field
        self.m = m
        self.n = n
    def cnt_ngh(self, m, n):
        cnt = 0
        for i in range(m - 1, (m + 1) + 1):
            for j in range(n - 1, (n + 1) + 1):
                if (i,j) == (m,n):
                    continue
                if self.field[i][j] == 1:
                    cnt += 1
        return cnt
    def scope(self):
        for i in range(1, self.m - 1):
            for j in range(1,self.n - 1):
                ngh = self.cnt_ngh(i,j)
                self.scope_field[i][j] = ngh
        for i in range(1, self.m - 1):
            for j in range(1, self.m - 1):
                if self.field[i][j] == 1:
                    if self.scope_field[i][j] < 2:
                        self.field[i][j] = 0
                    if self.scope_field[i][j] > 3:
                        self.field[i][j] = 0 
                else:
                    if self.scope_field[i][j] == 3:
                        self.field[i][j] = 1
    def game(self):
        while self.iteration <= self.cycles:
            self.scope()
            self.iteration += 1