class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        def helper(domain):
            res = []
            d = domain.split('.')
            for i in range(len(d) - 1, -1, -1):
                if not res:
                    res.append(d[i])
                else:
                    res.append(d[i] + '.' + res[-1])
            return res
        
        counter = defaultdict(int)
        for cpdomain in cpdomains:
            count, domain = cpdomain.split(' ')
            domains = helper(domain)
            for dom in domains:
                counter[dom] += int(count)
        
        res = []
        for domain in counter:
            res.append(str(counter[domain]) + ' ' + domain)
        return res