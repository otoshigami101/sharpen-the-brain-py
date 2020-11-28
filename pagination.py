import math

current_page = 1

data_count = 200
paginate_count = 5
display_link_count = 10
another_link_count = 3


def config():
    global data_count, paginate_count, display_link_count, another_link_count

    try:
        data_count = int(raw_input("data count (default: 200) > ") or 200)
        paginate_count = int(raw_input("paginate count (default: 5)> ") or 5)
        display_link_count = int(
            raw_input("display link (default: 10) > ") or 10)
        another_link_count = int(
            raw_input("display link (default: 3) > ") or 3)
        paginate()

    except ValueError:
        print ("\nvalue must be a number")
        config()


def choose_page():
    global current_page

    try:
        current_page = int(raw_input("choose page > "))
        paginate()
        choose_page()

    except ValueError:
        print ("\nvalue must be a number")
        choose_page()


def paginate():
    global current_page, data_count, paginate_count, display_link_count, another_link_count

    total_page = int(math.ceil(data_count/paginate_count))  # total of page

    min_num = another_link_count + 1  # different for split

    start = current_page - another_link_count  # start of num page in center
    end = start + another_link_count * 2  # end of num page in center

    is_elipsis_r = current_page - another_link_count <= total_page - \
        display_link_count  # elipsis condition in end

    count_r = total_page - another_link_count + \
        1  # start num after elipsis in end

    max_num = total_page - display_link_count
    # min start num in end if not elipsis

    is_split_l = current_page - min_num > another_link_count
    # is curr page - min_num bigger than another_link_count ?

    not_split_r = current_page - min_num > max_num
    # is curr page - min_num bigger than max_num ?

    # set elipsis false if not split is true
    if not_split_r == True:
        is_elipsis_r = False

    # reassign start, end value
    # if not end is not start with elipsis
    if is_elipsis_r == False:
        start = max_num + 1  # start of num in end
        end = total_page  # end of page

    i = 0
    arr = []
    while i < total_page:
        if i == -1:
            i = another_link_count + 1
            s = display_link_count + 1

            if is_split_l == True:
                i = start
                s = end + 1
                arr.append(str("..."))

            for j in range(i, s):
                arr.append(str(j))
                if j > total_page:
                    break

            i = -2

        elif i == -2:
            i = end + 1
            s = total_page+1

            if is_elipsis_r == True:
                i = count_r
                arr.append(str("..."))

            for j in range(i, s):
                arr.append(str(j))
                i = i + 1

        else:
            i = i + 1
            arr.append(str(i))

            if i == another_link_count:
                i = -1
            elif i == display_link_count:
                i = -2

    print "==============="
    print "pages :"
    print " ".join(arr)
    print "\ncurrent page :" + " " + str(current_page)
    print "total page" + " " + str(total_page)


if __name__ == "__main__":
    config()
    paginate()
    choose_page()
