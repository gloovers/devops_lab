import argparse
import calendar
import datetime
import getpass
import json
import requests
import time


def get_options():
    """Process path to config file."""
    parser = argparse.ArgumentParser(description="* Script gets PR statistic "
                                                 "from GitHub.Without options "
                                                 "script outlines common "
                                                 "information about git user "
                                                 "or specifed repo. *")
    parser.add_argument("--version", action="version", version="%(prog)s 1.0")
    parser.add_argument("--options", type=str, help="Set the options: "
                                                    "d-Number of days, "
                                                    "w-Day of the week opened,"
                                                    "h-Hour of the day opened,"
                                                    "u-User who opened,"
                                                    "l-Attached labels"
                                                    "(Working with --repo)")
    parser.add_argument("user", type=str, help="Specify a user of github.com")
    parser.add_argument("--repo", help="Specify the particular repo")
    args = parser.parse_args()
    return args.__dict__


def git_get_opt_repo(user, login, password, repo, opt):
    """Get main repo attributes"""
    r = requests.get("https://api.github.com/repos/%s/%s" % (user, repo),
                     auth=(login, password))
    output = json.loads(r.text)
    print("***\nCommon information about the Repository '{0}:'\n"
          "    Full name: {1},\n"
          "    HTML URL: {2},\n"
          "    Description: {3},\n"
          "    Forks Count: {4},\n"
          "    Pull Requests: {5}.".format(repo,
                                           output['full_name'],
                                           output['html_url'],
                                           output['description'],
                                           output['forks_count'],
                                           output['open_issues_count']))

    if opt:
        print("Additional attributes: ")
        options = [str for str in opt]
        if "l" in options:
            r = requests.get("https://api.github.com/repos/%s/%s/labels" %
                             (user, repo),
                             auth=(login, password))
            output_attr = json.loads(r.text)
            print("    Attached labels ({0}):".format(len(output_attr)))
            for label in output_attr:
                print("        -+- {0},".format(label["name"]))
        if "u" in options:
            print("    User who opened: {0}".format(output["owner"]["login"]))
        if "d" in options:
            date = datetime.datetime.strptime((output["created_at"]),
                                              "%Y-%m-%dT%H:%M:%SZ")
            unixtime = time.mktime(date.timetuple())
            delta = int(time.time() - unixtime) // 86400
            print("    Number of days opened: {0}".format(str(delta)))
        if "w" in options:
            date = datetime.datetime.strptime((output["created_at"]),
                                              "%Y-%m-%dT%H:%M:%SZ")
            print("    Day of the week opened: "
                  "{0}".format(str(calendar.day_name[date.weekday()])))
        if "h" in options:
            date = datetime.datetime.strptime((output["created_at"]),
                                              "%Y-%m-%dT%H:%M:%SZ")
            print("    Hour of the day opened: {0}".format(str(date.hour)))

    print("***")


def git_get_info_user(user, login, password):
    """Get info user."""
    r = requests.get("https://api.github.com/users/%s" % (user),
                     auth=(login, password))
    output = json.loads(r.text)
    r = requests.get("https://api.github.com/users/%s/repos" % (user),
                     auth=(login, password))
    output_repos = json.loads(r.text)
    print("***\nCommon information about the user '{0}:'\n"
          "    Name: {1},\n"
          "    Location: {2},\n"
          "    Email: {3},\n"
          "    Company: {4},\n"
          "    Public Repositories {5}:".format(user,
                                                output['name'],
                                                output['location'],
                                                output['email'],
                                                output['company'],
                                                output['public_repos']))

    for dicc in output_repos:
        print("        -+- {0}".format(dicc['full_name']))
    print("***")


def main_prog():
    """Main process."""
    options = get_options()
    login = input("***\nFor the connection to GitHub, "
                  "please enter the username and the password\nUser: ")
    password = getpass.getpass(prompt='Password: ', stream=None)
    if options['repo']:
        git_get_opt_repo(options['user'], login, password,
                         options['repo'], options['options'])
    else:
        git_get_info_user(options['user'], login, password)


main_prog()
