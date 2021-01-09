from collections import deque
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        count = 0
        emailDir = {}
        for e in emails:
            s = ""
            email = ""
            q = deque(e)
            emailChars = []
            pos = False
            while s != '@':
                s = q[0]
                q.popleft()
                if s == '+':
                    pos = True
                if s != '@':
                    if not pos:
                        if s != '.':
                            emailChars.append(s)
            emailChars.append('@')
            while q:
                s = q[0]
                q.popleft()
                emailChars.append(s)
            email = "".join(emailChars)
            emailDir[email] = email
        return len(emailDir)