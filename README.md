# Logs Analysis Project
## Project Overview
> This project describe that, how to explore a large database with over a million rows. In this you will stretch our SQL database skills and build complex queries and use them to draw business conclusions from data. You will also get interact with a live database both from the command line and from Python code.

## How to Run? :traffic_light:
### Pre Requirements!
* [Git 2.18.0](https://git-scm.com/) Version Control System
* [Python 2.7.12](https://www.python.org/downloads/windows/) High-Level Programming Language
* [Vagrant 2.1.2](https://www.vagrantup.com/) Build and Maintain Virtual Machine
* [VirtualBox 5.1.38](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) Execute the Virtual Machine

### Setup the Project:
1. Install Git.
2. Install Vagrant and VirtualBox.
3. Python and PostgreSQL are already pre-installed in VM.
2. Download or Clone [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository.
3. Download [Data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) from here of Newspaper Database.
4. You will need to unzip this file after downloading it. The file inside is called `newsdata.sql` and move this file inside **vagrant** sub-directory in the downloaded **fullstack-nanodegree-vm** repository.

### Start the Virtual Machine:
The VM is a Linux server system that runs on top of your own computer. You can share files easily between your compute. Launch the VM inside **vagrant** sub-directory in the downloaded **fullstack-nanodegree-vm** repository using command in terminal/Git Bash:
```
    $ vagrant up
```
log in VM using command in terminal/Git Bash:
```
    $ vagrant ssh
```
After log in VM, change directory `cd` to /vagrant and look around with `ls`. Then you will get Shell Prompt look like this:
```
    vagrant@vagrant:/vagrant$
```
### Setup the Database:
After successful login in VM. Load the data in local database using the command:
```
    $ psql -d news -f newsdata.sql
```
- `psql` — the PostgreSQL command line program
- `-d news` — connect to the database named news which has been set up for you
- `-f newsdata.sql` — run the SQL statements in the file **newsdata.sql**

Running this command will connect to your installed database server and execute the SQL commands in the downloaded file (`newsdata.sql`), creating tables and populating them with data.

Connect to the database using the command:
```
    $ psql news
```
### Create Views:
**Create View (top_articles) by using the command:**
```
$ create view top_articles as select articles.author,articles.title , view.num from articles
,(select path, count(*) as num from log group by path order by num desc limit 8 offset 1)
as view where (view.path like '%' || articles.slug || '%') order by num desc;
```
by `$ \d top_articles` using this command you will get the Shell Prompt look like this:

| Column | Type    |
| -------| ------- |
| author | integer |
| title  | text    |
| num    | bigint  |

**Create View (all_requests) by using the command:**
```
$ create view all_requests as select date(time), count(*) as num from log group by date(time);
```
by `$ \d all_requests` using this command you will get the Shell Prompt look like this:

| Column | Type   |
| -------| -------|
| date   | date   |
| num    | bigint |

**Create View (error_requests) by using the command:**
```
$ create view error_requests as select date(time), count(*) as num from log where status !=
'200 OK' group by date(time);
```
by `$ \d error_requests` using this command you will get the Shell Prompt look like this:

| Column | Type   |
| -------| -------|
| date   | date   |
| num    | bigint |

**Create View (error_percent) by using the command:**
```
$ create view error_percent as select round(e.num * 100.0 / a.num, 3) as percentage, e.date
from error_requests as e, all_requests as a where e.date = a.date;
```
by `$ \d error_percent` using this command you will get the Shell Prompt look like this:

|   Column   |  Type   |
|  --------  | --------|
| percentage | numeric |
| date       | date    |

## Run the Project: :rocket:
Close the `psql` database by pressing `Ctrl + d`. After closing, inside **vagrant** sub-directory run the `news.py` file using the command:
```
    $ python news.py
```

## Expected Output in VM terminal: :camel:
```
1. What are the most popular three articles of all time?
        Candidate is jerk, alleges rival ___ 338647 views
        Bears love berries, alleges bear ___ 253801 views
        Bad things gone, say good people ___ 170098 views


2. Who are the most popular article authors of all time?
        Ursula La Multa ___ 507594 views
        Rudolf von Treppenwitz ___ 423457 views
        Anonymous Contributor ___ 170098 views
        Markoff Chaney ___ 84557 views


3. On which days did more than 1%s of requests lead to errors?
        Jul 17, 2016 ___ 2.263% errors
```

## License
Log Analysis Project is Copyright :copyright: 2018 Kashif Iqbal. It is free, and may be redistributed under the terms specified in the [LICENSE](https://choosealicense.com/licenses/mit/#) file.