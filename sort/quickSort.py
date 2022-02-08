# 다음 리스트를 리스트 슬라이싱(예 [:2])을 이용해서 세 개로 짤라서 각 리스트 변수에 넣고 출력해보기
# data_list = [1, 2, 3, 4, 5]
# lens = len(data_list)//2
# left = data_list[:lens]
# mid = data_list[lens:lens+1]
# right = data_list[lens+1:]
# print(left)
# print(mid)
# print(right)

# 다음 리스트를 맨 앞에 데이터를 기준으로 작은 데이터는 left 변수에, 그렇지 않은 데이터는 right 변수에 넣기<br>
# data_list = [4, 1, 2, 5, 7]
# pivot = data_list[0]
# left, right = [],[]
# for i in range(1,len(data_list)):
#     if pivot > data_list[i]:
#         left.append(data_list[i])
#     else:
#         right.append(data_list[i])
# print(right)
# print(left)

# ata_list 가 다음 세 데이터를 가지고 있을 때 리스트를 맨 앞에 데이터를 기준으로 작은 데이터는 left 변수에, 그렇지 않은 데이터는 right 변수에 넣고 left, right, pivot 변수 값을 사용해서 정렬된 데이터 출력해보기<

data_list = [4, 3, 2]
def quickSort(list):
    if len(list)<=1:
        return list
    pivot = list[0]
    left, right = [],[]
    left = [item for item in list[1:] if item < pivot]
    right = [item for item in list[1:] if item >= pivot]
    # for i in range(1,len(list)):
    #     if pivot > list[i]:
    #         left.append(list[i])
    #     else:
    #         right.append(list[i])
    return quickSort(left)+[pivot]+quickSort(right)

print(quickSort(data_list))
