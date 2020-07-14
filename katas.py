def solution(args):
    # your code here
    string = ""
    first = True
    closed = False
    last_item = -1
    for counter, item in enumerate(args, 1):
        if not first:
            if last_item < item - 1:
                if not closed and last_added != item: 
                    # last_added != last_item:
                    string += '-' + str(last_item) + ','
                    closed = True
                else: 
                    string += ','
                    closed = True
                string += str(item)
                closed = False
                last_added = item
            if last_added != item and len(args) == counter:
                string += '-' + str(item)
            # two_before = last_item
            last_item = item
        elif first:
            string += str(item)
            last_added = item
            last_item = item
            first = False

    return string
