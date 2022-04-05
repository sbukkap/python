    def sortSentence(self, s: str) -> str:
        l=s.split()
        l.sort(key=lambda i:i[-1])
        nl=[]
        for i in l:
            nl.append(i[:-1])
        s=' '.join(nl)
        return s
        
