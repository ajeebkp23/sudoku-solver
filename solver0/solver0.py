from devtools import pprint

# from input0 import inputs

# pprint(inputs)
# outputs = inputs.copy()

# 1. Take filled counts of boxes of 3x3
def get_filled_counts(input_modified):
    filled_positions = []
    for position, box3x3 in enumerate(input_modified):
        # print(postion)
        filled_count = len([item for item in box3x3 if item])
        max_filled_item = {}
        max_filled_item['position'] = position
        max_filled_item['filled_count'] = filled_count
        filled_positions.append(max_filled_item)

    # 1.1 Sorted
    def sort_function(element):
        return element['filled_count']

    filled_positions.sort(key=sort_function, reverse=True)
    return filled_positions
# pprint(filled_positions)
    
def solve(puzzle):
    outputs = puzzle.copy()
    for i in range(100):
        inputs2 = outputs.copy()
        filled_positions = get_filled_counts(inputs2)
        # 2. Find what not in box3x3 and is in range(1,9+1)
        for filled in filled_positions:
            position = filled['position']
            filled_count = filled['filled_count']
            current_box = outputs[position]
            not_filled_in_box = set(range(1,9+1)) - set(current_box)
            filled['not_filled_in_box'] = not_filled_in_box

        # 3. Find what is not in Same Row items & same column items
        same_row_column_dict = {
            'row': {},
            'column': {}
        }
        def get_same_columns(position):
            existing_column = same_row_column_dict['column'].get(position)
            if existing_column:
                return existing_column
            else:
                computed = sorted([(position+col_index*3)%9 for col_index in range(3)])
                same_row_column_dict['column'][position] = computed
                return computed

        def get_same_rows(position):
            existing_row = same_row_column_dict['row'].get(position)
            if existing_row:
                return existing_row
            else:
                position_div_3 = int(position / 3)
                computed  = sorted(range(position_div_3*3,(position_div_3+1)*3))
                same_row_column_dict['row'][position] = computed
                return computed

        for filled in filled_positions:
            position = filled['position']
            filled_count = filled['filled_count']
            not_filled_in_box = filled['not_filled_in_box']
            current_box = outputs[position]
            # print('current_box: ',current_box)
            current_box_modified =current_box.copy() 
            for index, item in enumerate(current_box):
                # print(index,item,'>'*30)
                if not item:
                    # print('Item: ',item,' Index: ',index, ' position:  ',position)
                    box_column_positions = get_same_columns(position)
                    box_row_positions = get_same_rows(position)
                    item_column_postions = get_same_columns(index)
                    item_row_positions = get_same_rows(index)

                    column_items = []
                    for box_pos in box_column_positions:
                        inner_box = outputs[box_pos]
                        for item_pos in item_column_postions:
                            inner_item = inner_box[item_pos]
                            if inner_item:
                                column_items.append(inner_item)
                    # print('column_items: ',column_items)

                    row_items = []
                    for box_pos in box_row_positions:
                        inner_box = outputs[box_pos]
                        # print('inner_box: ',inner_box, 'item_row_positions: ',item_row_positions)
                        for item_pos in item_row_positions:
                            inner_item = inner_box[item_pos]
                            if inner_item:
                                # print('Inner Item: ',inner_item)
                                row_items.append(inner_item)
                    # print('row_items: ',row_items)

                    # 4. If single element common in 2 and 3 then fill it.
                    new_item = set(not_filled_in_box) - set(column_items + row_items)
                    if(len(new_item) == 1):
                        outputs[position][index] = list(new_item)[0]
                    # print('new_item: ',new_item)
                else:
                    continue
                # print(position, same_row_positions)

        # print(filled_positions)
        print('Done')

    return outputs
    # for i in outputs:
    #     print(i)
    #     print(i[0:3])
    #     print(i[3:6])
    #     print(i[6:9])
        # 5. Loop the things until finish.

# from input0 import inputs
# solve(inputs)