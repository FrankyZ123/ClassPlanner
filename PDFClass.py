import pdftotext

def flatten(A):
    rt = []
    for i in A:
        if isinstance(i,list): rt.extend(flatten(i))
        else: rt.append(i)
    return rt

class ParseSyllabus:
    def __init__(self):
        self.parsed = []

        self.titles = []
        self.weights = []
        self.released = []
        self.due = []
    
    def getAssignments(self, filename, parsed=[]):
        '''
        Returns Assignment Titles, Weights, and Due Dates from Syllabus.
        '''
        
        with open(filename, "rb") as f:
            pdf = pdftotext.PDF(f)

        for i in range(0, len(pdf)):
            parsed.extend([x.rstrip(':').rstrip(',').split('\n') for x in "".join(pdf[i]).split(" ")])

        parsed = flatten(parsed)
        
        for i in range(0, len(parsed)):
            if parsed[i] == 'ASSIGNMENT' and parsed[i+1] == 'TITLE':
                start_i = i
            if parsed[i] == 'Required' and parsed[i+1] == 'Texts':
                end_i = i

        parsed = [x for x in parsed[start_i:end_i] if x != ''][5:]
        
        current_ass = []
        index = 0
        for i in range(0, len(parsed)):
            if parsed[i]=="Due":
                current_ass = parsed[index:i+4]
                index = i+4

                for i in range(0, len(current_ass)):
                    try:
                        copy = current_ass
                        done = False

                        #Weights
                        if current_ass[i][-1]=='x':
                            if len(current_ass[i])==2:
                                self.weights.append(int(current_ass[i][0]))
                                del copy[i]
                            else:
                                self.weights.append(int(current_ass[i][0:2]))
                                del copy[i]

                        #Released
                        if current_ass[i]=='Released':
                            week_r = int(current_ass[i+2])-1
                            day_r = current_ass[i+3]
                            if day_r == 'Monday': day_r = 1
                            elif day_r == 'Tuesday': day_r = 2
                            elif day_r =='Wednesday': day_r = 3
                            elif day_r == 'Thursday': day_r = 4
                            elif day_r == 'Friday': day_r = 5
                            elif day_r == 'Saturday': day_r = 6
                            elif day_r == 'Sunday': day_r = 7
                            self.released.append([week_r, day_r])
                            del copy[i:i+4]

                        #Due
                        if current_ass[i]=='Due':
                            week_d = int(current_ass[i+2])-1
                            day_d = current_ass[i+3]
                            if day_d == 'Monday': day_d = 1
                            elif day_d == 'Tuesday': day_d = 2
                            elif day_d == 'Wednesday': day_d = 3
                            elif day_d == 'Thursday': day_d = 4
                            elif day_d == 'Friday': day_d = 5
                            elif day_d == 'Saturday': day_d = 6
                            elif day_d == 'Sunday': day_d = 7
                            self.due.append([week_d, day_d])
                            del copy[i:i+4]
                            done = True
                    
                        if done:
                            self.titles.append(" ".join(copy))
                    except:
                        pass
            return parsed