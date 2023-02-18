def intToRoman(num):
        """
        :type num: int
        :rtype: str
        
        s= 
        1956
        
        s=M
        856
        
        s=MD
        356
        
        s=MDC
        256
        s=MDCC
        156
        s=MDCCC
        56
        s=MDCCCL
        6
        
        
        M CM D CD C so on so forth
        M:1000
        CM:900
        D:500
        CD:400
        
        loop till num = 0
        iterate through symbol list
        
        i= num//symbol -> 1956//1000 = 1.95 => 1 - > 0 -> 1 ->0->0
        if i >= 1
            nums-=i -> 956 -> 56
            s+=symbol -> MCM
        else: pop symbol //why? cuz were never gonna use it again and we iterate through the list - > M CM D CD C -> CM D CD C -> D CD C -> CD C
        
         
        """
        
        symbolValues = {'I':1,'IV':4,'V':5,'IX':9,'X':10,'XL':40,'L':50,'XC':90,'C':100,'CD':400,'D':500,'CM':900,'M':1000}
        symbols = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        s=[]
        while num!=0:
            symbol = symbols[-1]
            i = num//symbolValues[symbol]
            if i>=1:
                num-=symbolValues[symbol]*i
                s.append(symbol*i)
            else: symbols.pop()
        return ''.join(s)

print(intToRoman(1994)) # MCMXCIV
print(intToRoman(3)) # III
print(intToRoman(58)) # LVIII
print(intToRoman(100)) # C
        