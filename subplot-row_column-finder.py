import  math

image_number=10

#finding row & column for subplot from image number
subplot_column=int(math.sqrt(image_number))
remaining_row_in_float=(image_number-(subplot_column*subplot_column))/subplot_column
remaining_row= int(remaining_row_in_float)
if remaining_row_in_float-remaining_row !=0.00:
    remaining_row= remaining_row+1
subplot_row=subplot_column+remaining_row
