data = '''
# Linear combinations of elements from A
a0 = (0.5+0.5j)*A[0,0] + (0.5+0.5j)*A[0,1] + (0.5+-0.5j)*A[1,0] + (0.5+-0.5j)*A[1,1] + (0.5+-0.5j)*A[2,0] + (0.5+-0.5j)*A[2,1] + (0.5+-0.5j)*A[3,0] + (0.5+-0.5j)*A[3,1]
a1 = (0.5+0.5j)*A[0,0] + (-0.5+0.5j)*A[0,3] + (0.5+0.5j)*A[1,0] + (-0.5+0.5j)*A[1,3] + (-0.5+-0.5j)*A[2,0] + (0.5+-0.5j)*A[2,3] + (0.5+-0.5j)*A[3,0] + (0.5+0.5j)*A[3,3]
a2 = -0.5*A[0,1] + 0.5*A[0,2] + -0.5j*A[1,1] + 0.5j*A[1,2] + 0.5j*A[2,1] + -0.5j*A[2,2] + -0.5j*A[3,1] + 0.5j*A[3,2]
a3 = -0.5j*A[0,0] + -0.5*A[0,1] + 0.5*A[0,2] + -0.5*A[0,3] + 0.5j*A[1,0] + -0.5*A[1,1] + 0.5*A[1,2] + 0.5*A[1,3] + -0.5j*A[2,0] + -0.5*A[2,1] + 0.5*A[2,2] + -0.5*A[2,3] + -0.5*A[3,0] + -0.5j*A[3,1] + 0.5j*A[3,2] + 0.5j*A[3,3]
a4 = (0.5+0.5j)*A[0,0] + (-0.5+-0.5j)*A[0,1] + (-0.5+0.5j)*A[1,0] + (0.5+-0.5j)*A[1,1] + (-0.5+0.5j)*A[2,0] + (0.5+-0.5j)*A[2,1] + (0.5+-0.5j)*A[3,0] + (-0.5+0.5j)*A[3,1]
a5 = (0.5+-0.5j)*A[0,2] + (-0.5+-0.5j)*A[0,3] + (0.5+-0.5j)*A[1,2] + (-0.5+-0.5j)*A[1,3] + (-0.5+0.5j)*A[2,2] + (0.5+0.5j)*A[2,3] + (-0.5+-0.5j)*A[3,2] + (-0.5+0.5j)*A[3,3]
a6 = 0.5j*A[0,0] + 0.5*A[0,3] + -0.5*A[1,0] + 0.5j*A[1,3] + 0.5*A[2,0] + -0.5j*A[2,3] + -0.5*A[3,0] + 0.5j*A[3,3]
a7 = (0.5+0.5j)*A[0,0] + (-0.5+-0.5j)*A[0,1] + (-0.5+-0.5j)*A[1,0] + (0.5+0.5j)*A[1,1] + (-0.5+-0.5j)*A[2,0] + (0.5+0.5j)*A[2,1] + (-0.5+0.5j)*A[3,0] + (0.5+-0.5j)*A[3,1]
a8 = -0.5j*A[0,0] + -0.5j*A[0,1] + -0.5*A[0,2] + -0.5j*A[0,3] + 0.5*A[1,0] + 0.5*A[1,1] + -0.5j*A[1,2] + 0.5*A[1,3] + -0.5*A[2,0] + -0.5*A[2,1] + -0.5j*A[2,2] + 0.5*A[2,3] + 0.5*A[3,0] + 0.5*A[3,1] + 0.5j*A[3,2] + -0.5*A[3,3]
a9 = (-0.5+0.5j)*A[0,0] + (-0.5+-0.5j)*A[0,3] + (0.5+0.5j)*A[1,0] + (-0.5+0.5j)*A[1,3] + (-0.5+-0.5j)*A[2,0] + (0.5+-0.5j)*A[2,3] + (-0.5+-0.5j)*A[3,0] + (0.5+-0.5j)*A[3,3]
a10 = (-0.5+0.5j)*A[0,0] + (0.5+-0.5j)*A[0,1] + (-0.5+0.5j)*A[1,0] + (0.5+-0.5j)*A[1,1] + (0.5+-0.5j)*A[2,0] + (-0.5+0.5j)*A[2,1] + (0.5+0.5j)*A[3,0] + (-0.5+-0.5j)*A[3,1]
a11 = 0.5*A[0,0] + 0.5*A[0,1] + -0.5j*A[0,2] + -0.5*A[0,3] + -0.5*A[1,0] + -0.5*A[1,1] + 0.5j*A[1,2] + 0.5*A[1,3] + 0.5*A[2,0] + 0.5*A[2,1] + 0.5j*A[2,2] + 0.5*A[2,3] + -0.5j*A[3,0] + -0.5j*A[3,1] + 0.5*A[3,2] + -0.5j*A[3,3]
a12 = (0.5+0.5j)*A[0,1] + (-0.5+-0.5j)*A[0,2] + (-0.5+0.5j)*A[1,1] + (0.5+-0.5j)*A[1,2] + (-0.5+0.5j)*A[2,1] + (0.5+-0.5j)*A[2,2] + (0.5+-0.5j)*A[3,1] + (-0.5+0.5j)*A[3,2]
a13 = (0.5+-0.5j)*A[0,1] + (-0.5+0.5j)*A[0,2] + (0.5+-0.5j)*A[1,1] + (-0.5+0.5j)*A[1,2] + (0.5+-0.5j)*A[2,1] + (-0.5+0.5j)*A[2,2] + (0.5+0.5j)*A[3,1] + (-0.5+-0.5j)*A[3,2]
a14 = 0.5j*A[0,0] + -0.5*A[0,1] + 0.5*A[0,2] + -0.5*A[0,3] + 0.5*A[1,0] + -0.5j*A[1,1] + 0.5j*A[1,2] + 0.5j*A[1,3] + 0.5*A[2,0] + 0.5j*A[2,1] + -0.5j*A[2,2] + 0.5j*A[2,3] + 0.5*A[3,0] + -0.5j*A[3,1] + 0.5j*A[3,2] + 0.5j*A[3,3]
a15 = (-0.5+0.5j)*A[0,2] + (0.5+0.5j)*A[0,3] + (0.5+-0.5j)*A[1,2] + (-0.5+-0.5j)*A[1,3] + (0.5+-0.5j)*A[2,2] + (-0.5+-0.5j)*A[2,3] + (-0.5+-0.5j)*A[3,2] + (-0.5+0.5j)*A[3,3]
a16 = -0.5*A[0,0] + 0.5j*A[0,1] + 0.5j*A[0,2] + -0.5j*A[0,3] + -0.5*A[1,0] + -0.5j*A[1,1] + -0.5j*A[1,2] + -0.5j*A[1,3] + -0.5*A[2,0] + 0.5j*A[2,1] + 0.5j*A[2,2] + -0.5j*A[2,3] + -0.5j*A[3,0] + 0.5*A[3,1] + 0.5*A[3,2] + 0.5*A[3,3]
a17 = (0.5+0.5j)*A[0,0] + (0.5+0.5j)*A[0,1] + (0.5+0.5j)*A[1,0] + (0.5+0.5j)*A[1,1] + (0.5+0.5j)*A[2,0] + (0.5+0.5j)*A[2,1] + (-0.5+0.5j)*A[3,0] + (-0.5+0.5j)*A[3,1]
a18 = 0.5j*A[0,0] + 0.5j*A[0,1] + -0.5*A[0,2] + 0.5j*A[0,3] + 0.5j*A[1,0] + 0.5j*A[1,1] + -0.5*A[1,2] + 0.5j*A[1,3] + 0.5j*A[2,0] + 0.5j*A[2,1] + 0.5*A[2,2] + -0.5j*A[2,3] + -0.5*A[3,0] + -0.5*A[3,1] + 0.5j*A[3,2] + 0.5*A[3,3]
a19 = (0.5+-0.5j)*A[0,2] + (0.5+0.5j)*A[0,3] + (0.5+-0.5j)*A[1,2] + (0.5+0.5j)*A[1,3] + (0.5+-0.5j)*A[2,2] + (0.5+0.5j)*A[2,3] + (0.5+0.5j)*A[3,2] + (-0.5+0.5j)*A[3,3]
a20 = (0.5+0.5j)*A[0,1] + (-0.5+-0.5j)*A[0,2] + (0.5+0.5j)*A[1,1] + (-0.5+-0.5j)*A[1,2] + (-0.5+-0.5j)*A[2,1] + (0.5+0.5j)*A[2,2] + (0.5+-0.5j)*A[3,1] + (-0.5+0.5j)*A[3,2]
a21 = 0.5j*A[0,0] + -0.5j*A[0,1] + -0.5*A[0,2] + -0.5j*A[0,3] + -0.5j*A[1,0] + 0.5j*A[1,1] + 0.5*A[1,2] + 0.5j*A[1,3] + -0.5j*A[2,0] + 0.5j*A[2,1] + -0.5*A[2,2] + -0.5j*A[2,3] + -0.5*A[3,0] + 0.5*A[3,1] + 0.5j*A[3,2] + -0.5*A[3,3]
a22 = (-0.5+-0.5j)*A[0,0] + (-0.5+0.5j)*A[0,3] + (0.5+-0.5j)*A[1,0] + (-0.5+-0.5j)*A[1,3] + (0.5+-0.5j)*A[2,0] + (-0.5+-0.5j)*A[2,3] + (-0.5+0.5j)*A[3,0] + (0.5+0.5j)*A[3,3]
a23 = (-0.5+-0.5j)*A[0,2] + (0.5+-0.5j)*A[0,3] + (0.5+-0.5j)*A[1,2] + (0.5+0.5j)*A[1,3] + (0.5+-0.5j)*A[2,2] + (0.5+0.5j)*A[2,3] + (-0.5+0.5j)*A[3,2] + (-0.5+-0.5j)*A[3,3]
a24 = -0.5*A[0,0] + 0.5*A[0,1] + -0.5j*A[0,2] + -0.5*A[0,3] + -0.5j*A[1,0] + 0.5j*A[1,1] + 0.5*A[1,2] + -0.5j*A[1,3] + -0.5j*A[2,0] + 0.5j*A[2,1] + -0.5*A[2,2] + 0.5j*A[2,3] + 0.5j*A[3,0] + -0.5j*A[3,1] + 0.5*A[3,2] + -0.5j*A[3,3]
a25 = (0.5+-0.5j)*A[0,2] + (0.5+0.5j)*A[0,3] + (-0.5+-0.5j)*A[1,2] + (0.5+-0.5j)*A[1,3] + (0.5+0.5j)*A[2,2] + (-0.5+0.5j)*A[2,3] + (0.5+0.5j)*A[3,2] + (-0.5+0.5j)*A[3,3]
a26 = (0.5+0.5j)*A[0,1] + (0.5+0.5j)*A[0,2] + (-0.5+-0.5j)*A[1,1] + (-0.5+-0.5j)*A[1,2] + (0.5+0.5j)*A[2,1] + (0.5+0.5j)*A[2,2] + (0.5+-0.5j)*A[3,1] + (0.5+-0.5j)*A[3,2]
a27 = -0.5j*A[0,0] + -0.5j*A[0,1] + 0.5*A[0,2] + 0.5j*A[0,3] + -0.5*A[1,0] + -0.5*A[1,1] + -0.5j*A[1,2] + 0.5*A[1,3] + -0.5*A[2,0] + -0.5*A[2,1] + 0.5j*A[2,2] + -0.5*A[2,3] + -0.5*A[3,0] + -0.5*A[3,1] + 0.5j*A[3,2] + -0.5*A[3,3]
a28 = (-0.5+0.5j)*A[0,0] + (-0.5+0.5j)*A[0,1] + (-0.5+-0.5j)*A[1,0] + (-0.5+-0.5j)*A[1,1] + (0.5+0.5j)*A[2,0] + (0.5+0.5j)*A[2,1] + (-0.5+-0.5j)*A[3,0] + (-0.5+-0.5j)*A[3,1]
a29 = (0.5+0.5j)*A[0,0] + (0.5+-0.5j)*A[0,3] + (-0.5+-0.5j)*A[1,0] + (-0.5+0.5j)*A[1,3] + (0.5+0.5j)*A[2,0] + (0.5+-0.5j)*A[2,3] + (0.5+-0.5j)*A[3,0] + (-0.5+-0.5j)*A[3,3]
a30 = (0.5+0.5j)*A[0,1] + (0.5+0.5j)*A[0,2] + (-0.5+-0.5j)*A[1,1] + (-0.5+-0.5j)*A[1,2] + (-0.5+-0.5j)*A[2,1] + (-0.5+-0.5j)*A[2,2] + (-0.5+0.5j)*A[3,1] + (-0.5+0.5j)*A[3,2]
a31 = 0.5*A[0,0] + -0.5*A[0,1] + -0.5j*A[0,2] + 0.5*A[0,3] + 0.5*A[1,0] + -0.5*A[1,1] + -0.5j*A[1,2] + 0.5*A[1,3] + -0.5*A[2,0] + 0.5*A[2,1] + -0.5j*A[2,2] + 0.5*A[2,3] + -0.5j*A[3,0] + 0.5j*A[3,1] + 0.5*A[3,2] + 0.5j*A[3,3]
a32 = (0.5+0.5j)*A[0,2] + (0.5+-0.5j)*A[0,3] + (-0.5+0.5j)*A[1,2] + (0.5+0.5j)*A[1,3] + (0.5+-0.5j)*A[2,2] + (-0.5+-0.5j)*A[2,3] + (-0.5+0.5j)*A[3,2] + (0.5+0.5j)*A[3,3]
a33 = 0.5*A[0,0] + 0.5j*A[0,1] + -0.5j*A[0,2] + -0.5j*A[0,3] + -0.5*A[1,0] + 0.5j*A[1,1] + -0.5j*A[1,2] + 0.5j*A[1,3] + -0.5*A[2,0] + -0.5j*A[2,1] + 0.5j*A[2,2] + 0.5j*A[2,3] + 0.5j*A[3,0] + 0.5*A[3,1] + -0.5*A[3,2] + 0.5*A[3,3]
a34 = -0.5j*A[0,0] + 0.5j*A[0,1] + -0.5*A[0,2] + 0.5j*A[0,3] + -0.5*A[1,0] + 0.5*A[1,1] + 0.5j*A[1,2] + 0.5*A[1,3] + 0.5*A[2,0] + -0.5*A[2,1] + 0.5j*A[2,2] + 0.5*A[2,3] + 0.5*A[3,0] + -0.5*A[3,1] + 0.5j*A[3,2] + 0.5*A[3,3]
a35 = (0.5+-0.5j)*A[0,2] + (0.5+0.5j)*A[0,3] + (-0.5+0.5j)*A[1,2] + (-0.5+-0.5j)*A[1,3] + (0.5+-0.5j)*A[2,2] + (0.5+0.5j)*A[2,3] + (-0.5+-0.5j)*A[3,2] + (0.5+-0.5j)*A[3,3]
a36 = (-0.5+-0.5j)*A[0,1] + (-0.5+-0.5j)*A[0,2] + (-0.5+0.5j)*A[1,1] + (-0.5+0.5j)*A[1,2] + (0.5+-0.5j)*A[2,1] + (0.5+-0.5j)*A[2,2] + (0.5+-0.5j)*A[3,1] + (0.5+-0.5j)*A[3,2]
a37 = 0.5*A[0,0] + -0.5j*A[0,1] + -0.5j*A[0,2] + -0.5j*A[0,3] + 0.5j*A[1,0] + -0.5*A[1,1] + -0.5*A[1,2] + 0.5*A[1,3] + 0.5j*A[2,0] + 0.5*A[2,1] + 0.5*A[2,2] + 0.5*A[2,3] + -0.5j*A[3,0] + 0.5*A[3,1] + 0.5*A[3,2] + -0.5*A[3,3]
a38 = (0.5+-0.5j)*A[0,1] + (0.5+-0.5j)*A[0,2] + (-0.5+-0.5j)*A[1,1] + (-0.5+-0.5j)*A[1,2] + (-0.5+-0.5j)*A[2,1] + (-0.5+-0.5j)*A[2,2] + (-0.5+-0.5j)*A[3,1] + (-0.5+-0.5j)*A[3,2]
a39 = -0.5*A[0,0] + -0.5j*A[0,1] + -0.5j*A[0,2] + -0.5j*A[0,3] + -0.5*A[1,0] + 0.5j*A[1,1] + 0.5j*A[1,2] + -0.5j*A[1,3] + 0.5*A[2,0] + 0.5j*A[2,1] + 0.5j*A[2,2] + 0.5j*A[2,3] + 0.5j*A[3,0] + 0.5*A[3,1] + 0.5*A[3,2] + -0.5*A[3,3]
a40 = (-0.5+-0.5j)*A[0,0] + (-0.5+-0.5j)*A[0,1] + (0.5+0.5j)*A[1,0] + (0.5+0.5j)*A[1,1] + (-0.5+-0.5j)*A[2,0] + (-0.5+-0.5j)*A[2,1] + (-0.5+0.5j)*A[3,0] + (-0.5+0.5j)*A[3,1]
a41 = (0.5+-0.5j)*A[0,0] + (-0.5+-0.5j)*A[0,3] + (-0.5+0.5j)*A[1,0] + (0.5+0.5j)*A[1,3] + (-0.5+0.5j)*A[2,0] + (0.5+0.5j)*A[2,3] + (0.5+0.5j)*A[3,0] + (0.5+-0.5j)*A[3,3]
a42 = (0.5+0.5j)*A[0,0] + (-0.5+0.5j)*A[0,3] + (0.5+-0.5j)*A[1,0] + (0.5+0.5j)*A[1,3] + (0.5+-0.5j)*A[2,0] + (0.5+0.5j)*A[2,3] + (0.5+-0.5j)*A[3,0] + (0.5+0.5j)*A[3,3]
a43 = 0.5j*A[0,0] + 0.5*A[0,1] + -0.5*A[0,2] + -0.5*A[0,3] + 0.5*A[1,0] + 0.5j*A[1,1] + -0.5j*A[1,2] + 0.5j*A[1,3] + -0.5*A[2,0] + 0.5j*A[2,1] + -0.5j*A[2,2] + -0.5j*A[2,3] + -0.5*A[3,0] + -0.5j*A[3,1] + 0.5j*A[3,2] + -0.5j*A[3,3]
a44 = (0.5+-0.5j)*A[0,2] + (-0.5+-0.5j)*A[0,3] + (-0.5+-0.5j)*A[1,2] + (-0.5+0.5j)*A[1,3] + (-0.5+-0.5j)*A[2,2] + (-0.5+0.5j)*A[2,3] + (-0.5+-0.5j)*A[3,2] + (-0.5+0.5j)*A[3,3]
a45 = (-0.5+0.5j)*A[0,0] + (0.5+-0.5j)*A[0,1] + (0.5+0.5j)*A[1,0] + (-0.5+-0.5j)*A[1,1] + (-0.5+-0.5j)*A[2,0] + (0.5+0.5j)*A[2,1] + (-0.5+-0.5j)*A[3,0] + (0.5+0.5j)*A[3,1]
a46 = (0.5+-0.5j)*A[0,0] + (0.5+0.5j)*A[0,3] + (0.5+-0.5j)*A[1,0] + (0.5+0.5j)*A[1,3] + (0.5+-0.5j)*A[2,0] + (0.5+0.5j)*A[2,3] + (0.5+0.5j)*A[3,0] + (-0.5+0.5j)*A[3,3]
a47 = 0.5*A[0,0] + 0.5j*A[0,1] + 0.5j*A[0,2] + -0.5j*A[0,3] + 0.5j*A[1,0] + 0.5*A[1,1] + 0.5*A[1,2] + 0.5*A[1,3] + -0.5j*A[2,0] + 0.5*A[2,1] + 0.5*A[2,2] + -0.5*A[2,3] + 0.5j*A[3,0] + 0.5*A[3,1] + 0.5*A[3,2] + 0.5*A[3,3]

# Linear combinations of elements from B
b0 = -0.5*B[0,0] + -0.5*B[1,0] + 0.5*B[2,0] + -0.5j*B[3,0]
b1 = 0.5j*B[0,1] + 0.5j*B[0,3] + 0.5j*B[1,1] + 0.5j*B[1,3] + 0.5j*B[2,1] + 0.5j*B[2,3] + 0.5*B[3,1] + 0.5*B[3,3]
b2 = (0.5+0.5j)*B[0,1] + (-0.5+-0.5j)*B[1,1] + (0.5+0.5j)*B[2,1] + (0.5+-0.5j)*B[3,1]
b3 = -0.5j*B[0,0] + 0.5j*B[0,2] + -0.5j*B[1,1] + -0.5j*B[1,2] + 0.5j*B[2,1] + 0.5j*B[2,2] + 0.5*B[3,0] + -0.5*B[3,2]
b4 = -0.5*B[0,0] + 0.5*B[0,2] + 0.5*B[0,3] + 0.5*B[1,0] + -0.5*B[1,2] + -0.5*B[1,3] + 0.5*B[2,0] + -0.5*B[2,2] + -0.5*B[2,3] + 0.5j*B[3,0] + -0.5j*B[3,2] + -0.5j*B[3,3]
b5 = 0.5*B[0,1] + 0.5*B[0,3] + 0.5*B[1,1] + 0.5*B[1,3] + 0.5*B[2,1] + 0.5*B[2,3] + 0.5j*B[3,1] + 0.5j*B[3,3]
b6 = (-0.5+-0.5j)*B[0,1] + (0.5+0.5j)*B[1,1] + (0.5+0.5j)*B[2,1] + (0.5+-0.5j)*B[3,1]
b7 = -0.5*B[0,0] + 0.5*B[0,3] + 0.5*B[1,0] + -0.5*B[1,3] + -0.5*B[2,0] + 0.5*B[2,3] + 0.5j*B[3,0] + -0.5j*B[3,3]
b8 = 0.5*B[0,0] + -0.5*B[0,2] + -0.5*B[0,3] + 0.5*B[1,0] + -0.5*B[1,2] + -0.5*B[1,3] + 0.5*B[2,1] + -0.5j*B[3,1]
b9 = 0.5j*B[0,1] + 0.5j*B[0,2] + 0.5j*B[0,3] + 0.5j*B[1,1] + 0.5j*B[1,2] + 0.5j*B[1,3] + -0.5j*B[2,1] + -0.5j*B[2,2] + -0.5j*B[2,3] + 0.5*B[3,1] + 0.5*B[3,2] + 0.5*B[3,3]
b10 = 0.5j*B[0,1] + 0.5j*B[0,3] + -0.5j*B[1,1] + -0.5j*B[1,3] + -0.5j*B[2,1] + -0.5j*B[2,3] + -0.5*B[3,1] + -0.5*B[3,3]
b11 = -0.5j*B[0,0] + 0.5j*B[0,3] + -0.5j*B[1,0] + 0.5j*B[1,3] + 0.5j*B[2,1] + 0.5j*B[2,2] + -0.5*B[3,1] + -0.5*B[3,2]
b12 = -0.5*B[0,0] + 0.5*B[0,2] + 0.5*B[0,3] + -0.5*B[1,0] + 0.5*B[1,2] + 0.5*B[1,3] + 0.5*B[2,0] + -0.5*B[2,2] + -0.5*B[2,3] + 0.5j*B[3,0] + -0.5j*B[3,2] + -0.5j*B[3,3]
b13 = 0.5j*B[0,0] + -0.5j*B[0,2] + -0.5j*B[1,0] + 0.5j*B[1,2] + 0.5j*B[2,0] + -0.5j*B[2,2] + -0.5*B[3,0] + 0.5*B[3,2]
b14 = -0.5*B[0,1] + -0.5*B[1,0] + 0.5*B[2,0] + 0.5j*B[3,1]
b15 = 0.5j*B[0,0] + -0.5j*B[0,3] + 0.5j*B[1,0] + -0.5j*B[1,3] + -0.5j*B[2,0] + 0.5j*B[2,3] + 0.5*B[3,0] + -0.5*B[3,3]
b16 = 0.5*B[0,1] + 0.5*B[0,2] + 0.5*B[1,0] + -0.5*B[1,2] + 0.5*B[2,0] + -0.5*B[2,2] + -0.5j*B[3,1] + -0.5j*B[3,2]
b17 = -0.5j*B[0,0] + 0.5j*B[0,2] + -0.5j*B[1,0] + 0.5j*B[1,2] + -0.5j*B[2,0] + 0.5j*B[2,2] + 0.5*B[3,0] + -0.5*B[3,2]
b18 = -0.5j*B[0,1] + -0.5j*B[0,3] + -0.5j*B[1,1] + -0.5j*B[1,3] + -0.5j*B[2,0] + 0.5j*B[2,2] + 0.5*B[3,0] + -0.5*B[3,2]
b19 = -0.5j*B[0,0] + 0.5j*B[0,2] + 0.5j*B[1,0] + -0.5j*B[1,2] + 0.5j*B[2,0] + -0.5j*B[2,2] + 0.5*B[3,0] + -0.5*B[3,2]
b20 = -0.5j*B[0,1] + -0.5j*B[0,3] + -0.5j*B[1,1] + -0.5j*B[1,3] + 0.5j*B[2,1] + 0.5j*B[2,3] + 0.5*B[3,1] + 0.5*B[3,3]
b21 = -0.5*B[0,1] + -0.5*B[0,2] + 0.5*B[1,1] + 0.5*B[1,2] + -0.5*B[2,0] + 0.5*B[2,3] + 0.5j*B[3,0] + -0.5j*B[3,3]
b22 = -0.5j*B[0,0] + 0.5j*B[0,2] + 0.5j*B[0,3] + -0.5j*B[1,0] + 0.5j*B[1,2] + 0.5j*B[1,3] + -0.5j*B[2,0] + 0.5j*B[2,2] + 0.5j*B[2,3] + 0.5*B[3,0] + -0.5*B[3,2] + -0.5*B[3,3]
b23 = -0.5*B[0,0] + 0.5*B[0,2] + 0.5*B[0,3] + -0.5*B[1,0] + 0.5*B[1,2] + 0.5*B[1,3] + -0.5*B[2,0] + 0.5*B[2,2] + 0.5*B[2,3] + 0.5j*B[3,0] + -0.5j*B[3,2] + -0.5j*B[3,3]
b24 = 0.5j*B[0,1] + -0.5j*B[1,1] + -0.5j*B[2,0] + 0.5j*B[2,2] + 0.5j*B[2,3] + 0.5*B[3,0] + -0.5*B[3,2] + -0.5*B[3,3]
b25 = 0.5j*B[0,1] + 0.5j*B[0,2] + 0.5j*B[0,3] + 0.5j*B[1,1] + 0.5j*B[1,2] + 0.5j*B[1,3] + -0.5j*B[2,1] + -0.5j*B[2,2] + -0.5j*B[2,3] + -0.5*B[3,1] + -0.5*B[3,2] + -0.5*B[3,3]
b26 = 0.5*B[0,1] + 0.5*B[0,2] + -0.5*B[1,1] + -0.5*B[1,2] + -0.5*B[2,1] + -0.5*B[2,2] + -0.5j*B[3,1] + -0.5j*B[3,2]
b27 = 0.5j*B[0,1] + 0.5j*B[0,2] + 0.5j*B[0,3] + 0.5j*B[1,1] + 0.5j*B[1,2] + 0.5j*B[1,3] + -0.5j*B[2,0] + -0.5*B[3,0]
b28 = 0.5*B[0,1] + 0.5*B[1,1] + 0.5*B[2,1] + -0.5j*B[3,1]
b29 = 0.5j*B[0,1] + 0.5j*B[0,2] + -0.5j*B[1,1] + -0.5j*B[1,2] + 0.5j*B[2,1] + 0.5j*B[2,2] + -0.5*B[3,1] + -0.5*B[3,2]
b30 = -0.5*B[0,0] + 0.5*B[0,3] + -0.5*B[1,0] + 0.5*B[1,3] + -0.5*B[2,0] + 0.5*B[2,3] + 0.5j*B[3,0] + -0.5j*B[3,3]
b31 = 0.5*B[0,0] + -0.5*B[0,2] + -0.5*B[1,0] + 0.5*B[1,2] + -0.5*B[2,1] + -0.5*B[2,3] + 0.5j*B[3,1] + 0.5j*B[3,3]
b32 = 0.5j*B[0,1] + -0.5j*B[1,1] + -0.5j*B[2,1] + 0.5*B[3,1]
b33 = -0.5*B[0,1] + -0.5*B[0,3] + 0.5*B[1,0] + -0.5*B[1,3] + -0.5*B[2,0] + 0.5*B[2,3] + -0.5j*B[3,1] + -0.5j*B[3,3]
b34 = 0.5j*B[0,0] + -0.5j*B[1,0] + 0.5j*B[2,1] + 0.5j*B[2,2] + 0.5j*B[2,3] + -0.5*B[3,1] + -0.5*B[3,2] + -0.5*B[3,3]
b35 = -0.5j*B[0,1] + -0.5j*B[0,2] + 0.5j*B[1,1] + 0.5j*B[1,2] + -0.5j*B[2,1] + -0.5j*B[2,2] + -0.5*B[3,1] + -0.5*B[3,2]
b36 = -0.5*B[0,1] + -0.5*B[0,2] + -0.5*B[0,3] + -0.5*B[1,1] + -0.5*B[1,2] + -0.5*B[1,3] + -0.5*B[2,1] + -0.5*B[2,2] + -0.5*B[2,3] + -0.5j*B[3,1] + -0.5j*B[3,2] + -0.5j*B[3,3]
b37 = 0.5j*B[0,1] + 0.5j*B[0,2] + 0.5j*B[0,3] + -0.5j*B[1,0] + 0.5j*B[1,2] + 0.5j*B[1,3] + -0.5j*B[2,0] + 0.5j*B[2,2] + 0.5j*B[2,3] + -0.5*B[3,1] + -0.5*B[3,2] + -0.5*B[3,3]
b38 = 0.5j*B[0,0] + -0.5j*B[1,0] + -0.5j*B[2,0] + -0.5*B[3,0]
b39 = -0.5j*B[0,0] + 0.5j*B[0,3] + 0.5j*B[1,1] + 0.5j*B[1,3] + 0.5j*B[2,1] + 0.5j*B[2,3] + -0.5*B[3,0] + 0.5*B[3,3]
b40 = 0.5j*B[0,1] + 0.5j*B[0,2] + 0.5j*B[1,1] + 0.5j*B[1,2] + -0.5j*B[2,1] + -0.5j*B[2,2] + 0.5*B[3,1] + 0.5*B[3,2]
b41 = 0.5*B[0,0] + -0.5*B[0,3] + 0.5*B[1,0] + -0.5*B[1,3] + -0.5*B[2,0] + 0.5*B[2,3] + 0.5j*B[3,0] + -0.5j*B[3,3]
b42 = 0.5j*B[0,0] + -0.5j*B[1,0] + 0.5j*B[2,0] + 0.5*B[3,0]
b43 = 0.5*B[0,0] + -0.5*B[0,2] + -0.5*B[0,3] + -0.5*B[1,1] + -0.5*B[1,2] + -0.5*B[1,3] + 0.5*B[2,1] + 0.5*B[2,2] + 0.5*B[2,3] + -0.5j*B[3,0] + 0.5j*B[3,2] + 0.5j*B[3,3]
b44 = -0.5j*B[0,0] + 0.5j*B[1,0] + -0.5j*B[2,0] + 0.5*B[3,0]
b45 = -0.5j*B[0,1] + -0.5j*B[0,2] + -0.5j*B[0,3] + 0.5j*B[1,1] + 0.5j*B[1,2] + 0.5j*B[1,3] + -0.5j*B[2,1] + -0.5j*B[2,2] + -0.5j*B[2,3] + 0.5*B[3,1] + 0.5*B[3,2] + 0.5*B[3,3]
b46 = -0.5*B[0,0] + 0.5*B[0,2] + 0.5*B[1,0] + -0.5*B[1,2] + 0.5*B[2,0] + -0.5*B[2,2] + 0.5j*B[3,0] + -0.5j*B[3,2]
b47 = 0.5*B[0,0] + 0.5*B[1,1] + 0.5*B[2,1] + 0.5j*B[3,0]

# Perform the 48 multiplications
m0 = a0 * b0
m1 = a1 * b1
m2 = a2 * b2
m3 = a3 * b3
m4 = a4 * b4
m5 = a5 * b5
m6 = a6 * b6
m7 = a7 * b7
m8 = a8 * b8
m9 = a9 * b9
m10 = a10 * b10
m11 = a11 * b11
m12 = a12 * b12
m13 = a13 * b13
m14 = a14 * b14
m15 = a15 * b15
m16 = a16 * b16
m17 = a17 * b17
m18 = a18 * b18
m19 = a19 * b19
m20 = a20 * b20
m21 = a21 * b21
m22 = a22 * b22
m23 = a23 * b23
m24 = a24 * b24
m25 = a25 * b25
m26 = a26 * b26
m27 = a27 * b27
m28 = a28 * b28
m29 = a29 * b29
m30 = a30 * b30
m31 = a31 * b31
m32 = a32 * b32
m33 = a33 * b33
m34 = a34 * b34
m35 = a35 * b35
m36 = a36 * b36
m37 = a37 * b37
m38 = a38 * b38
m39 = a39 * b39
m40 = a40 * b40
m41 = a41 * b41
m42 = a42 * b42
m43 = a43 * b43
m44 = a44 * b44
m45 = a45 * b45
m46 = a46 * b46
m47 = a47 * b47

# Construct the result matrix
C[0,0] = 0.5j*m0 + -0.5j*m1 + -0.5*m5 + 0.5*m8 + 0.5j*m9 + (-0.5+0.5j)*m11 + 0.5*m14 + -0.5j*m15 + (-0.5+-0.5j)*m16 + 0.5j*m17 + (-0.5+-0.5j)*m18 + -0.5j*m24 + 0.5j*m26 + 0.5j*m27 + 0.5*m28 + 0.5j*m30 + -0.5j*m32 + 0.5*m34 + 0.5*m36 + -0.5j*m37 + -0.5*m38 + (0.5+-0.5j)*m39 + -0.5j*m40 + -0.5*m42 + -0.5*m43 + -0.5*m44 + -0.5j*m46 + 0.5*m47
C[0,1] = -0.5j*m0 + 0.5*m2 + (-0.5+-0.5j)*m3 + 0.5*m5 + 0.5*m6 + -0.5*m8 + (0.5+-0.5j)*m11 + -0.5*m12 + 0.5j*m13 + 0.5j*m14 + 0.5j*m15 + -0.5j*m17 + (0.5+0.5j)*m18 + 0.5*m20 + -0.5*m22 + 0.5j*m24 + -0.5j*m27 + -0.5*m28 + -0.5j*m29 + 0.5j*m32 + (-0.5+-0.5j)*m33 + -0.5*m34 + -0.5*m37 + 0.5j*m40 + 0.5j*m41 + -0.5j*m43 + 0.5*m44 + -0.5j*m47
C[0,2] = -0.5*m2 + 0.5*m3 + -0.5*m5 + -0.5j*m8 + 0.5j*m11 + 0.5*m12 + -0.5j*m13 + -0.5j*m14 + -0.5j*m15 + -0.5*m16 + -0.5*m18 + 0.5j*m19 + -0.5*m20 + 0.5j*m21 + -0.5*m23 + -0.5j*m24 + -0.5*m25 + 0.5j*m26 + 0.5*m27 + 0.5j*m30 + -0.5*m31 + -0.5j*m32 + 0.5*m33 + 0.5*m34 + 0.5j*m35 + 0.5*m36 + -0.5j*m37 + -0.5*m38 + -0.5j*m39 + 0.5j*m43 + -0.5*m44 + 0.5*m47
C[0,3] = 0.5j*m0 + -0.5j*m1 + 0.5j*m3 + -0.5j*m4 + -0.5*m6 + 0.5*m7 + 0.5*m8 + 0.5j*m9 + -0.5*m10 + -0.5*m11 + 0.5*m14 + -0.5j*m16 + 0.5j*m17 + -0.5j*m18 + -0.5*m21 + 0.5*m22 + 0.5*m24 + 0.5j*m27 + 0.5*m28 + 0.5j*m29 + -0.5j*m31 + 0.5j*m33 + 0.5j*m34 + 0.5*m37 + 0.5*m39 + -0.5j*m40 + -0.5j*m41 + -0.5*m42 + -0.5*m43 + -0.5j*m45 + -0.5j*m46 + 0.5j*m47
C[1,0] = -0.5*m0 + -0.5*m1 + -0.5*m5 + -0.5j*m8 + -0.5j*m9 + (0.5+-0.5j)*m11 + -0.5j*m14 + 0.5j*m15 + (-0.5+0.5j)*m16 + 0.5j*m17 + (-0.5+-0.5j)*m18 + -0.5*m24 + 0.5*m26 + -0.5*m27 + -0.5j*m28 + 0.5*m30 + -0.5*m32 + 0.5j*m34 + 0.5*m36 + -0.5*m37 + -0.5*m38 + (-0.5+-0.5j)*m39 + 0.5j*m40 + 0.5*m42 + 0.5j*m43 + -0.5j*m44 + -0.5*m46 + -0.5j*m47
C[1,1] = 0.5*m0 + -0.5*m2 + (0.5+-0.5j)*m3 + 0.5*m5 + 0.5*m6 + 0.5j*m8 + (-0.5+0.5j)*m11 + 0.5*m12 + -0.5*m13 + -0.5*m14 + -0.5j*m15 + -0.5j*m17 + (0.5+0.5j)*m18 + 0.5j*m20 + -0.5*m22 + 0.5*m24 + 0.5*m27 + 0.5j*m28 + 0.5*m29 + 0.5*m32 + (0.5+-0.5j)*m33 + -0.5j*m34 + -0.5j*m37 + -0.5j*m40 + -0.5*m41 + 0.5*m43 + 0.5j*m44 + 0.5*m47
C[1,2] = 0.5*m2 + -0.5*m3 + -0.5*m5 + -0.5*m8 + -0.5j*m11 + -0.5*m12 + 0.5*m13 + 0.5*m14 + 0.5j*m15 + -0.5*m16 + -0.5*m18 + 0.5j*m19 + -0.5j*m20 + -0.5j*m21 + 0.5j*m23 + -0.5*m24 + -0.5j*m25 + 0.5*m26 + 0.5j*m27 + 0.5*m30 + -0.5*m31 + -0.5*m32 + -0.5*m33 + 0.5j*m34 + -0.5j*m35 + 0.5*m36 + -0.5*m37 + -0.5*m38 + -0.5j*m39 + -0.5*m43 + -0.5j*m44 + -0.5j*m47
C[1,3] = -0.5*m0 + -0.5*m1 + 0.5j*m3 + -0.5*m4 + -0.5*m6 + -0.5*m7 + -0.5j*m8 + -0.5j*m9 + -0.5*m10 + 0.5*m11 + -0.5j*m14 + 0.5j*m16 + 0.5j*m17 + -0.5j*m18 + 0.5*m21 + 0.5*m22 + -0.5j*m24 + -0.5*m27 + -0.5j*m28 + -0.5*m29 + -0.5j*m31 + 0.5j*m33 + -0.5*m34 + 0.5j*m37 + -0.5*m39 + 0.5j*m40 + 0.5*m41 + 0.5*m42 + 0.5j*m43 + 0.5*m45 + -0.5*m46 + -0.5*m47
C[2,0] = -0.5j*m0 + 0.5j*m1 + 0.5j*m5 + -0.5j*m8 + 0.5*m9 + (0.5+0.5j)*m11 + 0.5j*m14 + -0.5*m15 + (-0.5+-0.5j)*m16 + 0.5*m17 + (-0.5+0.5j)*m18 + -0.5*m24 + 0.5j*m26 + 0.5*m27 + -0.5*m28 + -0.5j*m30 + -0.5j*m32 + -0.5j*m34 + -0.5j*m36 + -0.5*m37 + -0.5j*m38 + (-0.5+0.5j)*m39 + -0.5*m40 + -0.5j*m42 + 0.5j*m43 + -0.5*m44 + -0.5j*m46 + 0.5j*m47
C[2,1] = 0.5j*m0 + 0.5j*m2 + (-0.5+-0.5j)*m3 + -0.5j*m5 + 0.5j*m6 + 0.5j*m8 + (-0.5+-0.5j)*m11 + 0.5j*m12 + 0.5j*m13 + -0.5*m14 + 0.5*m15 + -0.5*m17 + (0.5+-0.5j)*m18 + -0.5*m20 + 0.5j*m22 + 0.5*m24 + -0.5*m27 + 0.5*m28 + -0.5j*m29 + 0.5j*m32 + (0.5+0.5j)*m33 + 0.5j*m34 + 0.5j*m37 + 0.5*m40 + -0.5j*m41 + -0.5*m43 + 0.5*m44 + 0.5*m47
C[2,2] = -0.5j*m2 + 0.5*m3 + 0.5j*m5 + 0.5*m8 + 0.5j*m11 + -0.5j*m12 + -0.5j*m13 + 0.5*m14 + -0.5*m15 + -0.5*m16 + -0.5*m18 + -0.5*m19 + 0.5*m20 + -0.5j*m21 + 0.5*m23 + -0.5*m24 + 0.5*m25 + 0.5j*m26 + 0.5j*m27 + -0.5j*m30 + 0.5*m31 + -0.5j*m32 + -0.5*m33 + -0.5j*m34 + -0.5*m35 + -0.5j*m36 + -0.5*m37 + -0.5j*m38 + 0.5j*m39 + 0.5*m43 + -0.5*m44 + 0.5j*m47
C[2,3] = -0.5j*m0 + 0.5j*m1 + 0.5j*m3 + -0.5j*m4 + -0.5j*m6 + 0.5j*m7 + -0.5j*m8 + 0.5*m9 + -0.5j*m10 + 0.5*m11 + 0.5j*m14 + -0.5j*m16 + 0.5*m17 + 0.5j*m18 + -0.5*m21 + -0.5j*m22 + 0.5j*m24 + 0.5*m27 + -0.5*m28 + 0.5j*m29 + -0.5j*m31 + -0.5j*m33 + -0.5*m34 + -0.5j*m37 + -0.5*m39 + -0.5*m40 + 0.5j*m41 + -0.5j*m42 + 0.5j*m43 + -0.5j*m45 + -0.5j*m46 + -0.5*m47
C[3,0] = -0.5j*m0 + -0.5j*m1 + 0.5*m5 + 0.5j*m8 + 0.5j*m9 + (-0.5+0.5j)*m11 + -0.5j*m14 + -0.5j*m15 + (0.5+0.5j)*m16 + -0.5j*m17 + (0.5+0.5j)*m18 + 0.5*m24 + -0.5j*m26 + 0.5*m27 + 0.5*m28 + 0.5j*m30 + 0.5j*m32 + -0.5j*m34 + -0.5*m36 + 0.5*m37 + -0.5*m38 + (0.5+-0.5j)*m39 + -0.5j*m40 + 0.5*m42 + -0.5j*m43 + -0.5*m44 + 0.5j*m46 + -0.5j*m47
C[3,1] = 0.5j*m0 + -0.5*m2 + (-0.5+-0.5j)*m3 + -0.5*m5 + 0.5*m6 + -0.5j*m8 + (0.5+-0.5j)*m11 + -0.5*m12 + 0.5j*m13 + -0.5*m14 + 0.5j*m15 + 0.5j*m17 + (-0.5+-0.5j)*m18 + -0.5*m20 + 0.5*m22 + -0.5*m24 + -0.5*m27 + -0.5*m28 + -0.5j*m29 + -0.5j*m32 + (0.5+0.5j)*m33 + 0.5j*m34 + 0.5j*m37 + 0.5j*m40 + -0.5j*m41 + -0.5*m43 + 0.5*m44 + 0.5*m47
C[3,2] = 0.5*m2 + 0.5j*m3 + 0.5*m5 + -0.5*m8 + -0.5*m11 + 0.5*m12 + -0.5j*m13 + 0.5*m14 + -0.5j*m15 + 0.5j*m16 + 0.5j*m18 + 0.5j*m19 + 0.5*m20 + 0.5*m21 + -0.5*m23 + 0.5*m24 + 0.5*m25 + -0.5j*m26 + 0.5j*m27 + 0.5j*m30 + -0.5j*m31 + 0.5j*m32 + -0.5j*m33 + -0.5j*m34 + -0.5j*m35 + -0.5*m36 + 0.5*m37 + -0.5*m38 + 0.5*m39 + 0.5*m43 + -0.5*m44 + -0.5j*m47
C[3,3] = -0.5j*m0 + -0.5j*m1 + 0.5*m3 + 0.5j*m4 + -0.5*m6 + -0.5*m7 + 0.5j*m8 + 0.5j*m9 + -0.5*m10 + 0.5j*m11 + -0.5j*m14 + 0.5*m16 + -0.5j*m17 + 0.5*m18 + -0.5j*m21 + -0.5*m22 + -0.5j*m24 + 0.5*m27 + 0.5*m28 + 0.5j*m29 + -0.5*m31 + -0.5*m33 + -0.5*m34 + -0.5j*m37 + -0.5j*m39 + -0.5j*m40 + 0.5j*m41 + 0.5*m42 + -0.5j*m43 + -0.5j*m45 + 0.5j*m46 + -0.5*m47
'''

import re
# # A[i,j] -> (A i j)
# data = re.sub(r'A\[(\d+),(\d+)\]', r'(A \1 \2)', data)

# # B[i,j] -> (B i j)
# data = re.sub(r'B\[(\d+),(\d+)\]', r'(B \1 \2)', data)

for i in range(4):
    for j in range(4):
        data = data.replace(f'A[{i},{j}]', f'(A {i} {j})')
        data = data.replace(f'B[{i},{j}]', f'(B {i} {j})')
        data = data.replace(f'C[{i},{j}]', f'C{i}{j}')

data = data.replace('0.5j', '0.5*Complex.I').replace('#', '--')

data = data.split('\n')
for i in range(len(data)):
  line = data[i]
  if ' = ' in line:
    line = 'let ' + line.replace(' = ', ' := ')
  line = '  ' + line
  data[i] = line
data.append('  !![C00, C01, C02, C03; C10, C11, C12, C13; C20, C21, C22, C23; C30, C31, C32, C33]')
data.insert(0, 'def matmul4x4 (A B : Matrix (Fin 4) (Fin 4) ℂ) : Matrix (Fin 4) (Fin 4) ℂ :=')
data = '\n'.join(data)

print(data)


# copy to clipboard
import pyperclip
pyperclip.copy(data)
