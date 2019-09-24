class BikePerson():
    def bike_person(self, loc):
        # loc: N*M list of char consist of 'o', 'p', 'b' respect to none, person, bike.
        p_loc = set()
        b_loc = set()
        N = len(loc)
        M = len(loc[0])
        for i in len(N):
            for j in len(M):
                if loc[i][j] == 'p':
                    p_loc.add((i, j))
                if loc[i][j] == 'b':
                    b_loc.add((i, j))

