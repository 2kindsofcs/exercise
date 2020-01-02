class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueEmailList = []
        for email in emails:
            plusIndex = email.find('+')
            domainIndex = email.find('@')
            local = email[:domainIndex]
            domain = email[domainIndex:]
            if plusIndex > -1:
                local = local[:plusIndex]
            if '.' in local:
                local = local.replace('.', '')
            address = local + domain
            if address not in uniqueEmailList:
                uniqueEmailList.append(address)
        count = len(uniqueEmailList)
        return count
        
# Runtime: 44 ms, faster than 95.97% of Python3 online submissions for Unique Email Addresses.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Unique Email Addresses.
