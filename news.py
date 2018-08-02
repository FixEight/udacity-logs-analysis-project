#!/usr/bin/env python2

import psycopg2


# Create dictionary variables to store questions and thier answers
data_one = {}
data_one["question"] = """
    \n1. What are the most popular three articles of all time?"""
data_two = {}
data_two["question"] = """
    \n2. Who are the most popular article authors of all time?"""
data_three = {}
data_three["question"] = """
    \n3. On which days did more than 1%s of requests lead to errors?"""

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


def run_query(user_query):
    """Return the result of the given query."""
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute(user_query)
    result = c.fetchall()
    db.close()
    return result


def print_result(result_query):
    """Print the quesions and their related answer."""
    print (result_query["question"])
    for result in result_query["answer"]:
        print ("\t" + result[0] + " ___ " + str(result[1]) + " views")


def print_result_special(result_query):
    """Print the quesion number three which shows the error detail."""
    print (result_query["question"])
    for result in result_query["answer"]:
        print ("\t" + str(result[0]) + " ___ " + str(result[1]) + "% errors")

# Save the quries result
data_one["answer"] = run_query(answer_one)
data_two["answer"] = run_query(answer_two)
data_three["answer"] = run_query(answer_three)


# Print the output in given format
print_result(data_one)
print_result(data_two)
print_result_special(data_three)
print ("\n")
