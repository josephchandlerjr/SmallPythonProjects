class Test:
    def setAttr(self,x):
        self.attr = x


t = Test()


print(t)
t.setAttr(1)
print(t.attr)
Test.setAttr(t,44)
print(t.attr)
