ax1, ay1, ax2, ay2 = [ int(i) for i in input("1-й прямоугольник - x y w h: ").split() ]
ax2 = ax1 + ax2
ay2 = ay1 + ay2

bx1, by1, bx2, by2 = [ int(i) for i in input("2-й прямоугольник - x y w h: ").split() ]
bx2 = bx1 + bx2
by2 = by1 + by2

s1 = ( ax1>=bx1 and ax1<=bx2 ) or ( ax2>=bx1 and ax2<=bx2 )
s2 = ( ay1>=by1 and ay1<=by2 ) or ( ay2>=by1 and ay2<=by2 )
s3 = ( bx1>=ax1 and bx1<=ax2 ) or ( bx2>=ax1 and bx2<=ax2 )
s4 = ( by1>=ay1 and by1<=ay2 ) or ( by2>=ay1 and by2<=ay2 )

print( "YES" if ((s1 and s2) or (s3 and s4)) or ((s1 and s4) or (s3 and s2)) else "NO" )
if self.mouse_pos[0] >= x and self.mouse_pos[0] <= x + 100:
            self.btn.move(randint(1, 400), randint(1, 460))
