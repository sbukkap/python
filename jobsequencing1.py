
def jobScheduler(l):
    x=int(input('enter the number of jobs to schedule'))

    status=['not-scheduled']*x
    """if x is 3   status=[not-scheduled,scheduled,not-scheduled]"""
    """index                      0            1              2        """
    job_sequence=['null']*x
    """    job_sequence=[null,b,null]"""
    """                   0     1    2  """
    """sorting the 2D list of jobs in decreasing order of their profits"""
    l.sort(reverse=True,key= lambda i:i[2])
    """list is now sorted as per req."""
    """
    after sorting
    l=[['b',2,100]
        ['d',1,27]
        ['a',2,10]
        ['c',2,15]
        ['e',3,7]]
    """
    """final piece of code"""
    for i in range(len(l)):
        j=l[i][1]-1
        """i.e deadline values"""
        while j >= 0:
            if status[j] == 'not-scheduled':
                status[j] = 'scheduled'
                job_sequence[j]=l[i][0]

                break
            else:
                j-=1
    print(job_sequence)
"""input array(or list) is a 2D array consisting of 5 consequent arrays inside a array"""
l=[['a',1,45],
['b',2,45],['c',3,25],[]]
jobSchedulerCode(l)
