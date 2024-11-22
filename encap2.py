class super:
    var1=None
    _var2=None
    __var3=None
    def __init__(self,var1,var2,var3):
        self.var1=var1
        self._var2=var2
        self.__var3=var3

    def displaypublic(self):
        print("public data member:",self.var1)

    def _displayprotec(self):
        print("Protected memeber:",self._var2)
    def __displayrprivate(self):
        print("private member:",self.__var3)
    def accessprotect(self):
        self.__displayrprivate()
    
class sub(super):
    def __init__(self,var1,var2,var3):
        super.__init__(self,var1,var2,var3)
    def accessprivate(self):
        self._displayprotec()
obj=sub("Python",4,"Everyone")
obj.displaypublic()
obj.accessprotect()
obj.accessprivate()