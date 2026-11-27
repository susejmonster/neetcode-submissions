class Solution:
    class DSU:
        def __init__(self,N):
            self.parents = list(range(N))##initializer
        def union(self,child,parent):
            self.parents[self.find(child)] = self.find(parent)##find climbs to root of child subtree and connects to found root of parent subtree
        def find(self,x):
            if x!=self.parents[x]:
                self.parents[x] = self.find(self.parents[x])##path compression
            return self.parents[x]
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        #same accnt => common email, they may have same name
        #out-> name:sorted emials.

        ##for each i , store the diff email address in stackok
        ##if for next i,  the stack contains an email address, they are to be merged->DSU needed
        ##if not skips
        ##return as [name:emails] , [name:emails] etc
        dsu = self.DSU(len(accounts))
        mp = {}
        for i in range(0,len(accounts)):  
            for email in accounts[i][1:]:##j  = "john" , "xyz@gmail" [1:] start from 1
                if email in mp:
                    dsu.union(i,mp[email]) ## the i that we are on, and the index that te email belongs to 
                mp[email] = i 
        print(mp)
        print("Raw parents:", dsu.parents)
        print("Final bosses:", [dsu.find(i) for i in range(len(accounts))])
        ans = {}
        for email, owner in mp.items():
            root = dsu.find(owner)
            if root not in ans:
                ans[root] = []
            ans[root].append(email)

        return [[accounts[i][0]] + sorted(emails) for i, emails in ans.items()]
