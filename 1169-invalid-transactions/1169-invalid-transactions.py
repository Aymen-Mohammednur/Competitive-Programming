class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        """
        t1 - alice 20 800$ at mtv
        t2 - alice 50 100$ at beijing
        """
        
        store = defaultdict(list)
        res = set()
        for i, transaction in enumerate(transactions):
            name, time, amount, city = transaction.split(',')
            if int(amount) > 1000:
                res.add((transaction, i))
            if name in store:
                for tran, idx in store[name]:
                    n, t, a, c = tran.split(',')
                    if abs(int(time) - int(t)) <= 60 and city != c:
                        res.add((tran, idx))
                        res.add((transaction, i))
                        
            store[name].append((transaction, i))
        return [tran[0] for tran in res]