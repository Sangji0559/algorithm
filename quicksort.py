import pandas as pd

wb = pd.read_excel('./input_quick_sort.xlsx', index_col=0,header=None,dtype={'values':int})
wb_list = list(wb.index.values)

print(wb_list)

def QuickSort(wb_list, start, end):
  if(start>=end): return
  pivot = start
  left = start+1
  right = end
  while(left <= right):
    while(left <= end and wb_list[left]<=wb_list[pivot]):
      left += 1
    while(right > start and wb_list[right]>=wb_list[pivot]):
      right -= 1
    if(left>right): wb_list[right],wb_list[pivot] = wb_list[pivot],wb_list[right]
    else :
      wb_list[left],wb_list[right] = wb_list[right],wb_list[left]
  QuickSort(wb_list,start,right-1)
  QuickSort(wb_list,right+1,end)

QuickSort(wb_list,0,len(wb_list)-1)
print(wb_list)
