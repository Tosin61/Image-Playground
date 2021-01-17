def red_stripes(image_matrix):
    matrix = []
    c=0
    for row in range(len(image_matrix)):
        arr1 = []
        for column in range(len(image_matrix[row])):
            arr = list(image_matrix[row][column])
            if c>=50 and c<=100:
                if c == 100:
                    c = 0
                arr = tuple(arr)
                arr1.append(arr)
            else:
                arr[0] = 255
                arr = tuple(arr)
                arr1.append(arr)
        c+=1
        matrix.append(arr1)
    return matrix

def grayscale(image_matrix):
    matrix = []
    for row in range(len(image_matrix)):
        add=0
        arr1 = []
        for column in range(len(image_matrix[row])):
            arr = list(image_matrix[row][column])
            add = arr[0]+arr[1]+arr[2]
            split_up = add//3
            arr[0] = split_up 
            arr[1] = split_up 
            arr[2] = split_up 
            arr = tuple(arr)
            arr1.append(arr)
        matrix.append(arr1)
    return matrix
            
def invert_colors(image_matrix):
    matrix = []
    for row in range(len(image_matrix)):
        arr1 = []
        for column in range(len(image_matrix[row])):
            arr = list(image_matrix[row][column])
            diff = 255-arr[0]
            diff1 = 255-arr[1]
            diff2 = 255 - arr[2]
            arr[0] = diff
            arr[1] = diff1
            arr[2] = diff2
            arr = tuple(arr)
            arr1.append(arr)
        matrix.append(arr1)
    return matrix

def flip(image_matrix):
    image_matrix.reverse()
    return(image_matrix)

def blur(image_matrix):
    matrix = []
    for row in range(len(image_matrix)):
        karr = []
        for column in range(len(image_matrix[row])):
            
            if row == 0 and column == 0:
                arr=list(image_matrix[row][column])
                arr0=list(image_matrix[row][column+1])
                arr1=list(image_matrix[row+1][column+1])
                arr2=list(image_matrix[row+1][column])
                red = (arr[0] + arr0[0] + arr1[0] + arr2[0])//4
                green = (arr[1] + arr0[1] + arr1[1] + arr2[1])//4
                blue = (arr[2] + arr0[2] + arr1[2] + arr2[2])//4

            elif row == 0 and column+1 == len(image_matrix[row]):
                arr=list(image_matrix[row][column])
                arr0=list(image_matrix[row][column-1])
                arr1=list(image_matrix[row+1][column-1])
                arr2=list(image_matrix[row+1][column])
                red = (arr[0] + arr0[0] + arr1[0] + arr2[0])//4
                green = (arr[1] + arr0[1] + arr1[1] + arr2[1])//4
                blue = (arr[2] + arr0[2] + arr1[2] + arr2[2])//4

            elif row+1 ==len(image_matrix) and column == 0:
                arr=list(image_matrix[row][column])
                arr0=list(image_matrix[row][column+1])
                arr1=list(image_matrix[row-1][column+1])
                arr2=list(image_matrix[row-1][column])
                red = (arr[0] + arr0[0] + arr1[0] + arr2[0])//4
                green = (arr[1] + arr0[1] + arr1[1] + arr2[1])//4
                blue = (arr[2] + arr0[2] + arr1[2] + arr2[2])//4


            elif row+1 == len(image_matrix) and column+1 == len(image_matrix[row]):
                arr=list(image_matrix[row][column])
                arr0=list(image_matrix[row][column-1])
                arr1=list(image_matrix[row-1][column-1])
                arr2=list(image_matrix[row-1][column])
                red = (arr[0] + arr0[0] + arr1[0] + arr2[0])//4
                green = (arr[1] + arr0[1] + arr1[1] + arr2[1])//4
                blue = (arr[2] + arr0[2] + arr1[2] + arr2[2])//4

                
            elif row+1 == len(image_matrix):
                arr=list(image_matrix[row][column])
                arr0=list(image_matrix[row-1][column])
                arr1=list(image_matrix[row-1][column-1])
                arr2=list(image_matrix[row-1][column+1])
                arr3=list(image_matrix[row][column+1])
                arr4=list(image_matrix[row][column-1])
                red = (arr[0] + arr0[0] + arr1[0] + arr2[0] + arr3[0] + arr4[0])//6
                green = (arr[1] + arr0[1] + arr1[1] + arr2[1] + arr3[1] + arr4[1])//6 
                blue = (arr[2] + arr0[2] + arr1[2] + arr2[2] + arr3[2] + arr4[2])//6
                
            elif column+1 == len(image_matrix[row]):
                arr=list(image_matrix[row][column])
                arr0=list(image_matrix[row-1][column])
                arr1=list(image_matrix[row-1][column-1])
                arr2=list(image_matrix[row][column-1])
                arr3=list(image_matrix[row+1][column-1])
                arr4=list(image_matrix[row+1][column])
                red = (arr[0] + arr0[0] + arr1[0] + arr2[0] + arr3[0] + arr4[0])//6
                green = (arr[1] + arr0[1] + arr1[1] + arr2[1] + arr3[1] + arr4[1])//6 
                blue = (arr[2] + arr0[2] + arr1[2] + arr2[2] + arr3[2] + arr4[2])//6
                
            elif row == 0:
                arr=list(image_matrix[row][column])
                arr0=list(image_matrix[row+1][column])
                arr1=list(image_matrix[row+1][column-1])
                arr2=list(image_matrix[row+1][column+1])
                arr3=list(image_matrix[row][column+1])
                arr4=list(image_matrix[row][column-1])
                red = (arr[0] + arr0[0] + arr1[0] + arr2[0] + arr3[0] + arr4[0])//6
                green = (arr[1] + arr0[1] + arr1[1] + arr2[1] + arr3[1] + arr4[1])//6 
                blue = (arr[2] + arr0[2] + arr1[2] + arr2[2] + arr3[2] + arr4[2])//6
            elif column == 0:
                arr=list(image_matrix[row][column])
                arr0=list(image_matrix[row-1][column])
                arr1=list(image_matrix[row-1][column+1])
                arr2=list(image_matrix[row][column+1])
                arr3=list(image_matrix[row+1][column+1])
                arr4=list(image_matrix[row+1][column])
                red = (arr[0] + arr0[0] + arr1[0] + arr2[0] + arr3[0] + arr4[0])//6
                green = (arr[1] + arr0[1] + arr1[1] + arr2[1] + arr3[1] + arr4[1])//6 
                blue = (arr[2] + arr0[2] + arr1[2] + arr2[2] + arr3[2] + arr4[2])//6
                
            else:
                arr=list(image_matrix[row][column])
                arr0=list(image_matrix[row][column+1])
                arr1=list(image_matrix[row+1][column])
                arr2=list(image_matrix[row+1][column+1])
                arr3=list(image_matrix[row-1][column-1])
                arr4=list(image_matrix[row-1][column])
                arr5=list(image_matrix[row][column-1])
                arr6=list(image_matrix[row-1][column+1])
                arr7=list(image_matrix[row+1][column-1])
                red = (arr[0]+ arr0[0] + arr1[0] + arr2[0] + arr3[0] + arr4[0] + arr5[0] + arr6[0] + arr7[0])//9
                green = (arr[1]+ arr0[1] + arr1[1] + arr2[1] + arr3[1] + arr4[1] + arr5[1] + arr6[1] + arr7[1])//9

                blue = (arr[2]+ arr0[2] + arr1[2] + arr2[2] + arr3[2] + arr4[2] + arr5[2] + arr6[2] + arr7[2])//9
            tup=(red,green,blue)
            karr.append(tup)
        matrix.append(karr)
    return matrix
                
def sepia(image_matrix):
    matrix = []
    for row in range(len(image_matrix)):
        arr1 = []
        for column in range(len(image_matrix[row])):
            arr=list(image_matrix[row][column])
            red = (arr[0]*.393)+(arr[1]*.769)+(arr[2]*.189)
            red = int(red)
            green = (arr[0]*.349)+(arr[1]*.686)+(arr[2]*.168)
            green = int(green)
            blue = (arr[0]*.272)+(arr[1]*.534)+(arr[2]*.131)
            blue = int(blue)
            if red > 255:
                red = 255
            if blue > 255:
                blue = 255
            if green > 255:
                green = 255
            arr[0] = red
            arr[1] = green
            arr[2] = blue
            arr=tuple(arr)
            arr1.append(arr)
        matrix.append(arr1)
    return(matrix)

def threshold(image_matrix, 
              red_threshold=(0, 255), 
              green_threshold=(0, 255),
              blue_threshold=(0, 255)):
                  matrix = []
                  for row in range(len(image_matrix)):
                      arr1 = []
                      for column in range(len(image_matrix[row])):
                          arr=list(image_matrix[row][column])
                          if arr[0] > red_threshold[1] or arr[0] < red_threshold[0]:
                              arr[0] = 0
                              arr[1] = 0
                              arr[2] = 0
                          if arr[1] > green_threshold[1] or arr[1] < green_threshold[0]:
                              arr[0] = 0
                              arr[1] = 0
                              arr[2] = 0
                          if arr[2] > blue_threshold[1] or arr[2] < blue_threshold[0]:
                              arr[0]=0
                              arr[1]=0
                              arr[2]=0
                          arr = tuple(arr)
                          arr1.append(arr)
                      matrix.append(arr1)
                  return(matrix)
                  