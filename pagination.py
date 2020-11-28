import math

current_page = 1


def choose_page():
    global current_page

    try:
        current_page = int(raw_input("choose page > "))
        paginate(100, 5, 8)
        choose_page()

    except ValueError:
        print ("\nvalue must be a number")
        choose_page()


def paginate(data_count, paginate_count, display_link_count, another_link_count=3):
    """
    display list paginate
    """

    global current_page

    total_page = int(math.ceil(data_count/paginate_count))


    diff = another_link_count + 1
    is_split = current_page - diff > another_link_count
    
    start = current_page - another_link_count
    end = start + another_link_count * 2

    is_elipsis = current_page - another_link_count <= total_page - display_link_count or not current_page < total_page - display_link_count
    elipsis_num = total_page - another_link_count
    
    if is_elipsis == False:
        start = total_page - display_link_count + 1
        end = total_page


    i = 0
    arr = []
    while i < total_page:
        if i == -1:
            if is_split == True:
                arr.append(str("..."))
                i = start
                for j in range(start, end+1):
                    arr.append(str(j))
                    i = i + 1
                    if i > total_page:
                        break

            else:
                for j in range(another_link_count, display_link_count+1):
                    arr.append(str(j))

            i = -2

        elif i == -2:
            i = end + 1 if (is_split == True and is_elipsis ==
                            False) else elipsis_num

            for j in range(i, total_page+1):
                o = i

                if i == elipsis_num and is_elipsis == True:
                    o = "..."

                arr.append(str(o))
                i = i + 1

        else:
            i = i + 1
            arr.append(str(i))

            if i == another_link_count:
                i = -1
            elif i > display_link_count:
                i = -2

    print "==============="
    print "links :"
    print " ".join(arr)
    print "\ntotal page" + " " + str(total_page)


if __name__ == "__main__":
    paginate(100, 5, 8)
    choose_page()
