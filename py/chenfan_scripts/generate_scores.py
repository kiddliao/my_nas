import os
import random

input_path = r'py\chenfan_scripts\source_file\2_month.txt'
output_path = input_path.replace('.txt', '_processed.txt')
num_limit = [14, 4]
delta = [35]

with open(input_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()




res = {}
mid_res = []
for line in lines:
    id, stu_name, score = line.strip().split('\t')
    mid_res.append([id, stu_name, int(score.split('%')[0])])
    res[f'{id}-__-{stu_name}'] = []



def process_3(mid_res, month_id, month_name):
    change_name = set()
    print(f'-------成绩修改中-------')
    first_dict = {}
    second_dict = {}
    third_dict = {}
    for v in mid_res:
        id, stu_name, score = v
        if score >= 100:
            first_dict[f'{id}-__-{stu_name}'] = score
        elif 100 > score >= 80:
            second_dict[f'{id}-__-{stu_name}'] = score
        else:
            third_dict[f'{id}-__-{stu_name}'] = score
    
    while len(first_dict) < num_limit[0]:
        second_dict_key = list(second_dict.keys())
        rid = random.randint(0, len(second_dict) - 1)
        pop_name = second_dict_key[rid]
        if pop_name in change_name:
            continue
        pop_score = second_dict[pop_name]
        
        new_pop_score = random.randint(100, 150)
        if abs(new_pop_score - pop_score) > delta[0]:
            continue
        id, name = pop_name.split('-__-')
        print(f'第一梯队人数为{len(first_dict)},少于标准{num_limit[0]},将序号为{id}的{name}同学成绩由{pop_score}改为{new_pop_score},现有第一梯队人数为{len(first_dict) + 1}')
        second_dict.pop(pop_name)
        first_dict[pop_name] = new_pop_score
        change_name.add(pop_name)

    # while len(first_dict) > num_limit[0]:
    #     first_dict_key = list(first_dict.keys())
    #     rid = random.randint(0, len(first_dict) - 1)
    #     pop_name = first_dict_key[rid]
    #     if pop_name in change_name:
    #         continue
    #     pop_score = first_dict[pop_name]
        
    #     new_pop_score = random.randint(80, 99)
    #     if abs(new_pop_score - pop_score) > delta[0]:
    #         continue
    #     id, name = pop_name.split('-__-')
    #     print(f'第一梯队人数为{len(first_dict)},多于标准{num_limit[0]},将序号为{id}的{name}同学成绩由{pop_score}改为{new_pop_score},现有第一梯队人数为{len(first_dict) - 1}')
    #     first_dict.pop(pop_name)
    #     second_dict[pop_name] = new_pop_score
    #     change_name.add(pop_name)

    while len(second_dict) < num_limit[1]:
        third_dict_key = list(third_dict.keys())
        rid = random.randint(0, len(third_dict) - 1)
        pop_name = third_dict_key[rid]
        if pop_name in change_name:
            continue
        pop_score = third_dict[pop_name]
        
        new_pop_score = random.randint(80, 99)
        if abs(new_pop_score - pop_score) > delta[0]:
            continue
        id, name = pop_name.split('-__-')
        print(f'第二梯队人数为{len(second_dict)},少于标准{num_limit[1]},将序号为{id}的{name}同学成绩由{pop_score}改为{new_pop_score},现有第二梯队人数为{len(second_dict) + 1}')
        third_dict.pop(pop_name)
        second_dict[pop_name] = new_pop_score
        change_name.add(pop_name)

    # while len(second_dict) > num_limit[1]:
    #     second_dict_key = list(second_dict.keys())
    #     rid = random.randint(0, len(second_dict) - 1)
    #     pop_name = second_dict_key[rid]
    #     if pop_name in change_name:
    #         continue
    #     pop_score = second_dict[pop_name]
        
    #     new_pop_score = random.randint(13, 79)
    #     if abs(new_pop_score - pop_score) > delta[0]:
    #         continue
    #     id, name = pop_name.split('-__-')
    #     print(f'第二梯队人数为{len(second_dict)},多于标准{num_limit[1]},将序号为{id}的{name}同学成绩由{pop_score}改为{new_pop_score},现有第二梯队人数为{len(second_dict) - 1}')
    #     second_dict.pop(pop_name)
    #     third_dict[pop_name] = new_pop_score
    #     change_name.add(pop_name)

    for k, v in {**first_dict, **second_dict, **third_dict}.items():
        res[k].append(v)

    print(f'-------成绩修改结束-------')


def process_2(mid_res):
    change_name = set()
    print(f'-------成绩修改中-------')
    first_dict = {}
    second_dict = {}
    for v in mid_res:
        id, stu_name, score = v
        if score >= 80:
            first_dict[f'{id}-__-{stu_name}'] = score
        else:
            second_dict[f'{id}-__-{stu_name}'] = score

    while len(first_dict) < num_limit[0]:
        tmp_list = sorted(list(second_dict.items()),
                          key=lambda x: (-x[1], int(x[0].split('-__-')[0])))
        pop_name = tmp_list[0][0]
        if pop_name in change_name:
            continue
        pop_score = second_dict[pop_name]
        
        new_pop_score = random.randint(80, 80)
        if abs(new_pop_score - pop_score) > delta[0]:
            continue
        id, name = pop_name.split('-__-')
        print(
            f'第一梯队人数为{len(first_dict)},少于标准{num_limit[0]},将序号为{id}的{name}同学成绩由{pop_score}改为{new_pop_score},现有第一梯队人数为{len(first_dict) + 1}')
        second_dict.pop(pop_name)
        first_dict[pop_name] = new_pop_score
        change_name.add(pop_name)

    # while len(first_dict) > num_limit[0]:
    #     first_dict_key = list(first_dict.keys())
    #     rid = random.randint(0, len(first_dict) - 1)
    #     pop_name = first_dict_key[rid]
    #     if pop_name in change_name:
    #         continue
    #     pop_score = first_dict[pop_name]
        
    #     new_pop_score = random.randint(13, 80)
    #     if abs(new_pop_score - pop_score) > delta[0]:
    #         continue
    #     id, name = pop_name.split('-__-')
    #     print(
    #         f'第一梯队人数为{len(first_dict)},多于标准{num_limit[0]},将序号为{id}的{name}同学成绩由{pop_score}改为{new_pop_score},现有第一梯队人数为{len(first_dict) - 1}')
    #     first_dict.pop(pop_name)
    #     second_dict[pop_name] = new_pop_score
    #     change_name.add(pop_name)


    for k, v in {**first_dict, **second_dict}.items():
        res[k].append(v)

    print(f'-------成绩修改结束-------')

if len(num_limit) == 2:
    process_2(mid_res)
if len(num_limit) == 3:
    process_3(mid_res)

with open(output_path, 'w', encoding='utf_8') as f:
    res = sorted(list(res.items()), key=lambda x: int(x[0].split('-__-')[0]))
    for v in res:
        id, name = v[0].split('-__-')
        score = v[1][0]
        score = f'{score}%'
        f.write(f'{id}\t{name}\t{score}\n')
