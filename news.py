#!/usr/bin/env python2

import psycopg2


# Resultant queries according to the questions
answer_one = """
    select title, num from top_articles order by top_articles.num
    desc limit 3;"""
answer_two = """
    select authors.name, sum(num) as num from top_articles, authors
    group by top_articles.author, authors.id having
    authors.id=top_articles.author order by num desc;"""
answer_three = """
    select to_char(date,'Mon DD, YYYY'), percentage from error_percent
    where error_percent.percentage > 1.00;"""

# Global variable
count = 1


def run_query(user_query):
    """Return the result of the given query."""
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute(user_query)
    data = c.fetchall()
    global count
    if (count < 3):
        display(data)
        count = count + 1
    else:
        display_special(data)
    db.close()


def display(answers):
    """Display the first two answers"""
    for answer in answers:
        print ("\t %s ___ %s views" % (answer[0], answer[1]))


def display_special(special_answer):
    """Display the special answer"""
    for answer in special_answer:
        print ("\t %s ___ %s%% errors" % (answer[0], answer[1]))


# Run the program and get the formatted result
print ("\n1. What are the most popular three articles of all time?")
run_query(answer_one)
print ("\n2. Who are the most popular article authors of all time?")
run_query(answer_two)
print ("\n3. On which days did more than 1%s of requests lead to errors?")
run_query(answer_three)
print ("\n")
