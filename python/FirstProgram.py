n = 5

# # Upper half
# for i in range(1, n):
#     # Left numbers
#     for j in range(1, i+1):
#         print(j, end="")
#     # Spaces
#     for j in range(2*(n-i)):
#         print(" ", end="")
#     # Right numbers
#     for j in range(1, i+1):
#         print(j, end="")
#     print()

# # Lower half
# for i in range(n, 0, -1):
#     # Left numbers
#     for j in range(1, i+1):
#         print(j, end="")
#     # Spaces
#     for j in range(2*(n-i)):
#         print(" ", end="")
#     # Right numbers
#     for j in range(1, i+1):
#         print(j, end="")
#     print()

# 1        1
# 12      12
# 123    123
# 1234  1234
# 1234512345
# 1234  1234
# 123    123
# 12      12
# 1        1



# for i in range(1,n+1):
#     for j in range(i,n+1):
#         print(" ",end="")
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

#      1 
#     1 2
#    1 2 3
#   1 2 3 4
#  1 2 3 4 5

# for i in range(1,n+1):
#     for j in range(i,n+1):
#         print(" ",end="")
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

#      1 
#     2 2
#    3 3 3
#   4 4 4 4
#  5 5 5 5 5

# for i in range(1,n+1):
#     for j in range(i,n+1):
#         print(" ",end="")
#     for j in range(1,i+1):
#         if i%2==0:
#             print("#",end=" ")
#         else:
#             print("*",end=" ")
#     print()

#      * 
#     # #
#    * * *
#   # # # #
#  * * * * *

# for i in range(1,n+1):
#     for j in range(i):
#        print((i+j)%2, end=" ")
#     print()

# 1 
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(" ",end="")
#     for j in range(i,n+1):
#         print("* ",end="")
#     print()

#  * * * * * 
#   * * * *
#    * * *
#     * *
#      *

# for i in range(1,n+1):
#     for j in range(i,n+1):
#         print(" ",end="")
#     for j in range(1,i+1):
#         print("* ",end="")
#     print()

#      * 
#     * *
#    * * *
#   * * * *
#  * * * * *

# alpabet

# for i in range(1,n+1):
#     for j in range(i,n+1):
#         print(" ",end="")
#         char=65
#     for j in range(1,i+1):
#         print(chr(char),end=" ")
#         char+=1
#     print()

#      A 
#     A B
#    A B C
#   A B C D
#  A B C D E

# char=65
# for i in range(1,n+1):
#     for j in range(i,n+1):
#         print(" ",end="")
#     for j in range(1,i+1):
#         print(chr(char),end=" ")
#         char+=1
#     print()

#      A 
#     B C 
#    D E F 
#   G H I J 
#  K L M N O 

# char=65
# for i in range(1,n+1):
#     for j in range(i,n+1):
#         print(" ",end="")
        
#     for j in range(1,i+1):
#         print(chr(char),end=" ")
#     char+=1
#     print()

#      A 
#     B B
#    C C C
#   D D D D
#  E E E E E


# Drum
# for i in range(1,n):
#     for j in range(1,i+1):
#         print(" ",end="")
#     for j in range(i,n+1):
#         print(j,end=" ")
#     print()
# for i in range(1,n+1):
#     for j in range(i,n+1):
#         print(" ",end="")
#         k=n
#     for j in range(1,i+1):
#         print(k,end=" ")
#         k-=1
#     print()

#  1 2 3 4 5 
#   2 3 4 5
#    3 4 5
#     4 5
#      5
#     5 4
#    5 4 3
#   5 4 3 2
#  5 4 3 2 1

# star
# for i in range(1,n):
#     print("*"*i+" "*(2*(n-i))+"*"*i)
# for i in range(n,0,-1):
#     print("*"*i+" "*(2*(n-i))+"*"*i)

# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

# 1
# 12
# 123
# 1234
# 12345

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if(i%2==0):
#             print("2",end="")
#         else:
#             print("1",end="")
#     print()

# 1
# 22
# 111
# 2222
# 11111

# k=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(k,end="")
#         k+=1
#     print()

# 1
# 23
# 456
# 78910
# 1112131415


# for i in range(1,n):
#     for j in range(i,n+1):
#         print(" ",end="")
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(" ",end="")
#         k=n
#     for j in range(i,n+1):
#         print(k,end=" ")
#         k-=1
#     print()

#      1 
#     1 2 
#    1 2 3 
#   1 2 3 4 
#  5 4 3 2 1 
#   5 4 3 2 
#    5 4 3 
#     5 4 
#      5 

for i in range(n):
    for j in range(n,i,-1):
        print("*",end=" ")
    for j in range(i):
        print(" "*3,end=" ")
    for j in range(n,i,-1):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    for j in range(n,i+1,-1):
        print(" "*3,end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()