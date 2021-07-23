#To change the rgb to hexcode
def RGB_to_HEX(Seperate):
    if Seperate[0]<=255 and Seperate[1]<=255 and Seperate[2]<=255:
        FinalString="#"
        for i in range(len(Seperate)):
            num=Seperate[i]
            HexD=""
            while num>=1:
                rem=ChangeIf(num%16)
                HexD+=str(rem)
                num=num//16
            HexD=HexD[::-1]
            if len(HexD)<2:
                HexD="0"+HexD
            FinalString+=HexD
        return FinalString         
    else:
        return "NA"
#To change the value of remainter if its greater than 9
def ChangeIf(rem):
    if rem>=10:
        HighScale=[10,11,12,13,14,15]
        ToConvert=["A", "B", "C", "D", "E", "F"]
        for i in range(len(HighScale)):
            if rem==HighScale[i]:
                rem=ToConvert[i]
                return rem
    else:
        return rem

#Seperating the input given into a clean list
string=input()
winstart,winend=0,0
Seperate=[]
for winend in range(len(string)-1):
    i=winend
    if winend>=winstart:
        while i<len(string) and string[i]!="-":
            Var=string[winstart:i+1]
            i+=1
        winstart=i+1
        Seperate.append(int(Var))
# print(Seperate)
ans=RGB_to_HEX(Seperate)
print(ans)



#test case1:
#207-50-150
#CF3296

#test case 2:
#200-178-15
#C8B20F
