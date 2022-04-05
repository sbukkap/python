def rotateTheBox(self, l: List[List[str]]) -> List[List[str]]:
        """
        the basic idea is to mark the value(index) of the first rock ..then if empty space is found ...swp that with rocks value
        also i incrmented rock value by 1 as soon as i swap at lines 24 and 25 if empty sapce and rock are found and there is no obstacle between them....then it automatically means that the next item after the first occuring rock is also a rock....this is true for every case
        case 1: [#,.,*] and case 2: [#,#,#,.,etc] (in both cases its true)
        also i reassigned rock value to initial value in line 28 becasue line 28 means that there is an obstacle between rock and empty space and the value of first rock found is no longer true....same applies to line 31
        also you might be wondering why i initialzzed rock at line 16 and condition two at line 19 ,this is to make sure the value of first rock found doesnt get altered
        also the reason why i assigned obstacle at line 17 specially to lie between rock and j (in line 23)is because of this strnage test case which would fail otherwise
        [[.,.,.,.],[.,.,.,.],[.,.,.,.]] (or similar matrix where all are empty spaces) the way i manipulated obstacle values in various places(except last assinment at last elif statement) enures this test case doent fail

        Note1:if there exists obstacle between rock and empty space, no swap is to be done ...this is ensured by code at line 29
        """
        for i in l:
            rock = -2
            obstacle=-1
            for j in range(len(l[0])):
                if i[j] == '#' and rock == -2:
                    rock = j
                    obstacle=-2
                elif i[j] == '.':
                    if not rock<obstacle<j:
                        i[j] = '#'
                        i[rock] = '.'
                        rock+=1
                    else:
                        rock = -2
                elif i[j] == '*':
                    obstacle = j
                    rock = -2
        """the piece of code written below will shift the matriix into 90 degrees"""
        transpose=[[0 for i in range(len(l))] for j in range(len(l[0]))]
        for i in range(len(l[0])):
            for j in range(len(l)):
                transpose[i][j] = l[j][i]
        for i in transpose:
            i.reverse()
        return transpose
