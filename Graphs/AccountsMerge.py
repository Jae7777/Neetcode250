# https://leetcode.com/problems/accounts-merge/
class UnionFind:
    def __init__(self, n):
        self.rep = [ i for i in range(n) ]
        self.rank = [1] * n
    def find(self, u):
        while u != self.rep[u]:
            self.rep[u] = self.rep[self.rep[u]]
            u = self.rep[u]
        return u
    def union(self, u, v):
        uRep, vRep = self.find(u), self.find(v)
        if uRep == vRep:
            return False
        if self.rank[uRep] > self.rank[vRep]:
            self.rep[vRep] = self.rep[uRep]
            self.rank[uRep] += self.rank[vRep]
        else:
            self.rep[uRep] = self.rep[vRep]
            self.rank[vRep] += self.rank[uRep]
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        email_to_acc = {} # acc index
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_acc:
                    uf.union(i, email_to_acc[email])
                else:
                    email_to_acc[email] = i
        acc_to_email = defaultdict(list)
        for email in email_to_acc:
            acc = uf.find(email_to_acc[email])
            acc_to_email[acc].append(email)
        res = []
        for acc in acc_to_email:
            name = accounts[acc][0]
            res.append([name] + sorted(acc_to_email[acc]))
        return res