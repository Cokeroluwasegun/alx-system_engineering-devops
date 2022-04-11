#!/usr/bin/python3
""" Script that gathers to do data from an api """


if __name__=="__main__":
    import requests
    from sys import argv

    link = "https://jsonplaceholder.typicode.com/users"
    uid = argv[1]
    request_info = requests.get("{}/{}".format(link, uid)).json()
    if request_info.status_code == 200:
        emp_name = request_info['name']
        todo_content = requests.get("{}/{}/todos".format(link, uid)).json()
        done = list()
        for todo in todo_content:
            if todo['completed'] is True:
                done.append(todo['title'])
        total = len(todo_content)
        total_done = len(done)
        string = "Employee {} is done with task({}/{}):".format(emp_name,
                                                            total_done,
                                                            total)
        print(string)
        for task in done:
            print("\t", task)
