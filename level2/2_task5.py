class Wordcounter:
    def __init__(self,filename):
        self.filename=filename
        self.counts={}
    def read_and_count(self):
        with open(self.filename,"r") as f:
            words=f.read().lower().split()
            for w in words:
                w=w.strip(".,!?;:\"()[]{}")
                if w:
                    self.counts[w]=self.counts.get(w,0) + 1

    def display(self):
        for word in sorted(self.counts):
            print(word,self.counts[word])

name=input("Enter file name: ")
wc=Wordcounter(name)
wc.read_and_count()
wc.display()